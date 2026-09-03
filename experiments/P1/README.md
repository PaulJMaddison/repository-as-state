# P1 — corrected Repository-as-State causal study

Status: **SEARCHFORCARS CHAIN AND P1 TASK CONTRACTS ESTABLISHED; PRIVATE P1 VERIFIERS NOT YET FROZEN.**

P1 is a new experiment version created after the completed Subject-B P0 pilot
exposed material methodology/runtime confounds.

P1 does not overwrite, repair or rerun P0. P0 remains immutable historical
evidence.

## Why P1 exists

P0 established that the experimental apparatus could execute a six-run matched
session-history comparison, but post-experiment forensics found:

1. detached-HEAD repository-safety contamination in fresh-condition runs;
2. incomplete task-spec/governing-verifier alignment;
3. missing deterministic offline build/toolchain capability.

Those defects have now been remediated for future experiments.

## Required P1 foundations

P1 may not begin until all of the following are frozen:

- the already-established WP04/WP05/WP06 SearchForCars historical chain;
- exact accepted PRE states;
- neutral task specifications;
- complete governing task-spec-to-verifier behaviour mappings;
- hidden implementation-independent behavioural verifiers;
- runtime-v3 lock/reference;
- exact model/configuration;
- session-continuity design;
- prompt bytes;
- execution order;
- timeout/retry policy;
- metrics contract;
- public-safe preregistration commitment.

## Central P1 task-contract rule

> **A verifier may be hidden. A requirement may not be hidden.**

See:

- `task-contract-protocol.md`
- `protocol-v1.md`

No governing behavioural verifier check may remain
`NOT_REASONABLY_DERIVABLE_FROM_TASK_SPEC`.

## Current status

The shared task-contract evaluator has been independently validated and merged.

Runtime-v3 remediation is green.

No P1 task-solving model has run.

Current next step:

`BUILD_AND_FREEZE_PRIVATE_P1_VERIFIERS`.

All three corrected task contracts are now eligible and frozen by private hash.
The next step is private verifier implementation and PRE/POST/negative-control
qualification against those frozen contracts before P1 execution.
