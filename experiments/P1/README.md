# P1 — corrected Repository-as-State causal study

Status: **SEARCHFORCARS CHAIN AND P1 TASK CONTRACTS ESTABLISHED; WP04 PRIVATE VERIFIER QUALIFIED AND FROZEN; WP05/WP06 REMEDIATION PENDING.**

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

All three corrected task contracts are eligible and frozen by private hash.

WP04_PR5 is now qualified with a direct semantic private verifier. Its eight
governing behaviours are covered by semantic oracles, all eight targeted
behavioural negative controls are detected, all eight semantics-preserving
alternate implementations pass the unchanged verifier, oracle self-tests pass,
implementation-specific selector/source/diff/commit checks are absent, and the
historical PRE/POST controls remain deterministic FAIL/PASS across three clean
runs.

The WP04 private verifier package is frozen at:

`F61BEFEE8262FEE42D26DB3AC833E1BE8DB29E5555073CDCA30ABBE6DD996057`

WP05_PR6 and WP06_PR7 are not yet qualified for freeze. Their established
historical PRE/POST evidence remains valid, but their private verifiers still
require the same semantic-oracle, per-behaviour negative-control,
implementation-independence and oracle-self-test remediation completed for
WP04.

No P1 task-solving model has run. P0 has not been rerun.

Current next step:

`IMPLEMENT_SEMANTIC_PRIVATE_P1_ORACLES_AND_QUALIFY_WP05`.

The frozen task contracts must not change. Complete and freeze WP05 as one
work package before moving to WP06. Only after all three task verifiers are
qualified and frozen should the overall private verifier package be frozen and
the corrected P1 protocol be preregistered for execution.
