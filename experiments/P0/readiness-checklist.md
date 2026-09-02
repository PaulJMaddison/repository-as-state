# P0 readiness checklist

**Current status: NOT READY TO EXECUTE.**

This is a hard gate.

## Corpus — complete

- [x] Bounded candidate programme fixed before task selection.
- [x] Inclusion criteria frozen.
- [x] Exclusion criteria frozen.
- [x] Complete private considered-candidate record frozen.
- [x] Genuine sequential-dependence rule applied.
- [ ] Five task units selected without cherry-picking later candidates; prior selection superseded by amendment 001.
- [x] Neutral task specifications canonicalised and hashed.
- [x] Private corpus lock payload canonicalised and committed publicly by SHA-256 only.
- [x] Historical survivor/author-subject bias explicitly documented.

## Accepted boundaries — complete with frozen limitation

- [ ] Five committed coherent accepted post-states identified; original T3 boundary rejected.
- [x] Deterministic local behavioural test/proof contracts identified for every selected task.
- [x] No selected implementation surface contains unfinished TODO/FIXME/unimplemented markers observed by curation.
- [x] Historical acceptance evidence distinguished from current reproduction evidence.
- [x] Missing exact per-boundary CI/current historical rerun recorded as a limitation.

## Isolation harness — implemented and synthetically validated

- [x] Fresh independent Git workspace materialiser implemented.
- [x] No-remotes check.
- [x] Forbidden future OID non-resolution check.
- [x] Allowed-refs-only check.
- [x] Reflog closure check.
- [x] Unreachable-extra-object check.
- [x] Git alternates check.
- [x] Linked-worktree/source-link check.
- [x] Sidecar patch/bundle/archive check.
- [x] Symlink escape check.
- [x] Clean workspace check.
- [ ] Network-isolation assertion required; technical isolation is not yet proven.
- [x] Fail-closed behaviour tested.
- [x] Synthetic tests labelled non-research evidence.

## Task leakage — curation complete; execution proof pending

- [x] Private selected pre-states reviewed for legitimate durable state versus future-solution information.
- [x] Private leakage notes frozen in the lock payload.
- [ ] Re-run leakage checks on each finally materialised private execution workspace.

## Hidden verifier — superseded implementation exists; final amended set pending

- [x] Generic public contract frozen.
- [x] Task-specific behavioural requirements frozen privately.
- [x] Patch similarity rejected as success criterion.
- [x] Equivalent correct implementations required.
- [x] Superseded-corpus private verifier source built outside both public repo and subject workspace.
- [ ] Final verifier versions/hashes frozen after implementation.
- [ ] Verifier builder validates deterministic local/offline execution.

## Reconstruction probe — schema frozen

- [x] Reportable state schema frozen.
- [x] No chain-of-thought requested.
- [x] Probe remains outside subject workspace.
- [x] Probe is not available to later tasks.
- [ ] Final task-specific objective scoring keys built with the private verifier package.

## Model/runtime — BLOCKING

- [ ] Exact visible high-capability model/configuration frozen.
- [ ] Stable system instructions hashed.
- [ ] Tool schema/permissions frozen.
- [ ] Executor/runtime implementation frozen.
- [ ] Base toolchain/dependency image frozen.
- [ ] CPU/memory policy frozen where controllable.
- [ ] Cache policy frozen.
- [ ] Network policy enforced and frozen.
- [ ] Account/cross-session memory disabled or auditable.
- [ ] `P0_CAUSAL_RUNTIME_ELIGIBLE` resolved true.
- [ ] Telemetry capability frozen.
- [ ] Per-task wall-clock/model-call/token budgets frozen.

## Run control — logic frozen; numeric runtime limits pending

- [x] Failure taxonomy frozen.
- [x] No-human-rescue rule frozen.
- [x] Selective reruns prohibited.
- [x] Rerun eligibility restricted to objective infrastructure categories.
- [ ] Exact timeout/stopping/resource limits frozen after runtime selection.

## Preregistration

- [x] Corpus-selected preregistration document created.
- [x] Allowed P0 interpretation categories frozen.
- [x] P0 explicitly labelled methodology pilot.
- [x] No inferential non-inferiority claim planned from five tasks.
- [x] RRI/RTF kept descriptive.
- [ ] Final model/runtime fields populated.
- [ ] Final preregistration SHA generated.
- [ ] Condition order derived from final preregistration lock.
- [ ] `PREREGISTRATION_LOCK.json` created before outcomes.

If any mandatory runtime, leakage, verifier, or treatment-isolation item remains unresolved: **DO NOT RUN P0.**
