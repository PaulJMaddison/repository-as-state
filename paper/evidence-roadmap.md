# Evidence roadmap — What would convince a sceptic?

This roadmap prevents one successful pilot from being promoted into a general validation claim.

## Current controlled evidence — Subject-B P1

The methodology-corrected Subject-B P1 study is now executed, blind-adjudicated and interpreted.

Across three matched SearchForCars tasks, the persistent-session and fresh-session conditions produced identical behavioural vectors: **30/30 agreements, 0 disagreements**, with both conditions passing 18/30 governing behaviours and 2/3 tasks. WP04 and WP05 passed in both conditions; WP06 failed in both conditions.

This is **supportive-with-limitations single-subject controlled evidence**, not formal equivalence or non-inferiority evidence. Resource/reconstruction evidence is incomplete and mixed. The result therefore sits below Level 2: repeated same-repository runs and a larger preregistered task sample are still required before reliable same-repository effect estimates can be claimed.

Public-safe result record:

- `results/public/subject-b-p1-results-v1.md`
- `results/public/subject-b-p1-results-v1.json`

Historical preregistration state: `d95e2cdc47f8082a805fa2d5b09cdb272cf977ef`.

## Level 0 — Observed workflow motivation

Evidence:
- repeated practical use of fresh reasoning sessions over repository state;
- bounded execution and deterministic validation in real engineering work.

What it supports:
- the research question is grounded in a real workflow.

What it does **not** support:
- causal repository sufficiency;
- cost savings;
- generalisation.

**Current status: available as OBSERVED motivation.**

## Level 1 — Controlled single-repository pilot / initial case study

Required:
- matched A/B history treatment;
- canonical workspace rematerialisation;
- FUTURE_HISTORY_LEAK_GATE;
- frozen task corpus and hidden verifier hashes;
- no human rescue of experimental implementations;
- reconstruction probe and resource telemetry;
- multiple genuinely dependent tasks.

What it can support:
- the intervention is executable;
- leakage can be controlled;
- reconstruction can be measured;
- obvious catastrophic continuity failure is or is not observed;
- supportive/mixed/adverse **pilot** evidence.

What it cannot support:
- general superiority;
- population-level non-inferiority;
- provider-internal savings.

**Current status: achieved for Subject-B P1 behavioural continuity, with incomplete/mixed resource evidence and only three matched tasks.**

## Level 2 — Repeated runs on the same complex repository

Required:
- multiple independent repetitions;
- declared stochastic/sampling policy;
- paired A/B observations;
- dependence-aware uncertainty;
- preregistered non-inferiority/equivalence margin if claimed.

What it can support:
- more reliable same-repository behavioural effect estimates;
- reconstruction-cost distribution;
- depth sensitivity.

Remaining weakness:
- private subject and author/repository bias.

**Current status: not achieved. P2 should target this level before any formal same-repository equivalence/non-inferiority claim is considered.**

## Level 3 — Multiple repositories and task classes

Required:
- unrelated public repositories;
- multiple languages/architectures;
- variation in repository size, task locality, dependency width, documentation/test quality;
- independent task selection rules.

What it can support:
- external-validity claims over the sampled repository/task population;
- reconstruction-scaling analysis.

## Level 4 — Multiple model families

Required:
- repeat matched A/B experiments using independently developed model families;
- record model/tool differences explicitly;
- analyse interactions rather than pooling blindly.

What it can support:
- evidence that observed continuity effects are not specific to one model's navigation or memory behaviour.

## Level 5 — Cross-model continuity

Design:
- model family M_A produces accepted state R_t;
- a different family M_B receives R_t + U_(t+1) without M_A's predecessor history;
- matched controls isolate model-change effects.

Why it matters:
- successful continuation would provide stronger evidence that continuity resides in external project state rather than a provider/model-specific session representation.

This is not part of P1.

## Level 6 — Independent external replication

Required:
- independent investigators;
- independently selected repositories/tasks;
- public protocol and harness;
- independently constructed verifiers;
- replication without author intervention.

What it can support:
- strongest evidence that RaS is not an artefact of one author's repositories, tooling, task selection, or implementation.

## Separate evidence ladders

Do not collapse these into one “RaS validated” badge:

- behavioural continuity;
- reconstruction economics;
- semantic-state causality;
- tiered execution;
- security;
- infrastructure/serving implications.

Each requires its own evidence.

## Publication discipline

A paper should state the highest achieved level and the exact claim family it supports. Subject-B P1 is bounded Level-1 behavioural evidence; it is not Level-2 repeated-run evidence or Level-6 validation.
