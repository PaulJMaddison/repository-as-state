"""Canonical workspace materialisation for RaS experiments.

HARNESS CODE ONLY. This module makes the PRE workspace state explicit and
fail-closed; it is not evidence that Repository-as-State works.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import subprocess
from typing import Sequence

from .git_isolation import (
    EXPERIMENT_BRANCH_NAME,
    LeakGateResult,
    create_truncated_workspace,
    future_history_leak_gate,
)


@dataclass(frozen=True)
class WorkspaceMaterialisationResult:
    passed: bool
    action: str
    destination: str
    expected_commit: str
    actual_commit: str
    actual_tree: str
    head_ref: str
    branch_name: str
    leak_gate: LeakGateResult

    def as_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["leak_gate"] = self.leak_gate.as_dict()
        return data


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def materialize_pre_workspace(
    source_repo: str | Path,
    allowed_commit: str,
    destination: str | Path,
    forbidden_future_oids: Sequence[str],
    *,
    network_isolation_asserted: bool,
    branch_name: str = EXPERIMENT_BRANCH_NAME,
    sidecar_roots: Sequence[str | Path] = (),
) -> WorkspaceMaterialisationResult:
    """Create and independently validate one exact writable PRE workspace."""

    workspace = create_truncated_workspace(
        source_repo,
        allowed_commit,
        destination,
        branch_name=branch_name,
    )

    expected_commit = _git(workspace, "rev-parse", allowed_commit).lower()
    actual_commit = _git(workspace, "rev-parse", "HEAD").lower()
    actual_tree = _git(workspace, "rev-parse", "HEAD^{tree}").lower()
    head_ref = _git(workspace, "symbolic-ref", "HEAD")

    gate = future_history_leak_gate(
        workspace,
        forbidden_future_oids,
        allowed_refs=(f"refs/heads/{branch_name}",),
        network_isolation_asserted=network_isolation_asserted,
        sidecar_roots=sidecar_roots,
    )

    identity_matches = actual_commit == expected_commit
    branch_matches = head_ref == f"refs/heads/{branch_name}"
    passed = identity_matches and branch_matches and gate.passed

    return WorkspaceMaterialisationResult(
        passed=passed,
        action="PROCEED_TO_MODEL_INVOCATION" if passed else "STOP_BEFORE_MODEL_INVOCATION",
        destination=str(workspace),
        expected_commit=expected_commit,
        actual_commit=actual_commit,
        actual_tree=actual_tree,
        head_ref=head_ref,
        branch_name=branch_name,
        leak_gate=gate,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Materialise an exact writable historical PRE workspace and run the leak gate."
    )
    parser.add_argument("--source", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--destination", required=True)
    parser.add_argument("--forbid", action="append", default=[])
    parser.add_argument("--branch", default=EXPERIMENT_BRANCH_NAME)
    parser.add_argument(
        "--network-isolation-asserted",
        action="store_true",
        help="Assert that the caller has independently enforced the frozen network boundary.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = materialize_pre_workspace(
            args.source,
            args.commit,
            args.destination,
            args.forbid,
            network_isolation_asserted=args.network_isolation_asserted,
            branch_name=args.branch,
        )
    except Exception as exc:
        print(
            json.dumps(
                {
                    "passed": False,
                    "action": "STOP_BEFORE_MODEL_INVOCATION",
                    "error": f"{type(exc).__name__}: {exc}",
                },
                sort_keys=True,
            )
        )
        return 2

    print(json.dumps(result.as_dict(), sort_keys=True))
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
