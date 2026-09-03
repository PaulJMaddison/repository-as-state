# P1 — corrected Repository-as-State causal study

Status: **SEARCHFORCARS CHAIN AND P1 TASK CONTRACTS ESTABLISHED; PRIVATE P1 VERIFIER REMEDIATION IN PROGRESS.**

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

The candidate private P1 verifiers now reproduce the required historical
PRE-fail / POST-pass separation and are deterministic across the required
three-run control matrix. Hidden-material ACLs have also been corrected.

They are **not yet qualified for freeze** because implementation-specific test
method-name selection remains, per-behaviour negative controls have not yet been
implemented, implementation-independence evidence is only partial, and oracle
self-tests are incomplete.

No P1 task-solving model has run.

Current next step:

`REMEDIATE_PRIVATE_P1_VERIFIER_IMPLEMENTATION`.

The frozen task contracts must not change. The remaining work is only to make
the private oracles direct, semantic, implementation-independent and robust
before final verifier-package freeze and P1 preregistration.
