import pytest

from ras.preregistration import preregistration_digest, validate_public_preregistration


def valid_doc():
    return {
        "experiment": {"id": "P0"},
        "research_question": {"primary": "x"},
        "audit_base_sha": "public-sha",
        "subject": {"identifier": "PRIVATE_SUBJECT_A"},
        "corpus": {
            "task_count": 2,
            "task_spec_sha256": {"P0-T1": "a", "P0-T2": "b"},
        },
        "conditions": {"D": {"enabled_for_p0": False}},
        "endpoints": {},
        "leakage": {},
        "workspace": {},
        "run_control": {},
        "interpretation": {},
        "falsification": {},
        "public_private_boundary": {},
        "model_runtime": {},
        "results": {
            "experimental_agent_runs": 0,
            "positive_empirical_ras_results": False,
        },
    }


def test_valid_preregistration_is_accepted_and_hash_is_repeatable():
    value = valid_doc()
    assert validate_public_preregistration(value) == ()
    assert preregistration_digest(value) == preregistration_digest(dict(reversed(list(value.items()))))


def test_missing_required_top_level_is_rejected():
    value = valid_doc()
    value.pop("leakage")
    assert any(x.startswith("missing_top_level:") for x in validate_public_preregistration(value))


@pytest.mark.parametrize(
    "mutation,expected",
    [
        (lambda d: d["experiment"].update(id="P1"), "experiment_id_must_be_P0"),
        (lambda d: d["subject"].update(identifier="PRIVATE_REPO_NAME"), "public_subject_must_be_pseudonymous"),
        (lambda d: d["results"].update(experimental_agent_runs=1), "experimental_agent_runs_must_be_zero_before_P0"),
        (lambda d: d["results"].update(positive_empirical_ras_results=True), "positive_empirical_ras_results_must_be_false_before_P0"),
        (lambda d: d["conditions"]["D"].update(enabled_for_p0=True), "tiered_execution_must_be_disabled_for_primary_P0"),
    ],
)
def test_invalid_preregistration_state_is_rejected(mutation, expected):
    value = valid_doc()
    mutation(value)
    assert expected in validate_public_preregistration(value)


def test_task_hash_count_mismatch_is_rejected():
    value = valid_doc()
    value["corpus"]["task_count"] = 3
    assert "task_hash_count_mismatch" in validate_public_preregistration(value)


def test_digest_refuses_invalid_document():
    value = valid_doc()
    value["results"]["experimental_agent_runs"] = 1
    with pytest.raises(ValueError):
        preregistration_digest(value)
