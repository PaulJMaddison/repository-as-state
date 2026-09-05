# Experiment plan — Paper v0.1 hostile-audit revision

## P0 — Forced-State-Reset Methodology Pilot

**Status: NOT EXECUTED.**
**Execution readiness: NOT YET READY.**
**Audit decision: GO_WITH_REQUIRED_PROTOCOL_CHANGES.**

P0 is an initial case study whose purpose is to determine whether the treatment can be isolated, leakage prevented, reconstruction measured, and dependent-task continuation adjudicated. It cannot establish general superiority or population-level non-inferiority.

## Primary causal treatment

### A — Persistent-history control

Available at task d:
- canonical accepted project state R_d;
- current task U_d;
- stable experiment instructions;
- predecessor high-capability reasoning-session history.

### B — Forced reset

Available at task d:
- the same canonical accepted project state R_d;
- the same current task U_d;
- the same stable experiment instructions;
- **no predecessor reasoning conversation, hidden summary, resume state, copied reconstruction, or account/session memory**.

The intended A/B difference is predecessor reasoning-session history. Model/configuration, tools, executor, workspace, environment and verifier must be matched.

### C — Exploratory semantic-state ablation

Optional only after A/B integrity is established.

Remove one small preregistered semantic artefact class while preserving task meaning/buildability. The question is marginal continuity value, not whether an agent fails after the repository is broadly damaged.

### D — Tiered execution

**Deferred beyond primary P0.** It changes executor capability and would confound the continuity treatment.

## Required infrastructure before preregistration can be frozen

### 1. Canonical workspace materialiser

Given a task/cutoff manifest, construct condition-independent workspace state:
- exact allowed Git object graph;
- exact tracked files;
- empty/declared untracked state;
- no prior shell/editor/worktree scratch;
- declared toolchain/dependency state;
- declared environment/network state.

The same materialiser must be used for A and B.

### 2. Runtime-control manifest

Freeze:
- high-capability model/provider/model ID;
- API/runtime version where exposed;
- sampling/temperature;
- system/developer experiment instructions;
- tool schema;
- executor implementation/privileges;
- base image/toolchain versions;
- environment variables/locale/timezone policy;
- dependency/cache policy;
- network policy.

If provider/account/session memory cannot be disabled or audited, that runtime is ineligible for the causal A/B experiment.

### 3. FUTURE_HISTORY_LEAK_GATE

Before model invocation verify:
- no remotes;
- known post-cutoff solution SHAs cannot resolve;
- no future refs/tags/reflogs/packed objects;
- no Git alternates or environment-based alternate object stores;
- no source-repository worktree/filesystem link;
- no patch/generated/CI artefact with future solution;
- network cannot retrieve private future source state.

Any failure => **RUN INVALID; STOP BEFORE MODEL CALL.**

### 4. Task-leakage audit

Audit post-cutoff information in:
- commit messages;
- issue edits;
- branch/tag names;
- changelogs/TODOs;
- comments/generated docs;
- future tests;
- task-generation files;
- historical patch files.

Legitimate information already present at cutoff remains allowed.

### 5. Hidden-verifier package

For each task:
- behaviour-oriented;
- outside experimental workspace;
- inaccessible to agent;
- identical across conditions;
- frozen version/hash before runs;
- accepts equivalent correct implementations;
- historical future patch not used as text oracle.

### 6. Reconstruction-probe rubric

Freeze objective reportable items:
- relevant components;
- architecture/state;
- constraints/invariants;
- current behaviour;
- relevant tests/evidence;
- prior accepted work;
- outstanding work;
- uncertainty/unknowns.

Store probe outside subject workspace. Do not request chain-of-thought.

### 7. Run-control rules

Pre-register:
- timeouts/stopping;
- allowed retries;
- cancellation handling;
- AGENT_FAILURE;
- INFRASTRUCTURE_FAILURE;
- rerun eligibility;
- no-human-rescue rules.

## Corpus selection

Before outcomes:
1. define a historical candidate time/window or equivalent reproducible frame;
2. freeze inclusion/exclusion criteria;
3. require genuine sequential dependency across tasks;
4. avoid five unrelated bug fixes;
5. avoid artificially manufactured dependencies;
6. freeze candidate list and task hashes;
7. freeze sampling/randomisation procedure and seed if used;
8. record any subjective complexity label before outcomes.

Approximately five tasks are acceptable for P0 only as a methodology pilot.

## Sequential dependency criterion

A later task should naturally depend on one or more earlier accepted:
- code changes;
- interfaces/contracts;
- tests;
- architecture decisions;
- schemas/migrations;
- state transitions.

The dependence rationale is frozen before runs.

## Telemetry

Capture where observable:
- input/output tokens;
- reconstruction-attributed input;
- cached/uncached tokens;
- files and bytes read;
- repository/symbol/history searches;
- model calls;
- tool calls;
- reconstruction elapsed time;
- total elapsed time;
- retries/escalations;
- verifier result;
- human-intervention flag;
- infrastructure-failure flag;
- provider-billed usage when exposed.

## Outcomes

Primary descriptive P0 reporting:
- matched A/B verifier result by task and depth;
- complete-sequence success.

Secondary:
- B-only RRI by task/depth;
- reconstruction-probe accuracy;
- RTF and full resource vector;
- regression/retry behaviour.

Do not conduct or imply population non-inferiority from ~5 tasks.

## Allowed P0 interpretations

- METHODOLOGY FAILURE
- EVIDENCE AGAINST RaS
- MIXED / CONDITIONAL PILOT EVIDENCE
- SUPPORTIVE PILOT EVIDENCE

Not allowed:
- PROVEN
- GENERAL SUPERIORITY
- PROVIDER-INFRASTRUCTURE SAVING

## Later experiments

### P1 — Repeated same-repository runs
Completed for Subject-B as a bounded three-task controlled study: 18/30 versus 18/30, with 30 matched agreements and no disagreements. It remains supportive-with-limitations and does not establish equivalence or non-inferiority.

### P2 — Level-2 same-repository replication
Completed for Subject-B as four tasks × three repetitions × two conditions. Both conditions satisfied 0/39 behaviours, with 39 matched agreements and no disagreements, a floor effect that provides no positive evidence of successful behavioural preservation. P1 and P2 are not pooled.

### P3 — Multi-repository replication
Independent repositories, languages, architectures, task classes and dependency widths; Subject C is required for this external-validity step.

### P4 — Semantic-state ablation
Small causal ablations of durable artefact classes.

### P5 — Tiered execution
Separate executor-capability/economic study.

### P6 — Reconstruction scaling
Vary repository mass and dependency width; compare retrieval strategies.

### P7 — Cross-model continuity
M_A creates accepted state; M_B resumes without predecessor model-native state.

## Decision gates

Do not run P0 until all readiness items in experiments/P0/readiness-checklist.md are frozen and auditable.

Do not make behavioural continuity claims if A/B treatment isolation is not demonstrated.

Do not make economic claims without reconstruction/retry costs.

Do not make security, serving or generalisation claims from P0.

## P0 corpus-selection status — 2026-09-02

Corpus curation is complete under the hostile-audit controls.

- public subject: `PRIVATE_SUBJECT_A`;
- 38 candidate transitions considered in a bounded programme frozen before task selection;
- five genuinely sequential task units selected;
- neutral task specifications canonicalised and committed by SHA-256 only;
- five credible accepted boundaries identified;
- all selected tasks are designed for deterministic local verification and exclude cloud/live-model/credential dependencies;
- Condition C disabled with `NO_DEFENSIBLE_ABLATION`;
- tiered execution remains deferred;
- FUTURE_HISTORY_LEAK_GATE v0.1.0 implemented and synthetically validated;
- task-specific hidden-verifier behavioural requirements frozen privately; implementation not yet built;
- model/runtime freeze still pending.

The private repository identity, exact historical commits, private paths, task text, solution history, curation notes, and task-specific verifier details are not stored in this public repository.

Because model/runtime identity, resource limits, telemetry, cache/network policy, and cross-session-memory controls remain unresolved:

`P0_PREREGISTRATION_FROZEN=false`

`P0_PROTOCOL_READY_FOR_MODEL_FREEZE=true`

No experimental agent has been run.
## Fixed cross-condition state progression

To preserve causal identifiability, P0 does **not** let A and B produce different repository states for the next task. For each task, both conditions receive independently materialised copies of the same frozen historical accepted pre-state. Experimental outputs are adjudicated and recorded, but the next task advances to the next frozen historical accepted boundary.

This preserves byte-identical repository state across A/B. It also creates a declared limitation: Condition A may retain reasoning about a materially equivalent prior implementation that differs from the next frozen historical boundary. Stable runtime instructions must state that the rematerialised repository is authoritative.

