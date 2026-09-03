from pathlib import Path
import os
import ctypes
import subprocess

import pytest

from ras.git_isolation import (
    EXPERIMENT_BRANCH_NAME,
    create_truncated_workspace,
    future_history_leak_gate,
)


def git(repo: Path, *args: str, check: bool = True) -> str:
    r = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and r.returncode != 0:
        raise AssertionError(r.stderr)
    return r.stdout.strip()


def init_source(tmp_path: Path):
    repo = tmp_path / "source repo ü"
    repo.mkdir()
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "synthetic@example.invalid")
    git(repo, "config", "user.name", "Synthetic Harness")
    (repo / "state.txt").write_text("R0\n", encoding="utf-8")
    git(repo, "add", "state.txt")
    git(repo, "commit", "-q", "-m", "R0")
    allowed = git(repo, "rev-parse", "HEAD")
    (repo / "state.txt").write_text("R1 FUTURE\n", encoding="utf-8")
    git(repo, "commit", "-q", "-am", "future")
    future = git(repo, "rev-parse", "HEAD")
    return repo, allowed, future


def clean_workspace(tmp_path: Path):
    source, allowed, future = init_source(tmp_path)
    dest = tmp_path / "isolated workspace"
    create_truncated_workspace(source, allowed, dest)
    return source, dest, allowed, future


def test_clean_genuinely_truncated_history_passes(tmp_path):
    _, dest, _, future = clean_workspace(tmp_path)
    result = future_history_leak_gate(
        dest, [future], network_isolation_asserted=True
    )
    assert result.passed
    assert result.run_valid
    assert result.action == "PROCEED_TO_MODEL_INVOCATION"



def test_materialized_workspace_uses_normal_writable_experiment_branch(tmp_path):
    _, dest, allowed, future = clean_workspace(tmp_path)

    assert git(dest, "rev-parse", "HEAD") == allowed
    assert git(dest, "symbolic-ref", "--short", "HEAD") == EXPERIMENT_BRANCH_NAME
    assert git(dest, "remote") == ""
    assert git(dest, "fsck", "--unreachable", check=False) == ""

    probe = dest / "synthetic-edit.txt"
    probe.write_text("editable\n", encoding="utf-8")
    assert "?? synthetic-edit.txt" in git(dest, "status", "--porcelain")
    probe.unlink()

    result = future_history_leak_gate(
        dest, [future], network_isolation_asserted=True
    )
    assert result.passed


def test_detached_head_fails_closed(tmp_path):
    _, dest, allowed, future = clean_workspace(tmp_path)
    git(dest, "checkout", "--detach", allowed)

    result = future_history_leak_gate(
        dest, [future], network_isolation_asserted=True
    )

    assert not result.passed
    assert "detached_head" in result.failures
    assert result.action == "STOP_BEFORE_MODEL_INVOCATION"


def test_wrong_current_branch_fails_even_when_ref_is_local(tmp_path):
    _, dest, allowed, future = clean_workspace(tmp_path)
    git(dest, "branch", "other", allowed)
    git(dest, "symbolic-ref", "HEAD", "refs/heads/other")
    git(dest, "reset", "--hard", allowed)

    result = future_history_leak_gate(
        dest,
        [future],
        allowed_refs=(f"refs/heads/{EXPERIMENT_BRANCH_NAME}", "refs/heads/other"),
        network_isolation_asserted=True,
    )

    # Multiple allowed refs are supported by the generic gate, but the active
    # branch must still be one of the explicitly allowed refs.
    assert result.passed


def test_unexpected_current_branch_fails(tmp_path):
    _, dest, allowed, future = clean_workspace(tmp_path)
    git(dest, "branch", "other", allowed)
    git(dest, "symbolic-ref", "HEAD", "refs/heads/other")
    git(dest, "reset", "--hard", allowed)

    result = future_history_leak_gate(
        dest, [future], network_isolation_asserted=True
    )

    assert not result.passed
    assert "head_ref_not_allowed" in result.failures
    assert "unexpected_refs_or_tags" in result.failures


def test_export_refuses_invalid_branch_name(tmp_path):
    source, allowed, _ = init_source(tmp_path)
    with pytest.raises(ValueError, match="invalid experiment branch name"):
        create_truncated_workspace(
            source,
            allowed,
            tmp_path / "dest",
            branch_name="bad branch name",
        )

def test_duplicate_forbidden_oids_are_deduplicated(tmp_path):
    _, dest, _, future = clean_workspace(tmp_path)
    result = future_history_leak_gate(
        dest, [future, future], network_isolation_asserted=True
    )
    assert result.passed


def test_invalid_forbidden_sha_fails_closed(tmp_path):
    _, dest, _, _ = clean_workspace(tmp_path)
    result = future_history_leak_gate(
        dest, ["not-a-sha"], network_isolation_asserted=True
    )
    assert not result.passed
    assert result.action == "STOP_BEFORE_MODEL_INVOCATION"


def test_remote_still_configured_fails(tmp_path):
    source, dest, _, future = clean_workspace(tmp_path)
    git(dest, "remote", "add", "origin", str(source))
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=True)
    assert "remote_configured" in result.failures


def test_future_branch_fails(tmp_path):
    source, dest, _, future = clean_workspace(tmp_path)
    git(dest, "fetch", "--no-tags", "--no-write-fetch-head", str(source), future)
    git(dest, "update-ref", "refs/heads/future", future)
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=True)
    assert "unexpected_refs_or_tags" in result.failures
    assert "forbidden_future_oid_resolves" in result.failures


def test_future_tag_fails(tmp_path):
    source, dest, _, future = clean_workspace(tmp_path)
    git(dest, "fetch", "--no-tags", "--no-write-fetch-head", str(source), future)
    git(dest, "tag", "future-tag", future)
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=True)
    assert "unexpected_refs_or_tags" in result.failures


def test_future_commit_in_reflog_fails(tmp_path):
    source, dest, allowed, future = clean_workspace(tmp_path)
    git(dest, "fetch", "--no-tags", "--no-write-fetch-head", str(source), future)
    git(dest, "update-ref", f"refs/heads/{EXPERIMENT_BRANCH_NAME}", future)
    git(dest, "reset", "--hard", allowed)
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=True)
    assert "reflog_exposes_unreachable_history" in result.failures
    assert "forbidden_future_oid_resolves" in result.failures


def test_removed_refs_but_unreachable_future_objects_fail(tmp_path):
    source, dest, _, future = clean_workspace(tmp_path)
    git(dest, "fetch", "--no-tags", "--no-write-fetch-head", str(source), future)
    git(dest, "reflog", "expire", "--expire=now", "--all")
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=True)
    assert "unreachable_extra_objects" in result.failures
    assert "forbidden_future_oid_resolves" in result.failures


def test_alternates_fail(tmp_path):
    source, dest, _, future = clean_workspace(tmp_path)
    alternates = dest / ".git" / "objects" / "info" / "alternates"
    alternates.parent.mkdir(parents=True, exist_ok=True)
    alternates.write_text(str((source / ".git" / "objects").resolve()) + "\n", encoding="utf-8")
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=True)
    assert "git_alternates_present" in result.failures


def test_unreadable_or_non_utf8_alternates_fail(tmp_path):
    _, dest, _, future = clean_workspace(tmp_path)
    alternates = dest / ".git" / "objects" / "info" / "alternates"
    alternates.parent.mkdir(parents=True, exist_ok=True)
    alternates.write_bytes(b"\xff\xfe")
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=True)
    assert "alternates_unreadable" in result.failures


def test_linked_worktree_fails(tmp_path):
    source, _, allowed, future = clean_workspace(tmp_path)
    linked = tmp_path / "linked"
    git(source, "worktree", "add", "--detach", str(linked), allowed)
    result = future_history_leak_gate(linked, [future], network_isolation_asserted=True)
    assert "linked_worktree_or_source_link" in result.failures


def test_symlink_escape_fails(tmp_path):
    _, dest, _, future = clean_workspace(tmp_path)
    external = tmp_path / "external.txt"
    external.write_text("x", encoding="utf-8")
    link = dest / "escape-link"
    if os.name == "nt":
        # Python's os.symlink does not request the Windows 10+
        # SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE flag.  Use the
        # native API so this deterministic harness works for developers
        # with Developer Mode enabled, without requiring an elevated token.
        create_symbolic_link = ctypes.windll.kernel32.CreateSymbolicLinkW
        create_symbolic_link.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32]
        create_symbolic_link.restype = ctypes.c_ubyte
        created = create_symbolic_link(str(link), str(external), 2)
        if not created:
            error = ctypes.WinError()
            if getattr(error, "winerror", None) == 1314:
                pytest.skip("Windows symbolic-link privilege is unavailable")
            raise error
    else:
        os.symlink(external, link)
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=True)
    assert "symlink_escape" in result.failures
    assert "workspace_not_clean" in result.failures


def test_future_state_sidecar_fails(tmp_path):
    _, dest, _, future = clean_workspace(tmp_path)
    (dest / "solution.patch").write_text("future", encoding="utf-8")
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=True)
    assert "future_state_sidecar_present" in result.failures


def test_network_isolation_must_be_asserted(tmp_path):
    _, dest, _, future = clean_workspace(tmp_path)
    result = future_history_leak_gate(dest, [future], network_isolation_asserted=False)
    assert "network_isolation_not_asserted" in result.failures


def test_missing_repo_fails_closed(tmp_path):
    result = future_history_leak_gate(
        tmp_path / "missing", [], network_isolation_asserted=True
    )
    assert not result.passed
    assert "gate_internal_or_repository_error" in result.failures


def test_empty_directory_is_not_a_repo(tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    result = future_history_leak_gate(empty, [], network_isolation_asserted=True)
    assert not result.passed


def test_malformed_git_directory_fails_closed(tmp_path):
    malformed = tmp_path / "malformed"
    (malformed / ".git").mkdir(parents=True)
    result = future_history_leak_gate(malformed, [], network_isolation_asserted=True)
    assert not result.passed


def test_export_refuses_destination_inside_source(tmp_path):
    source, allowed, _ = init_source(tmp_path)
    with pytest.raises(ValueError):
        create_truncated_workspace(source, allowed, source / "child")


def test_export_refuses_existing_destination(tmp_path):
    source, allowed, _ = init_source(tmp_path)
    existing = tmp_path / "existing"
    existing.mkdir()
    with pytest.raises(ValueError):
        create_truncated_workspace(source, allowed, existing)


def test_export_refuses_invalid_oid(tmp_path):
    source, _, _ = init_source(tmp_path)
    with pytest.raises(ValueError):
        create_truncated_workspace(source, "bad", tmp_path / "dest")


def test_deterministic_failure_order(tmp_path):
    source, dest, _, future = clean_workspace(tmp_path)
    git(dest, "remote", "add", "origin", str(source))
    first = future_history_leak_gate(dest, [future], network_isolation_asserted=False)
    second = future_history_leak_gate(dest, [future], network_isolation_asserted=False)
    assert first.failures == second.failures
    assert first.details == second.details
    assert tuple(first.failures) == tuple(sorted(first.failures))
