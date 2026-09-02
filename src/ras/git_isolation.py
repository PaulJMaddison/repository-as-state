"""Fail-closed Git isolation checks for Repository-as-State experiments.

HARNESS CODE ONLY. Passing these checks is not evidence that RaS works.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import os
import re
import shutil
import subprocess
from typing import Iterable, Sequence

_OID_RE = re.compile(r"^[0-9a-fA-F]{40}([0-9a-fA-F]{24})?$")
_SIDECAR_SUFFIXES = (".patch", ".diff", ".bundle", ".zip", ".tar", ".tgz", ".tar.gz", ".7z")


@dataclass(frozen=True)
class LeakGateResult:
    passed: bool
    run_valid: bool
    action: str
    failures: tuple[str, ...]
    details: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def _run_git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        raise ValueError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result


def _validate_repo_path(repo: Path) -> Path:
    try:
        resolved = repo.resolve(strict=True)
    except (FileNotFoundError, OSError) as exc:
        raise ValueError("repository path does not exist or cannot be resolved") from exc
    if not resolved.is_dir():
        raise ValueError("repository path is not a directory")
    dot_git = resolved / ".git"
    if not dot_git.exists():
        raise ValueError("not a Git working repository")
    if dot_git.is_symlink() or not dot_git.is_dir():
        raise ValueError("linked worktrees and symlinked .git directories are not allowed")
    probe = _run_git(resolved, "rev-parse", "--is-inside-work-tree", check=False)
    if probe.returncode != 0 or probe.stdout.strip() != "true":
        raise ValueError("not a valid Git working tree")
    return resolved


def _normalise_oids(oids: Iterable[str]) -> tuple[str, ...]:
    result: list[str] = []
    seen: set[str] = set()
    for oid in oids:
        if not isinstance(oid, str) or not _OID_RE.fullmatch(oid):
            raise ValueError(f"invalid Git object id: {oid!r}")
        lowered = oid.lower()
        if lowered not in seen:
            seen.add(lowered)
            result.append(lowered)
    return tuple(sorted(result))


def _all_objects(repo: Path) -> set[str]:
    result = _run_git(repo, "cat-file", "--batch-all-objects", "--batch-check=%(objectname)")
    return {line.strip().lower() for line in result.stdout.splitlines() if line.strip()}


def _reachable_objects(repo: Path) -> set[str]:
    result = _run_git(repo, "rev-list", "--objects", "--all")
    return {line.split(" ", 1)[0].strip().lower() for line in result.stdout.splitlines() if line.strip()}


def _refs(repo: Path) -> dict[str, str]:
    result = _run_git(repo, "for-each-ref", "--format=%(refname) %(objectname)")
    refs: dict[str, str] = {}
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        name, oid = line.split(" ", 1)
        refs[name] = oid.strip().lower()
    return refs


def _reflog_oids(repo: Path) -> set[str]:
    result = _run_git(repo, "reflog", "show", "--all", "--format=%H", check=False)
    if result.returncode not in (0, 1):
        raise ValueError(f"git reflog failed: {result.stderr.strip()}")
    return {line.strip().lower() for line in result.stdout.splitlines() if line.strip()}


def _outside_symlinks(repo: Path) -> list[str]:
    failures: list[str] = []
    root = repo.resolve()
    for current, dirs, files in os.walk(repo, followlinks=False):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in [*dirs, *files]:
            path = Path(current) / name
            if not path.is_symlink():
                continue
            try:
                target = path.resolve(strict=True)
            except (FileNotFoundError, OSError):
                failures.append(str(path.relative_to(repo)))
                continue
            try:
                target.relative_to(root)
            except ValueError:
                failures.append(str(path.relative_to(repo)))
    return sorted(set(failures))


def create_truncated_workspace(
    source_repo: str | Path,
    allowed_commit: str,
    destination: str | Path,
    branch_name: str = "p0",
) -> Path:
    """Create a fresh repo containing only objects needed by allowed_commit ancestry.

    The source repository is never modified. The destination is created via a
    direct no-tag fetch of the allowed commit, then stripped of FETCH_HEAD and
    validated separately by future_history_leak_gate.
    """
    source = _validate_repo_path(Path(source_repo))
    allowed = _normalise_oids([allowed_commit])[0]
    destination_path = Path(destination)
    if destination_path.exists():
        raise ValueError("destination already exists")
    source_real = source.resolve()
    destination_parent = destination_path.parent.resolve(strict=True)
    try:
        destination_parent.relative_to(source_real)
    except ValueError:
        pass
    else:
        raise ValueError("destination must not be inside the source repository")

    subprocess.run(["git", "init", "-q", str(destination_path)], check=True)
    fetch = subprocess.run(
        [
            "git",
            "-c",
            "protocol.file.allow=always",
            "-C",
            str(destination_path),
            "fetch",
            "--no-tags",
            "--no-write-fetch-head",
            str(source),
            allowed,
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if fetch.returncode != 0:
        shutil.rmtree(destination_path, ignore_errors=True)
        raise ValueError(f"history export failed: {fetch.stderr.strip()}")

    _run_git(destination_path, "update-ref", f"refs/heads/{branch_name}", allowed)
    _run_git(destination_path, "symbolic-ref", "HEAD", f"refs/heads/{branch_name}")
    _run_git(destination_path, "reset", "--hard", allowed)
    return destination_path


def future_history_leak_gate(
    repo: str | Path,
    forbidden_future_oids: Sequence[str],
    *,
    allowed_refs: Sequence[str] = ("refs/heads/p0",),
    network_isolation_asserted: bool,
    sidecar_roots: Sequence[str | Path] = (),
) -> LeakGateResult:
    """Fail closed if a P0 workspace exposes state outside its allowed Git closure."""
    failures: list[str] = []
    details: list[str] = []
    try:
        raw_repo = Path(repo)
        try:
            prelim = raw_repo.resolve(strict=True)
        except (FileNotFoundError, OSError) as exc:
            raise ValueError("repository path does not exist or cannot be resolved") from exc
        prelim_git = prelim / ".git"
        if prelim_git.is_file() or prelim_git.is_symlink():
            failures.append("linked_worktree_or_source_link")
            raise ValueError("linked worktree .git indirection is not allowed")
        root = _validate_repo_path(prelim)
        forbidden = _normalise_oids(forbidden_future_oids)
        allowed_ref_set = set(allowed_refs)
        if not allowed_ref_set or any(not ref.startswith("refs/") for ref in allowed_ref_set):
            raise ValueError("allowed_refs must contain one or more full refs/* names")

        remotes = tuple(sorted(filter(None, _run_git(root, "remote").stdout.splitlines())))
        if remotes:
            failures.append("remote_configured")
            details.append("remotes=" + ",".join(remotes))

        alternates = root / ".git" / "objects" / "info" / "alternates"
        if alternates.exists():
            try:
                alternate_text = alternates.read_text(encoding="utf-8").strip()
            except (OSError, UnicodeError) as exc:
                failures.append("alternates_unreadable")
                details.append(type(exc).__name__)
            else:
                if alternate_text:
                    failures.append("git_alternates_present")

        refs = _refs(root)
        unexpected_refs = sorted(set(refs) - allowed_ref_set)
        if unexpected_refs:
            failures.append("unexpected_refs_or_tags")
            details.append("unexpected_refs=" + ",".join(unexpected_refs))
        missing_refs = sorted(allowed_ref_set - set(refs))
        if missing_refs:
            failures.append("required_allowed_ref_missing")
            details.append("missing_refs=" + ",".join(missing_refs))

        reachable = _reachable_objects(root)
        all_objects = _all_objects(root)
        extra_objects = sorted(all_objects - reachable)
        if extra_objects:
            failures.append("unreachable_extra_objects")
            details.append(f"unreachable_object_count={len(extra_objects)}")

        reflog = _reflog_oids(root)
        reflog_outside = sorted(reflog - reachable)
        if reflog_outside:
            failures.append("reflog_exposes_unreachable_history")
            details.append(f"reflog_unreachable_count={len(reflog_outside)}")

        for oid in forbidden:
            probe = _run_git(root, "cat-file", "-e", f"{oid}^{{commit}}", check=False)
            if probe.returncode == 0:
                failures.append("forbidden_future_oid_resolves")
                details.append(f"forbidden_oid={oid}")

        status = _run_git(root, "status", "--porcelain=v1", "--untracked-files=all").stdout.strip()
        if status:
            failures.append("workspace_not_clean")

        outside_links = _outside_symlinks(root)
        if outside_links:
            failures.append("symlink_escape")
            details.append("outside_symlinks=" + ",".join(outside_links))

        roots = [root, *(Path(p) for p in sidecar_roots)]
        sidecars: list[str] = []
        for scan_root in roots:
            try:
                scan = scan_root.resolve(strict=True)
            except (FileNotFoundError, OSError):
                failures.append("sidecar_root_unreadable")
                continue
            if not scan.is_dir():
                failures.append("sidecar_root_not_directory")
                continue
            for path in scan.iterdir():
                lower = path.name.lower()
                if any(lower.endswith(suffix) for suffix in _SIDECAR_SUFFIXES):
                    sidecars.append(str(path))
        if sidecars:
            failures.append("future_state_sidecar_present")
            details.append(f"sidecar_count={len(sidecars)}")

        worktrees = _run_git(root, "worktree", "list", "--porcelain").stdout
        worktree_paths = [
            line.split(" ", 1)[1]
            for line in worktrees.splitlines()
            if line.startswith("worktree ")
        ]
        if len(worktree_paths) != 1 or Path(worktree_paths[0]).resolve() != root:
            failures.append("linked_worktree_or_source_link")

        if not network_isolation_asserted:
            failures.append("network_isolation_not_asserted")

    except Exception as exc:
        failures.append("gate_internal_or_repository_error")
        details.append(f"{type(exc).__name__}: {exc}")

    unique_failures = tuple(sorted(set(failures)))
    unique_details = tuple(sorted(set(details)))
    passed = not unique_failures
    return LeakGateResult(
        passed=passed,
        run_valid=passed,
        action="PROCEED_TO_MODEL_INVOCATION" if passed else "STOP_BEFORE_MODEL_INVOCATION",
        failures=unique_failures,
        details=unique_details,
    )
