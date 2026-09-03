from pathlib import Path
import sys
import textwrap
import time

import pytest

from ras.execution import ProcessStatus, SupervisionPolicy, run_supervised


def python_cmd(source: str) -> list[str]:
    return [sys.executable, "-c", textwrap.dedent(source)]


def test_run_supervised_completes_and_captures_output():
    result = run_supervised(
        python_cmd("print('done')"),
        policy=SupervisionPolicy(
            stall_timeout_s=1,
            hard_timeout_s=2,
            poll_interval_s=0.02,
        ),
    )

    assert result.status is ProcessStatus.COMPLETED
    assert result.returncode == 0
    assert result.succeeded
    assert result.result_available
    assert result.stdout_tail == ("done",)


def test_nonzero_exit_is_completed_but_not_successful():
    result = run_supervised(
        python_cmd("import sys; print('bad', file=sys.stderr); sys.exit(7)"),
        policy=SupervisionPolicy(
            stall_timeout_s=1,
            hard_timeout_s=2,
            poll_interval_s=0.02,
        ),
    )

    assert result.status is ProcessStatus.COMPLETED
    assert result.returncode == 7
    assert not result.succeeded
    assert result.result_available
    assert result.stderr_tail == ("bad",)


def test_output_heartbeats_prevent_false_stall():
    result = run_supervised(
        python_cmd(
            """
            import time
            for i in range(4):
                print(i, flush=True)
                time.sleep(0.12)
            """
        ),
        policy=SupervisionPolicy(
            stall_timeout_s=0.80,
            hard_timeout_s=3,
            poll_interval_s=0.02,
        ),
    )

    assert result.status is ProcessStatus.COMPLETED
    assert result.returncode == 0
    assert result.stdout_tail[-1] == "3"


def test_progress_file_heartbeats_prevent_false_stall(tmp_path: Path):
    progress = tmp_path / "progress.txt"
    result = run_supervised(
        python_cmd(
            f"""
            from pathlib import Path
            import time
            p = Path({str(progress)!r})
            for i in range(4):
                p.write_text(str(i))
                time.sleep(0.14)
            """
        ),
        policy=SupervisionPolicy(
            stall_timeout_s=0.30,
            hard_timeout_s=2,
            poll_interval_s=0.02,
            progress_file=progress,
        ),
    )

    assert result.status is ProcessStatus.COMPLETED
    assert result.returncode == 0
    assert result.last_progress_kind in {"progress_file", "stdout", "stderr"}


def test_stall_timeout_kills_process_quickly():
    result = run_supervised(
        python_cmd("import time; time.sleep(5)"),
        policy=SupervisionPolicy(
            stall_timeout_s=0.80,
            hard_timeout_s=3,
            poll_interval_s=0.02,
            terminate_grace_s=0.1,
        ),
    )

    assert result.status is ProcessStatus.STALL_TIMEOUT
    assert not result.result_available
    assert result.duration_s < 2.0


def test_hard_timeout_applies_even_with_continuous_output():
    result = run_supervised(
        python_cmd(
            """
            import time
            for i in range(100):
                print(i, flush=True)
                time.sleep(0.04)
            """
        ),
        policy=SupervisionPolicy(
            stall_timeout_s=0.80,
            hard_timeout_s=1.20,
            poll_interval_s=0.02,
            terminate_grace_s=0.1,
        ),
    )

    assert result.status is ProcessStatus.HARD_TIMEOUT
    assert not result.result_available
    assert result.duration_s < 2.0


def test_completion_file_ends_irrelevant_process_tail(tmp_path: Path):
    done = tmp_path / "verifier.done"
    result = run_supervised(
        python_cmd(
            f"""
            from pathlib import Path
            import time
            Path({str(done)!r}).write_text('result-ready')
            time.sleep(5)
            """
        ),
        policy=SupervisionPolicy(
            stall_timeout_s=1,
            hard_timeout_s=2,
            poll_interval_s=0.02,
            terminate_grace_s=0.1,
            completion_file=done,
        ),
    )

    assert result.status is ProcessStatus.COMPLETION_SIGNAL
    assert not result.succeeded
    assert result.result_available
    assert result.duration_s < 2.0
    assert done.read_text() == "result-ready"


def test_stale_completion_file_does_not_short_circuit_new_run(tmp_path: Path):
    done = tmp_path / "verifier.done"
    done.write_text("old")
    started = time.monotonic()

    result = run_supervised(
        python_cmd(
            f"""
            from pathlib import Path
            import time
            time.sleep(0.25)
            Path({str(done)!r}).write_text('new-result')
            time.sleep(5)
            """
        ),
        policy=SupervisionPolicy(
            stall_timeout_s=1,
            hard_timeout_s=2,
            poll_interval_s=0.02,
            terminate_grace_s=0.1,
            completion_file=done,
        ),
    )

    elapsed = time.monotonic() - started
    assert result.status is ProcessStatus.COMPLETION_SIGNAL
    assert result.result_available
    assert elapsed >= 0.20
    assert done.read_text() == "new-result"


def test_output_tail_is_bounded():
    result = run_supervised(
        python_cmd("for i in range(20): print(i)"),
        policy=SupervisionPolicy(
            stall_timeout_s=1,
            hard_timeout_s=2,
            poll_interval_s=0.02,
            max_output_lines=3,
        ),
    )

    assert result.status is ProcessStatus.COMPLETED
    assert result.stdout_tail == ("17", "18", "19")


@pytest.mark.parametrize(
    "kwargs",
    [
        {"stall_timeout_s": 0},
        {"hard_timeout_s": 0},
        {"poll_interval_s": 0},
        {"terminate_grace_s": -1},
        {"max_output_lines": 0},
    ],
)
def test_policy_rejects_invalid_values(kwargs):
    with pytest.raises(ValueError):
        SupervisionPolicy(**kwargs)


def test_empty_command_is_rejected():
    with pytest.raises(ValueError):
        run_supervised([])
