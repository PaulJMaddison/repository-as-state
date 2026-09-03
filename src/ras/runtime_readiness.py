"""Fail-closed readiness evaluation for isolated P0 runtimes.

HARNESS CODE ONLY. A READY result means the declared runtime controls satisfy
the frozen pre-experiment gate; it is not evidence that Repository-as-State
works.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class RuntimeIsolationEvidence:
    final_lock_integrity_valid: bool
    model_selection_explicit: bool
    runtime_configuration_frozen: bool
    session_semantics_frozen: bool
    filesystem_isolation_enforced: bool
    agent_tool_network_denied: bool
    provider_transport_separated: bool
    cross_session_memory_auditable: bool
    workspace_materialisation_ready: bool
    leak_gate_ready: bool
    leak_gate_clean_control_pass: bool
    leak_gate_negative_control_detected: bool
    execution_order_frozen: bool
    retry_policy_frozen: bool
    timeout_policy_frozen: bool
    metrics_collection_frozen: bool
    experimental_agent_runs: int = 0
    p0_executed: bool = False

    def __post_init__(self) -> None:
        if self.experimental_agent_runs < 0:
            raise ValueError("experimental_agent_runs must be non-negative")


@dataclass(frozen=True)
class RuntimeReadinessResult:
    ready: bool
    action: str
    failures: tuple[str, ...]
    evidence: RuntimeIsolationEvidence

    def as_dict(self) -> dict[str, object]:
        result = asdict(self)
        result["evidence"] = asdict(self.evidence)
        return result


_REQUIRED_TRUE_FIELDS: tuple[tuple[str, str], ...] = (
    ("final_lock_integrity_valid", "final_lock_integrity_invalid"),
    ("model_selection_explicit", "model_selection_not_explicit"),
    ("runtime_configuration_frozen", "runtime_configuration_not_frozen"),
    ("session_semantics_frozen", "session_semantics_not_frozen"),
    ("filesystem_isolation_enforced", "filesystem_isolation_not_enforced"),
    ("agent_tool_network_denied", "agent_tool_network_not_denied"),
    ("provider_transport_separated", "provider_transport_not_separated"),
    ("cross_session_memory_auditable", "cross_session_memory_not_auditable"),
    ("workspace_materialisation_ready", "workspace_materialisation_not_ready"),
    ("leak_gate_ready", "leak_gate_not_ready"),
    ("leak_gate_clean_control_pass", "leak_gate_clean_control_failed"),
    ("leak_gate_negative_control_detected", "leak_gate_negative_control_not_detected"),
    ("execution_order_frozen", "execution_order_not_frozen"),
    ("retry_policy_frozen", "retry_policy_not_frozen"),
    ("timeout_policy_frozen", "timeout_policy_not_frozen"),
    ("metrics_collection_frozen", "metrics_collection_not_frozen"),
)


def evaluate_runtime_readiness(
    evidence: RuntimeIsolationEvidence,
) -> RuntimeReadinessResult:
    """Evaluate the frozen runtime gate without performing any experiment.

    The gate is deliberately conjunctive and fail-closed. Missing one required
    control blocks model invocation for P0.
    """

    failures: list[str] = [
        failure
        for field, failure in _REQUIRED_TRUE_FIELDS
        if not getattr(evidence, field)
    ]

    if evidence.experimental_agent_runs != 0:
        failures.append("experimental_agent_run_already_recorded")
    if evidence.p0_executed:
        failures.append("p0_already_executed")

    unique_failures = tuple(sorted(set(failures)))
    ready = not unique_failures
    return RuntimeReadinessResult(
        ready=ready,
        action="READY_TO_EXECUTE_P0" if ready else "STOP_BEFORE_P0",
        failures=unique_failures,
        evidence=evidence,
    )
