# Experiment plan — Paper v0.1

## P0 — Forced-State-Reset Pilot

**Status: NOT EXECUTED.**

Purpose: validate the continuity intervention, task sequencing, history isolation, hidden verification, reconstruction probe, telemetry and public/private evidence pipeline before any confirmatory claim.

### Before P0 is allowed to run

1. independently audit the paper, claims register, novelty boundary and experimental design;
2. select approximately five genuinely sequential non-trivial tasks from a complex private software repository;
3. pin the allowed starting history for every task;
4. ensure future solution commits, refs, reflogs, pack objects and remotes cannot be resolved;
5. create neutral task specifications without hidden solution language;
6. define hidden behavioural verification before the model sees the task;
7. freeze the state-reconstruction probe rubric;
8. freeze reconstruction-cost classification;
9. define model/configuration pinning and sampling settings;
10. define agent failure versus harness/infrastructure failure;
11. define allowed retries, timeouts and cancellation rules;
12. define prohibited human intervention;
13. define sanitisation and public evidence fields;
14. commit the preregistration before observing outcomes.

### Primary P0 conditions

**A — Persistent monolithic control**
- same high-capability session continues;
- conversation/history retained;
- agent may reason, edit and test.

**B — RaS forced reset**
- same high-capability model/configuration;
- complete allowed repository state;
- fresh session after every bounded task;
- no prior conversation, summary, resume state or copied reconstruction.

**C — Semantic-state ablation**
- same as B;
- preregistered semantic state carriers removed;
- source/tests/build rules preserved unless explicitly part of the ablation.

Condition D (tiered execution) should normally be deferred until the core continuity intervention is understood.

### State-reconstruction probe

Before edits in reset conditions, capture outside the subject repository:

- relevant architecture;
- current behaviour;
- affected components;
- constraints/invariants;
- relevant tests;
- completed prior work;
- current remaining work;
- evidence paths;
- uncertainty;
- unknowns.

Do not collect hidden chain-of-thought.

### Telemetry

Capture where available:

- total input/output tokens;
- reconstruction-attributed tokens;
- cached/uncached input;
- files/bytes read;
- repository searches;
- symbol/history operations;
- tool calls;
- model calls;
- reconstruction elapsed time;
- total elapsed time;
- retries;
- escalation;
- human-intervention flag;
- harness-failure flag.

### Primary outcome

Correct engineering continuation under independent hidden behavioural verification.

### Secondary outcomes

- RRI by sequential depth;
- state-reconstruction accuracy;
- Reconstruction Token Fraction;
- regression rate;
- reconstruction and total measured cost proxies;
- retry/escalation behaviour.

## P1 — Public controlled replication

Replicate A/B on public repositories with multiple languages, repository sizes, documentation qualities, dependency widths and task localities. Establish uncertainty intervals and power analysis.

## P2 — Semantic-state ablation

Systematically remove durable state classes to estimate which artefacts carry continuity and which are redundant.

## P3 — Tiered execution

Compare monolithic high-capability execution with high-capability reasoning plus constrained lower-cost/stateful workers. Count failed execution and reasoning re-entry.

## P4 — Reconstruction scaling

Hold task semantics constant while varying irrelevant repository mass and dependency width. Compare reconstruction strategies and test the bounded-K assumption directly.

## Decision gates

Do not make a positive repository-sufficiency claim if reset integrity cannot be proven, hidden verification is not independent, or task construction leaks future state.

Do not make a state-economics claim if reconstruction, retry and execution costs are incomplete.

Do not make a tiered-execution claim before quality-equivalence criteria are defined.
