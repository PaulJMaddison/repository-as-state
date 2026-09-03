"""Fail-closed task-spec/verifier contract checks for future RaS experiments.

This module does not select tasks or inspect hidden verifier source. It validates
that every governing behavioural requirement is represented in the frozen task
contract before any model invocation.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from enum import Enum
from typing import Iterable


class DerivationClass(str, Enum):
    EXPLICITLY_REQUIRED_BY_TASK_SPEC = "EXPLICITLY_REQUIRED_BY_TASK_SPEC"
    REASONABLY_ENTAILED_BY_TASK_SPEC = "REASONABLY_ENTAILED_BY_TASK_SPEC"
    NOT_REASONABLY_DERIVABLE_FROM_TASK_SPEC = "NOT_REASONABLY_DERIVABLE_FROM_TASK_SPEC"


@dataclass(frozen=True)
class RequirementMapping:
    task_statement_id: str
    verifier_behaviour_id: str
    derivation_class: DerivationClass
    implementation_independent: bool
    observable_behaviour: bool


@dataclass(frozen=True)
class TaskContractResult:
    eligible: bool
    action: str
    failures: tuple[str, ...]
    governing_behaviour_count: int
    mapped_behaviour_count: int

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def evaluate_task_contract(
    governing_behaviour_ids: Iterable[str],
    mappings: Iterable[RequirementMapping],
) -> TaskContractResult:
    """Return a fail-closed eligibility result for one frozen task contract."""

    failures: list[str] = []
    governing = tuple(governing_behaviour_ids)
    mapping_rows = tuple(mappings)

    if not governing:
        failures.append("no_governing_behaviours")

    if any(not isinstance(x, str) or not x.strip() for x in governing):
        failures.append("invalid_governing_behaviour_id")

    if len(set(governing)) != len(governing):
        failures.append("duplicate_governing_behaviour_id")

    behaviour_ids = [m.verifier_behaviour_id for m in mapping_rows]
    task_statement_ids = [m.task_statement_id for m in mapping_rows]

    if any(not x.strip() for x in behaviour_ids):
        failures.append("invalid_mapping_behaviour_id")
    if any(not x.strip() for x in task_statement_ids):
        failures.append("invalid_task_statement_id")
    if len(set(behaviour_ids)) != len(behaviour_ids):
        failures.append("duplicate_mapping_for_governing_behaviour")

    governing_set = set(governing)
    mapped_set = set(behaviour_ids)

    missing = governing_set - mapped_set
    extra = mapped_set - governing_set
    if missing:
        failures.append("governing_behaviour_unmapped")
    if extra:
        failures.append("mapping_references_non_governing_behaviour")

    if any(
        m.derivation_class is DerivationClass.NOT_REASONABLY_DERIVABLE_FROM_TASK_SPEC
        for m in mapping_rows
    ):
        failures.append("hidden_or_under_specified_requirement")

    if any(not m.implementation_independent for m in mapping_rows):
        failures.append("implementation_specific_acceptance")

    if any(not m.observable_behaviour for m in mapping_rows):
        failures.append("non_observable_acceptance")

    unique_failures = tuple(sorted(set(failures)))
    eligible = not unique_failures

    return TaskContractResult(
        eligible=eligible,
        action="ELIGIBLE_FOR_PREREGISTRATION" if eligible else "REJECT_TASK_BEFORE_PREREGISTRATION",
        failures=unique_failures,
        governing_behaviour_count=len(governing_set),
        mapped_behaviour_count=len(mapped_set & governing_set),
    )
