"""Deterministic subprocess supervision for Repository-as-State tooling.

High-capability reasoners should make decisions, not babysit subprocesses.
This module provides a small mechanical controller with bounded waiting,
progress heartbeats, stall detection, hard deadlines and structured outcomes.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from enum import Enum
import os
from pathlib import Path
import queue
import signal
import subprocess
import threading
import time
from typing import Mapping, Sequence


class ProcessStatus(str, Enum):
    COMPLETED = "completed"
    STALL_TIMEOUT = "stall_timeout"
    HARD_TIMEOUT = "hard_timeout"
    COMPLETION_SIGNAL = "completion_signal"


@dataclass(frozen=True)
class SupervisionPolicy:
    """Bounds and progress rules for one subprocess invocation."""

    stall_timeout_s: float = 30.0
    hard_timeout_s: float = 120.0
    poll_interval_s: float = 0.10
    terminate_grace_s: float = 2.0
    completion_file: Path | None = None
    progress_file: Path | None = None
    max_output_lines: int = 200

    def __post_init__(self) -> None:
        if self.stall_timeout_s <= 0:
            raise ValueError("stall_timeout_s must be greater than zero")
        if self.hard_timeout_s <= 0:
            raise ValueError("hard_timeout_s must be greater than zero")
        if self.poll_interval_s <= 0:
            raise ValueError("poll_interval_s must be greater than zero")
        if self.terminate_grace_s < 0:
            raise ValueError("terminate_grace_s must be non-negative")
        if self.max_output_lines < 1:
            raise ValueError("max_output_lines must be at least one")


@dataclass(frozen=True)
class SupervisedProcessResult:
    status: ProcessStatus
    returncode: int | None
    pid: int
    duration_s: float
    last_progress_age_s: float
    last_progress_kind: str
    stdout_tail: tuple[str, ...]
    stderr_tail: tuple[str, ...]

    @property
    def succeeded(self) -> bool:
        """Whether the child itself exited successfully."""

        return self.status is ProcessStatus.COMPLETED and self.returncode == 0

    @property
    def result_available(self) -> bool:
        """Whether the caller can now inspect the child's structured result."""

        return self.status in {
            ProcessStatus.COMPLETED,
            ProcessStatus.COMPLETION_SIGNAL,
        }


@dataclass(frozen=True)
class _OutputEvent:
    stream: str
    line: str
    at: float


def _pump_lines(stream, name: str, events: "queue.Queue[_OutputEvent]") -> None:
    try:
        for line in iter(stream.readline, ""):
            events.put(_OutputEvent(name, line.rstrip("\r\n"), time.monotonic()))
    finally:
        stream.close()


def _file_signature(path: Path | None) -> tuple[int, int] | None:
    if path is None:
        return None
    try:
        stat = path.stat()
    except FileNotFoundError:
        return None
    return (stat.st_mtime_ns, stat.st_size)


def _terminate_process_tree(process: subprocess.Popen[str], grace_s: float) -> None:
    """Terminate the supervised process and its descendants where supported."""

    if process.poll() is not None:
        return

    if os.name == "nt":
        # dotnet test and similar commands commonly spawn testhost children.
        # taskkill /T prevents a timed-out supervisor from leaving them behind.
        completed = subprocess.run(
            ["taskkill", "/PID", str(process.pid), "/T", "/F"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if completed.returncode == 0:
            try:
                process.wait(timeout=max(grace_s, 0.1))
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            return

        # Fallback for environments where taskkill is unavailable or denied.
        process.terminate()
        try:
            process.wait(timeout=grace_s)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
        return

    try:
        process_group = os.getpgid(process.pid)
    except ProcessLookupError:
        return

    os.killpg(process_group, signal.SIGTERM)
    try:
        process.wait(timeout=grace_s)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(process_group, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait()


def run_supervised(
    command: Sequence[str],
    *,
    cwd: str | os.PathLike[str] | None = None,
    env: Mapping[str, str] | None = None,
    policy: SupervisionPolicy | None = None,
) -> SupervisedProcessResult:
    """Run *command* under bounded deterministic supervision.

    Progress is any stdout/stderr line or a change to the configured progress
    file. A completion file is an explicit signal owned by the child process.
    Existing/stale files are baselined before launch so they cannot complete a
    later invocation accidentally.

    A completion signal means "structured result is ready", not "the verifier
    passed". The caller must inspect that result independently.
    """

    if not command:
        raise ValueError("command must not be empty")
    policy = policy or SupervisionPolicy()

    completion_signature = _file_signature(policy.completion_file)
    progress_signature = _file_signature(policy.progress_file)

    popen_kwargs: dict[str, object] = {}
    if os.name == "nt":
        popen_kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
    else:
        popen_kwargs["start_new_session"] = True

    started = time.monotonic()
    process = subprocess.Popen(
        list(command),
        cwd=cwd,
        env=dict(env) if env is not None else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        **popen_kwargs,
    )
    assert process.stdout is not None
    assert process.stderr is not None

    events: "queue.Queue[_OutputEvent]" = queue.Queue()
    threads = [
        threading.Thread(
            target=_pump_lines,
            args=(process.stdout, "stdout", events),
            daemon=True,
        ),
        threading.Thread(
            target=_pump_lines,
            args=(process.stderr, "stderr", events),
            daemon=True,
        ),
    ]
    for thread in threads:
        thread.start()

    stdout_tail: deque[str] = deque(maxlen=policy.max_output_lines)
    stderr_tail: deque[str] = deque(maxlen=policy.max_output_lines)
    last_progress_at = started
    last_progress_kind = "started"

    while True:
        now = time.monotonic()

        while True:
            try:
                event = events.get_nowait()
            except queue.Empty:
                break
            if event.stream == "stdout":
                stdout_tail.append(event.line)
            else:
                stderr_tail.append(event.line)
            last_progress_at = event.at
            last_progress_kind = event.stream

        current_progress_signature = _file_signature(policy.progress_file)
        if (
            policy.progress_file is not None
            and current_progress_signature is not None
            and current_progress_signature != progress_signature
        ):
            progress_signature = current_progress_signature
            last_progress_at = now
            last_progress_kind = "progress_file"

        current_completion_signature = _file_signature(policy.completion_file)
        if (
            policy.completion_file is not None
            and current_completion_signature is not None
            and current_completion_signature != completion_signature
        ):
            _terminate_process_tree(process, policy.terminate_grace_s)
            ended = time.monotonic()
            return SupervisedProcessResult(
                status=ProcessStatus.COMPLETION_SIGNAL,
                returncode=None,
                pid=process.pid,
                duration_s=ended - started,
                last_progress_age_s=0.0,
                last_progress_kind="completion_file",
                stdout_tail=tuple(stdout_tail),
                stderr_tail=tuple(stderr_tail),
            )

        returncode = process.poll()
        if returncode is not None:
            for thread in threads:
                thread.join(timeout=0.2)
            while True:
                try:
                    event = events.get_nowait()
                except queue.Empty:
                    break
                target = stdout_tail if event.stream == "stdout" else stderr_tail
                target.append(event.line)
            ended = time.monotonic()
            return SupervisedProcessResult(
                status=ProcessStatus.COMPLETED,
                returncode=returncode,
                pid=process.pid,
                duration_s=ended - started,
                last_progress_age_s=max(0.0, ended - last_progress_at),
                last_progress_kind=last_progress_kind,
                stdout_tail=tuple(stdout_tail),
                stderr_tail=tuple(stderr_tail),
            )

        if now - started >= policy.hard_timeout_s:
            _terminate_process_tree(process, policy.terminate_grace_s)
            ended = time.monotonic()
            return SupervisedProcessResult(
                status=ProcessStatus.HARD_TIMEOUT,
                returncode=process.returncode,
                pid=process.pid,
                duration_s=ended - started,
                last_progress_age_s=max(0.0, ended - last_progress_at),
                last_progress_kind=last_progress_kind,
                stdout_tail=tuple(stdout_tail),
                stderr_tail=tuple(stderr_tail),
            )

        if now - last_progress_at >= policy.stall_timeout_s:
            _terminate_process_tree(process, policy.terminate_grace_s)
            ended = time.monotonic()
            return SupervisedProcessResult(
                status=ProcessStatus.STALL_TIMEOUT,
                returncode=process.returncode,
                pid=process.pid,
                duration_s=ended - started,
                last_progress_age_s=max(0.0, ended - last_progress_at),
                last_progress_kind=last_progress_kind,
                stdout_tail=tuple(stdout_tail),
                stderr_tail=tuple(stderr_tail),
            )

        time.sleep(policy.poll_interval_s)
