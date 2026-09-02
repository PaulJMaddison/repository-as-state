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

`c5d2c4d4346152b58ae85513997a404eea08896e6a1af02ce33ab8f9315b49be`

Public corpus manifest canonical digest:

`05b10fc6ddad29e962eaa0ca7e7551c6c9dc6e57eb09918917d5a64a28f21b8c`

Current corpus-selected preregistration canonical digest (not a final freeze hash):

`15d1fbfd88e5fe4e56bf1b2a26f5be5ac2a4069e0bf5bca23f19ed063147392f`

Private P0 lock:

`f18860982a56fb639399ff5c004d681e65d49c91d563dd05296ea27917e2fd0e`

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
