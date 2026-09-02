# P0 corpus curation report

**PUBLIC SAFE REPORT — NO PRIVATE SUBJECT IDENTIFIERS OR COMMITS**

## Status

- corpus selected: **yes**;
- P0 executed: **no**;
- experimental agent runs: **0**;
- model/runtime freeze pending: **yes**;
- final preregistration frozen: **no**.

## Candidate-window methodology

A bounded contiguous local engineering programme was fixed before individual task selection. The window was selected for methodological neutrality: one coherent local programme with deterministic behavioural surfaces, excluding cloud/model/live-service work by programme scope rather than by expected RaS outcome.

- candidate transitions considered: **38**;
- selected task units: **5**;
- transitions contained in selected units: **17**;
- excluded later transitions: **21**.

Exclusion of the remaining transitions followed the fixed five-task pilot budget; later tasks were not substituted based on perceived difficulty or expected reset performance.

## Selected public task structure

- `P0-T1`: runtime-governance, medium, chain root;
- `P0-T2`: temporal-governance, high, depends on T1;
- `P0-T3`: identity-lifecycle, high, depends on T1/T2;
- `P0-T4`: governed-fact-state, high, depends on T1/T2;
- `P0-T5`: durable-governed-ingress, high, depends on T3/T4.

The graph is genuinely sequential and connected.

## Accepted boundaries

All five post-states satisfy the curation definition of credible accepted engineering boundaries through committed coherent state plus deterministic behavioural test/proof contracts.

Limitation: exact historical CI/check records are not attached to the five boundary commits, and current private-source historical build reproduction was not possible in the connector-only curator runtime. This is frozen as a limitation, not upgraded into evidence.

## External dependency exclusion

Every selected task is designed for deterministic local Rust verification. Cloud-only, live-model, credential-dependent, live-service, and network-dependent tasks are excluded from P0.

## Public commitments

Selection rule:

`0afd708810437c474261e294d8353865a7d0f522434452f648d618c761a54c1e`

Public corpus manifest canonical digest:

`a5dad058ce528576f549b9d641f3f57687888fe9d8455742eec3a5bcf868d0de`

Current corpus-selected preregistration remains mutable pending the required model/runtime freeze; no final preregistration hash is claimed yet.

Private P0 lock:

`ad0d5abdcd98d4cc73a02b085553ca1bcfa4831ba46c42ea9e77cf3b14d575b2`

## Harness status

FUTURE_HISTORY_LEAK_GATE v0.1.0 is implemented generically.

Synthetic validation: **21 leak/isolation tests passed**. Full public research-tool suite: **50 tests passed**.

**HARNESS TEST DATA — NOT RESEARCH EVIDENCE.**

## Verifier and ablation status

Task-specific hidden-verifier behavioural requirements are frozen in the private lock payload; verifier implementation is not yet built.

Condition C is not enabled:

`C_NOT_RUN_REASON=NO_DEFENSIBLE_ABLATION`

## Preregistration status

The corpus and methodological rules are prepared, but model/runtime identity, resource limits, telemetry, cache/network policy, and cross-session-memory control are unresolved.

Therefore:

`P0_PREREGISTRATION_FROZEN=false`

`P0_PROTOCOL_READY_FOR_MODEL_FREEZE=true`

No empirical RaS result exists.
