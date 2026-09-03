# P1 task-contract protocol

Status: **PUBLIC METHODOLOGY REMEDIATION FOR A FUTURE EXPERIMENT.**

This does not amend or repair Subject-B P0. P0 remains immutable.

## Problem exposed by P0

A hidden verifier may stay hidden. A hidden requirement may not.

Before any future causal experiment, every governing behavioural check must be
mapped to the neutral task specification shown to both conditions.

The contract unit is:

`task-spec statement -> governing verifier behaviour -> derivation class`

Allowed derivation classes:

- `EXPLICITLY_REQUIRED_BY_TASK_SPEC`
- `REASONABLY_ENTAILED_BY_TASK_SPEC`

A task is ineligible if any governing behaviour is:

`NOT_REASONABLY_DERIVABLE_FROM_TASK_SPEC`

## Fail-closed eligibility

The shared `ras.task_contract` evaluator rejects a task before preregistration
when any of the following holds:

- a governing behaviour is unmapped;
- a mapping refers to behaviour outside the governing set;
- the same governing behaviour is mapped more than once;
- a requirement is hidden or under-specified;
- acceptance depends on a specific historical implementation rather than
  observable behaviour;
- a governing check is not observable.

The verifier source may remain private. The requirement matrix itself may be
stored privately before execution and publicly committed by hash.

## Curator rule

Historical POST source may be used to discover candidate requirements, but it
must not be used to smuggle implementation details into acceptance.

A competent independent engineer receiving only the historical PRE repository
and neutral task specification must be able to infer every behaviour that can
make the governing verifier pass or fail.

## Versioning

Any task contract used in a future experiment must be frozen before model
invocation and versioned separately from P0.

No P0 task, prompt, verifier or verdict is changed by this protocol.
