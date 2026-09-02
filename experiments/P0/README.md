# P0 — Forced-State-Reset Methodology Pilot

**Status: CORPUS SELECTED; PROTOCOL PREPARED; MODEL/RUNTIME FREEZE PENDING.**  
**P0 executed: NO.**  
**Experimental agent runs: 0.**

P0 tests one narrow causal question:

> After a validated accepted engineering transition, how much continuity is lost when predecessor high-capability reasoning-session state is destroyed?

## Corpus status

A privileged curator inspected a private historical software repository under a strict public/private boundary.

Public subject identifier: **PRIVATE_SUBJECT_A**

The candidate window was frozen before individual task selection. It contained 38 historical transitions. Applying the preregistered selection rule produced five pseudonymous, genuinely sequential task units comprising 17 transitions; 21 later transitions were excluded by the fixed five-task pilot budget rule.

The public corpus manifest contains only pseudonymous IDs, broad categories, hashes, dependency structure, and acceptance status. Exact private repository identity, commits, paths, task text, historical solutions, verifier details, and curation notes are committed only by cryptographic hash.

## Conditions

**A — PERSISTENT_HISTORY_CONTROL**

At every accepted boundary the workspace is destroyed and canonically rematerialised. Predecessor reasoning-session history is retained.

**B — FORCED_RESET_RAS**

At the same accepted boundary the workspace is identically destroyed/rematerialised and the reasoning session is destroyed. The fresh session receives stable experiment instructions, the exact same neutral task bytes, the same accepted repository state, and the same permitted tools/environment.

The intended treatment difference is predecessor reasoning-session history.

**C — SEMANTIC_STATE_ABLATION**

Not enabled for P0.

`C_NOT_RUN_REASON=NO_DEFENSIBLE_ABLATION`

**D — TIERED_EXECUTION**

Not part of primary P0. Deferred.

## Current blockers before execution

P0 remains **NOT RUN-READY** until the exact model/runtime is frozen, including:

- visible model/configuration;
- stable system instructions;
- tool surface and permissions;
- per-task resource limits;
- telemetry availability;
- account/cross-session memory control;
- cache policy;
- network policy.

The private hidden verifier implementation and isolated task workspaces also remain to be prepared outside both this public repository and the subject workspace.

## Harness status

The generic FUTURE_HISTORY_LEAK_GATE and canonicalisation/preregistration helpers are implemented in `src/ras/`.

Current deterministic synthetic harness validation: **49 passed / 1 environment-skipped** (Windows symlink privilege), including **21 Git isolation/leakage tests**.

**HARNESS TEST DATA — NOT RESEARCH EVIDENCE.**

## Freeze status

`MODEL_RUNTIME_FREEZE_PENDING=true`  
`P0_PREREGISTRATION_FROZEN=false`  
`P0_CORPUS_INSUFFICIENT_AFTER_BOUNDARY_VALIDATION=true`
`P0_PROTOCOL_READY_FOR_MODEL_FREEZE=false`
`NETWORK_ISOLATION_READY=false`

No `PREREGISTRATION_LOCK.json` is created yet because unresolved runtime fields are causal requirements, not optional metadata.

## Curator separation

The curator who selected this corpus has seen future history and is permanently disqualified from acting as Condition A, B, C, execution worker, or result judge.
## Fixed cross-condition state progression

To preserve causal identifiability, P0 does **not** let A and B produce different repository states for the next task. For each task, both conditions receive independently materialised copies of the same frozen historical accepted pre-state. Experimental outputs are adjudicated and recorded, but the next task advances to the next frozen historical accepted boundary.

This preserves byte-identical repository state across A/B. It also creates a declared limitation: Condition A may retain reasoning about a materially equivalent prior implementation that differs from the next frozen historical boundary. Stable runtime instructions must state that the rematerialised repository is authoritative.

