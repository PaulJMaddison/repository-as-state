from ras.task_contract import (
    DerivationClass,
    RequirementMapping,
    evaluate_task_contract,
)


def row(behaviour, derivation=DerivationClass.EXPLICITLY_REQUIRED_BY_TASK_SPEC):
    return RequirementMapping(
        task_statement_id=f"statement-{behaviour}",
        verifier_behaviour_id=behaviour,
        derivation_class=derivation,
        implementation_independent=True,
        observable_behaviour=True,
    )


def test_complete_explicit_contract_is_eligible():
    result = evaluate_task_contract(["b1", "b2"], [row("b1"), row("b2")])
    assert result.eligible
    assert result.action == "ELIGIBLE_FOR_PREREGISTRATION"
    assert result.failures == ()


def test_reasonably_entailed_requirement_is_eligible():
    result = evaluate_task_contract(
        ["b1"],
        [row("b1", DerivationClass.REASONABLY_ENTAILED_BY_TASK_SPEC)],
    )
    assert result.eligible


def test_unmapped_governing_behaviour_fails_closed():
    result = evaluate_task_contract(["b1", "b2"], [row("b1")])
    assert not result.eligible
    assert "governing_behaviour_unmapped" in result.failures


def test_hidden_requirement_fails_closed():
    result = evaluate_task_contract(
        ["b1"],
        [row("b1", DerivationClass.NOT_REASONABLY_DERIVABLE_FROM_TASK_SPEC)],
    )
    assert not result.eligible
    assert "hidden_or_under_specified_requirement" in result.failures


def test_implementation_specific_acceptance_fails():
    mapping = RequirementMapping(
        task_statement_id="s1",
        verifier_behaviour_id="b1",
        derivation_class=DerivationClass.EXPLICITLY_REQUIRED_BY_TASK_SPEC,
        implementation_independent=False,
        observable_behaviour=True,
    )
    result = evaluate_task_contract(["b1"], [mapping])
    assert "implementation_specific_acceptance" in result.failures


def test_non_observable_acceptance_fails():
    mapping = RequirementMapping(
        task_statement_id="s1",
        verifier_behaviour_id="b1",
        derivation_class=DerivationClass.EXPLICITLY_REQUIRED_BY_TASK_SPEC,
        implementation_independent=True,
        observable_behaviour=False,
    )
    result = evaluate_task_contract(["b1"], [mapping])
    assert "non_observable_acceptance" in result.failures


def test_duplicate_mapping_fails():
    result = evaluate_task_contract(["b1"], [row("b1"), row("b1")])
    assert "duplicate_mapping_for_governing_behaviour" in result.failures


def test_mapping_to_non_governing_behaviour_fails():
    result = evaluate_task_contract(["b1"], [row("b1"), row("b2")])
    assert "mapping_references_non_governing_behaviour" in result.failures


def test_empty_contract_fails():
    result = evaluate_task_contract([], [])
    assert "no_governing_behaviours" in result.failures
