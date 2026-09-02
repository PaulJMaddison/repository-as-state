# P0 corpus curation report

**PUBLIC SAFE REPORT — NO PRIVATE SUBJECT IDENTIFIERS OR COMMITS**

## Status

- corpus selected: **no — superseded during boundary validation**;
- P0 executed: **no**;
- experimental agent runs: **0**;
- model/runtime freeze pending: **yes**;
- final preregistration frozen: **no**.

## Candidate-window methodology

A bounded contiguous local engineering programme was fixed before individual task selection. The window was selected for methodological neutrality: one coherent local programme with deterministic behavioural surfaces, excluding cloud/model/live-service work by programme scope rather than by expected RaS outcome.

- candidate transitions considered: **38**;
- amended selected task units: **0 final units**;
- transitions contained in final amended units: **0**;
- excluded later transitions: **21**.

Exclusion of the remaining transitions followed the fixed five-task pilot budget; later tasks were not substituted based on perceived difficulty or expected reset performance.

## Superseded public task structure

- `P0-T1`: runtime-governance, medium, chain root;
- `P0-T2`: temporal-governance, high, depends on T1;
- `P0-T3`: identity-lifecycle, high, depends on T1/T2;
- `P0-T4`: governed-fact-state, high, depends on T1/T2;
- `P0-T5`: durable-governed-ingress, high, depends on T3/T4.

This original graph is superseded by amendment 001. `P0-T3` is recorded as
`EXCLUDED_INVALID_ACCEPTED_BOUNDARY_DISCOVERED_DURING_PREPARATION`; no amended
five-task graph is selected.

## Accepted boundaries

The original five-boundary claim is withdrawn. No final amended boundary is
accepted because the mandatory replacement pre-fail/post-pass chain was not
completed.

Limitation: exact historical CI/check records are not attached to the five boundary commits, and current private-source historical build reproduction was not possible in the connector-only curator runtime. This is frozen as a limitation, not upgraded into evidence.

## External dependency exclusion

Every selected task is designed for deterministic local Rust verification. Cloud-only, live-model, credential-dependent, live-service, and network-dependent tasks are excluded from P0.

## Public commitments

Selection rule:

`0d05613e86be9dd3bc9c133104b750ac71dc19377c6dee5cc9d4e0007449d6e0`

Public corpus manifest canonical digest:

`fc03bd010e47d035218021d65fce6b84622df6968b86aa83e3a6e62df9bd8f2d`

Current corpus-selected preregistration canonical digest (not a final freeze hash):

`ef3a29aba53b44ea7d8ee134b448cd37a71a17738bc5e7b1c240f7c5b3eb09f0`

Private P0 lock:

`75d4a60d0d650c7899c6ec25cb74931b9590785c2ed45eae1bedf82d048c5609`

## Harness status

FUTURE_HISTORY_LEAK_GATE v0.1.0 is implemented generically.

Synthetic validation: **21 leak/isolation tests passed**. Full public research-tool suite: **49 passed / 1 environment-skipped** (Windows symlink privilege).

**HARNESS TEST DATA — NOT RESEARCH EVIDENCE.**

## Verifier and ablation status

Task-specific hidden-verifier behavioural requirements are frozen in the private lock payload. Superseded-corpus verifier implementations were built privately; no final amended verifier set was frozen because the amended corpus is insufficient.

Condition C is not enabled:

`C_NOT_RUN_REASON=NO_DEFENSIBLE_ABLATION`

## Preregistration status

The corpus and methodological rules are prepared, but model/runtime identity, resource limits, telemetry, cache/network policy, and cross-session-memory control are unresolved.

Therefore:

`P0_PREREGISTRATION_FROZEN=false`

`P0_CORPUS_INSUFFICIENT_AFTER_BOUNDARY_VALIDATION=true`
`P0_PROTOCOL_READY_FOR_MODEL_FREEZE=false`
`NETWORK_ISOLATION_READY=false`

No empirical RaS result exists.
