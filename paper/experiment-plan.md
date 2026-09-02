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
Estimate stochastic variation and paired A/B effects.

### P2 — Multi-repository replication
Public unrelated repositories, languages, architectures, task classes and dependency widths.

### P3 — Semantic-state ablation
Small causal ablations of durable artefact classes.

### P4 — Tiered execution
Separate executor-capability/economic study.

### P5 — Reconstruction scaling
Vary repository mass and dependency width; compare retrieval strategies.

### P6 — Cross-model continuity
M_A creates accepted state; M_B resumes without predecessor model-native state.

## Decision gates

Do not run P0 until all readiness items in experiments/P0/readiness-checklist.md are frozen and auditable.

Do not make behavioural continuity claims if A/B treatment isolation is not demonstrated.

Do not make economic claims without reconstruction/retry costs.

Do not make security, serving or generalisation claims from P0.
