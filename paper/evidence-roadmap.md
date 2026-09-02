# Evidence roadmap — What would convince a sceptic?

This roadmap prevents one successful pilot from being promoted into a general validation claim.

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

## Level 1 — P0 methodology pilot / initial case study

Required:
- matched A/B history treatment;
- canonical workspace rematerialisation;
- FUTURE_HISTORY_LEAK_GATE;
- frozen task corpus and hidden verifier hashes;
- no human rescue;
- reconstruction probe and resource telemetry;
- approximately five genuinely dependent tasks.

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

This is not part of P0.

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

A paper should state the highest achieved level and the exact claim family it supports. Level 1 supportive evidence is not Level 6 validation.
