# P1 — corrected Repository-as-State causal study

Status: **SEARCHFORCARS CHAIN AND P1 TASK CONTRACTS ESTABLISHED; WP04 AND WP05 PRIVATE VERIFIERS QUALIFIED AND FROZEN; WP06 PENDING.**

P1 is a new experiment version created after the completed Subject-B P0 pilot exposed material methodology/runtime confounds.

P1 does not overwrite, repair or rerun P0. P0 remains immutable historical evidence.

## Required P1 foundations

P1 may not begin until the historical chain, exact PRE states, neutral task specifications, complete governing behaviour mappings, hidden implementation-independent behavioural verifiers, runtime-v3 lock/reference, exact model/configuration, session-continuity design, prompt bytes, execution order, timeout/retry policy, metrics contract and public-safe preregistration commitment are frozen.

## Central P1 task-contract rule

> **A verifier may be hidden. A requirement may not be hidden.**

No governing behavioural verifier check may remain `NOT_REASONABLY_DERIVABLE_FROM_TASK_SPEC`.

## Current status

The shared task-contract evaluator has been independently validated and merged. Runtime-v3 remediation is green. All three corrected task contracts are eligible and frozen by private hash.

WP04_PR5 is qualified and frozen at `F61BEFEE8262FEE42D26DB3AC833E1BE8DB29E5555073CDCA30ABBE6DD996057`.

WP05_PR6 is also qualified and frozen. Its 10 governing behaviours have direct semantic oracles; 10/10 targeted negative controls are detected; 10/10 semantics-preserving alternate implementations pass; 15 oracle self-test categories pass; implementation-specific selector/source/diff/commit checks are absent; and the historical PRE/POST controls remain deterministic FAIL/PASS across three clean runs.

The WP05 private verifier package is frozen at `5BBE8A480B2453B4EAE6B8AB7769753062E994602CE18F349ABB5B70E8329E4D`.

WP06_PR7 remains the only task verifier not yet qualified for freeze.

No P1 task-solving model has run. P0 has not been rerun.

Current next step: `IMPLEMENT_SEMANTIC_PRIVATE_P1_ORACLES_AND_QUALIFY_WP06`.

The frozen task contracts must not change. Complete and freeze WP06 as its own work package. Only after WP06 is qualified and frozen should the overall private P1 verifier package be frozen and the corrected P1 protocol preregistered for execution.
