# Falsification criteria — Repository-as-State v0.1

RaS is useful only if evidence can count against it. This document defines the directions of evidence that weaken different parts of the thesis. Numerical margins are deliberately not invented here; any threshold used for P0 or later confirmatory inference must be justified and preregistered before outcomes.

## Claims are separable

A result can support one RaS claim while falsifying another.

- **Continuity claim:** fresh reasoning after accepted transitions can preserve engineering outcomes closely enough relative to a matched persistent-history control.
- **Reconstruction claim:** accepted repository state can be reconstructed with tolerable effort and fidelity.
- **Economic/resource claim:** disposal does not merely move equal or greater work into rediscovery.
- **Semantic-state claim:** identifiable repository artefacts carry marginal continuity value.
- **Tiered-execution claim:** separate lower-cost execution can preserve quality after coordination overhead.
- **Security implication:** separation can be implemented with narrower privilege and measurably lower attack impact.
- **Generalisability claim:** effects survive beyond one private, highly curated repository/model/task family.

Failure of the economic claim does not automatically falsify behavioural resumability. Failure of behavioural continuity is more fundamental.

## Evidence against the core continuity thesis

The continuity thesis is weakened when, under a valid matched A/B protocol:

1. the forced-reset condition has materially lower hidden-verifier task success than the persistent-history control;
2. complete-sequence success collapses with sequential depth in B while A continues;
3. the fresh reasoner repeatedly misses constraints that were available only in predecessor reasoning history;
4. B requires systematic human rescue, prompt adjustment, or task-specific hints to match A;
5. failures persist even when reconstruction tooling is reasonable and the accepted repository state is correctly materialised.

A later confirmatory experiment must define a non-inferiority/equivalence margin before outcomes. P0 is not powered to establish such a result.

## Evidence against the reconstruction/state-economics thesis

The economic thesis is weakened when:

1. reconstruction input tokens, file reads, searches, model calls, or elapsed time dominate the forced-reset workload;
2. total outcome-normalised resource use in B is no better than, or worse than, A after counting retries and failed tasks;
3. predecessor history is cheaper to retain/compact/retrieve than repository state is to rediscover;
4. Reconstruction Token Fraction remains high or grows strongly with repository size/depth;
5. bounded or slowly growing reconstruction fails on larger or cross-cutting tasks;
6. comparable success requires specially curated state documents whose maintenance/retrieval burden grows similarly to the history they replace.

The experiment must be allowed to conclude: **“RaS is behaviourally resumable but economically worse because reconstruction dominates.”**

## Evidence against repository-state sufficiency for a task class

Evidence against repository-state sufficiency includes:

- hidden behavioural constraints repeatedly absent from allowed cutoff state;
- state-reconstruction probes systematically omit required architecture/constraints despite exhaustive reasonable exploration;
- success depends on predecessor rationale not encoded in project artefacts;
- semantic ablation reveals that one specially authored state file contains nearly all continuity;
- accepted code/tests/docs are insufficient without extra transcript-derived memory.

This does not imply all repositories fail. It narrows the task/repository class.

## Evidence against the accepted-boundary distinction

The strongest prior challenge, Handoff Debt (arXiv:2606.02875), shows repository-only takeover can be expensive for interrupted tasks.

RaS's distinguishing hypothesis is that **validated accepted boundaries** externalise enough state to reduce that handoff debt.

This distinction is weakened if post-acceptance forced reset shows similar rediscovery penalties to interrupted-task takeover, especially when persistent history improves efficiency without harming correctness.

## Evidence against semantic-state ablation claims

Condition C is uninformative or adverse if:

- ablation merely makes the repository broken or unrealistic;
- removed information remains redundantly available elsewhere;
- task meaning changes because the artefact is removed;
- arbitrary large-scale deletion causes failure but says nothing about marginal continuity;
- effects do not replicate across tasks.

The valid question is marginal continuity value of a preregistered artefact class.

## Evidence against tiered execution

Tiered execution is weakened if lower-cost/stateful workers:

- reduce verifier success;
- increase retry/escalation enough to erase nominal model savings;
- require high-capability re-entry on most tasks;
- add coordination latency exceeding execution savings;
- need privileges equivalent to the high-capability reasoner.

This claim is outside the primary P0 comparison.

## Evidence against security implications

Security implications are weakened if separation:

- fails to reduce actual privileges held by components;
- creates exploitable confused-deputy paths;
- lets repository prompt injection persist across fresh reasoners;
- lets malicious tests/dependencies or commit metadata bypass policy;
- increases trusted-computing-base size or approval burden without reducing impact.

No positive security property exists at v0.1.

## Evidence against generalisation

A strong RaS generalisation is weakened if apparent advantages:

- disappear on unrelated public repositories;
- depend on unusually complete tests/docs;
- disappear with larger repositories or wider dependency graphs;
- disappear on different model families;
- depend on author-selected historical tasks;
- fail when task sets are independently constructed.

## P0 interpretation gate

P0 may end only in one of:

- **METHODOLOGY FAILURE**
- **EVIDENCE AGAINST RaS**
- **MIXED / CONDITIONAL PILOT EVIDENCE**
- **SUPPORTIVE PILOT EVIDENCE**

P0 may not end in **PROVEN**.

## Stop conditions before P0

Do not execute P0 if:

- A/B differ on uncontrolled model/tool/workspace/environment state;
- account-level/session memory cannot be disabled or audited;
- the FUTURE_HISTORY_LEAK_GATE cannot fail closed;
- task corpus selection is not frozen;
- hidden verifier hashes are not frozen;
- human-rescue/rerun rules are not preregistered;
- reconstruction telemetry is too incomplete to evaluate rediscovery.
