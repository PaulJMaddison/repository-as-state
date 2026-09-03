from pathlib import Path
import json
import subprocess

from ras.git_isolation import EXPERIMENT_BRANCH_NAME
from ras.workspace import main, materialize_pre_workspace


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return result.stdout.strip()


def source_repo(tmp_path: Path) -> tuple[Path, str, str]:
    repo = tmp_path / "source"
    repo.mkdir()
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "probe@example.invalid")
    git(repo, "config", "user.name", "Probe")
    (repo / "app.txt").write_text("PRE\n", encoding="utf-8")
    git(repo, "add", "app.txt")
    git(repo, "commit", "-q", "-m", "pre")
    pre = git(repo, "rev-parse", "HEAD")
    (repo / "app.txt").write_text("POST\n", encoding="utf-8")
    git(repo, "commit", "-q", "-am", "post")
    post = git(repo, "rev-parse", "HEAD")
    return repo, pre, post


def test_materialize_pre_workspace_returns_ready_writable_branch(tmp_path):
    source, pre, post = source_repo(tmp_path)
    destination = tmp_path / "workspace"

    result = materialize_pre_workspace(
        source,
        pre,
        destination,
        [post],
        network_isolation_asserted=True,
    )

    assert result.passed
    assert result.action == "PROCEED_TO_MODEL_INVOCATION"
    assert result.expected_commit == pre
    assert result.actual_commit == pre
    assert result.head_ref == f"refs/heads/{EXPERIMENT_BRANCH_NAME}"
    assert result.leak_gate.passed

    (destination / "edit.txt").write_text("write probe\n", encoding="utf-8")
    assert "?? edit.txt" in git(destination, "status", "--porcelain")


def test_materialize_pre_workspace_fails_closed_without_network_assertion(tmp_path):
    source, pre, post = source_repo(tmp_path)

    result = materialize_pre_workspace(
        source,
        pre,
        tmp_path / "workspace",
        [post],
        network_isolation_asserted=False,
    )

    assert not result.passed
    assert result.action == "STOP_BEFORE_MODEL_INVOCATION"
    assert "network_isolation_not_asserted" in result.leak_gate.failures


def test_cli_emits_machine_readable_success(tmp_path, capsys):
    source, pre, post = source_repo(tmp_path)
    destination = tmp_path / "workspace"

    exit_code = main(
        [
            "--source",
            str(source),
            "--commit",
            pre,
            "--destination",
            str(destination),
            "--forbid",
            post,
            "--network-isolation-asserted",
        ]
    )

    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload["passed"] is True
    assert payload["head_ref"] == f"refs/heads/{EXPERIMENT_BRANCH_NAME}"


def test_cli_fails_closed_for_existing_destination(tmp_path, capsys):
    source, pre, post = source_repo(tmp_path)
    destination = tmp_path / "workspace"
    destination.mkdir()

    exit_code = main(
        [
            "--source",
            str(source),
            "--commit",
            pre,
            "--destination",
            str(destination),
            "--forbid",
            post,
            "--network-isolation-asserted",
        ]
    )

    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 2
    assert payload["passed"] is False
    assert payload["action"] == "STOP_BEFORE_MODEL_INVOCATION"
