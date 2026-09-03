import pytest

from ras.runtime_readiness import (
    RuntimeIsolationEvidence,
    evaluate_runtime_readiness,
)


def complete_evidence(**overrides):
    values = dict(
        final_lock_integrity_valid=True,
        model_selection_explicit=True,
        runtime_configuration_frozen=True,
        session_semantics_frozen=True,
        filesystem_isolation_enforced=True,
        agent_tool_network_denied=True,
        provider_transport_separated=True,
        cross_session_memory_auditable=True,
        workspace_materialisation_ready=True,
        leak_gate_ready=True,
        leak_gate_clean_control_pass=True,
        leak_gate_negative_control_detected=True,
        execution_order_frozen=True,
        retry_policy_frozen=True,
        timeout_policy_frozen=True,
        metrics_collection_frozen=True,
        experimental_agent_runs=0,
        p0_executed=False,
    )
    values.update(overrides)
    return RuntimeIsolationEvidence(**values)


def test_complete_evidence_is_ready():
    result = evaluate_runtime_readiness(complete_evidence())
    assert result.ready
    assert result.action == "READY_TO_EXECUTE_P0"
    assert result.failures == ()


@pytest.mark.parametrize(
    ("field", "failure"),
    [
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
        (
            "leak_gate_negative_control_detected",
            "leak_gate_negative_control_not_detected",
        ),
        ("execution_order_frozen", "execution_order_not_frozen"),
        ("retry_policy_frozen", "retry_policy_not_frozen"),
        ("timeout_policy_frozen", "timeout_policy_not_frozen"),
        ("metrics_collection_frozen", "metrics_collection_not_frozen"),
    ],
)
def test_each_required_control_fails_closed(field, failure):
    result = evaluate_runtime_readiness(complete_evidence(**{field: False}))
    assert not result.ready
    assert result.action == "STOP_BEFORE_P0"
    assert failure in result.failures


def test_multiple_failures_are_deterministically_sorted():
    result = evaluate_runtime_readiness(
        complete_evidence(
            filesystem_isolation_enforced=False,
            agent_tool_network_denied=False,
            timeout_policy_frozen=False,
        )
    )
    assert result.failures == tuple(sorted(result.failures))
    assert result.failures == (
        "agent_tool_network_not_denied",
        "filesystem_isolation_not_enforced",
        "timeout_policy_not_frozen",
    )


def test_existing_experimental_run_blocks_readiness():
    result = evaluate_runtime_readiness(
        complete_evidence(experimental_agent_runs=1)
    )
    assert result.failures == ("experimental_agent_run_already_recorded",)


def test_existing_p0_execution_blocks_readiness():
    result = evaluate_runtime_readiness(complete_evidence(p0_executed=True))
    assert result.failures == ("p0_already_executed",)


def test_negative_experimental_run_count_is_invalid():
    with pytest.raises(ValueError):
        complete_evidence(experimental_agent_runs=-1)


def test_result_dict_is_machine_readable():
    result = evaluate_runtime_readiness(
        complete_evidence(network_isolation_enforced=False)
    ) if False else evaluate_runtime_readiness(
        complete_evidence(agent_tool_network_denied=False)
    )
    payload = result.as_dict()
    assert payload["ready"] is False
    assert payload["action"] == "STOP_BEFORE_P0"
    assert payload["evidence"]["agent_tool_network_denied"] is False
