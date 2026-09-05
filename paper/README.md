# Paper v0.1 — hostile-audit revision

Working title: **Repository-as-State: Externalising Agent Continuity for Stateless High-Capability Reasoning**

Author: **Paul Maddison**  
Affiliation: **Independent Researcher**  
Location: **Liverpool, United Kingdom**  
Version: **0.1.0**

## Audit status

A hostile pre-experiment audit narrowed the novelty and strengthened the experimental design. P0 subsequently ran exactly once and is retained as an immutable methodology/failure record.

**Historical pre-P0 audit decision:** GO_WITH_REQUIRED_PROTOCOL_CHANGES  
**P0 execution status:** EXECUTED ONCE — `MIXED_METHODOLOGY_AND_MODEL_FAILURE`  
**Controlled empirical evidence:** BOUNDED SUBJECT-B P1/P2 RESULTS PUBLISHED

P0 does not support a causal A/B correctness interpretation and must not be rerun. The paper does **not** conclude that RaS is validated. Subject-B P1 provides bounded equal non-zero performance; Subject-B P2 provides a bounded equal-zero floor-effect result. Neither establishes equivalence, non-inferiority, universal repository sufficiency, or generalisation.

Key audit documents:

- `hostile-review-v0.1.md`
- `novelty-audit.md`
- `reviewer-attacks.md`
- `falsification-criteria.md`
- `evidence-roadmap.md`
- `experiment-plan.md`
- `validation-audit.md`
- `../experiments/P0/readiness-checklist.md`

## Narrowed contribution

The broad idea that repositories/Git can serve as agent memory is prior art. The current paper focuses on:

1. disposal of predecessor high-capability reasoning-session state **after validated accepted sequential engineering transitions**;
2. a matched persistent-history versus forced-reset treatment;
3. reconstruction-cost accounting that can falsify the economic thesis;
4. a reportable state-reconstruction probe stored outside the subject workspace;
5. small semantic-state ablations at accepted boundaries.

RRI, tiered execution, repository retrieval, sequential coding evaluation, Git-bound memory, tests/docs as engineering knowledge, and durable compute are not presented as independently novel contributions.

## Major hostile-audit corrections

- removed the unobservable KL-divergence repository-sufficiency formalism;
- replaced it with a behavioural matched A/B target;
- demoted quadratic full-history growth to a naive stress model;
- explicitly state that a managed persistent agent can also have linear cumulative effective context;
- replaced speculative additive economics with an observable resource vector and observability classes;
- demoted RRI to a descriptive metric;
- deferred tiered execution beyond primary P0;
- made Handoff Debt adverse prior evidence;
- added canonical workspace/runtime matching;
- added FUTURE_HISTORY_LEAK_GATE and task-leakage controls;
- added verifier hash/freeze requirements;
- added no-human-rescue and preregistered rerun rules;
- added reproducible historical-corpus selection rules.

## Evidence status

**P0 was executed exactly once and classified `MIXED_METHODOLOGY_AND_MODEL_FAILURE`; its A/B correctness outcome is not causally interpretable.** P1 and P2 are reported as bounded Subject-B evidence in the Results section. Positive evidence for successful P2 behavioural preservation remains absent because both P2 conditions were at the correctness floor.

## Build

From the paper directory:

    pdflatex main.tex
    bibtex main
    pdflatex main.tex
    pdflatex main.tex

or, where available:

    latexmk -pdf main.tex

The paper uses TikZ for conceptual figures.

## Research discipline

- Current prior work must be credited even when it weakens novelty.
- Handoff Debt is not to be dismissed; post-acceptance boundaries are the hypothesis.
- P0 is immutable historical evidence and must not be rerun.
- Do not infer provider GPU/KV/margin savings from client token counters.
- Conceptual figures are not empirical data.
- Public/private boundary remains mandatory.

## Draft AI-assistance disclosure

Generative AI was used extensively to assist with formalisation, mathematical framing, drafting, literature synthesis, hostile review, experiment design, and research-software design. The human author controls the research direction, hypotheses, engineering observations, experimental decisions, interpretation, and final claims. AI systems are not listed as authors.

This disclosure remains outside the manuscript until a target venue's requirements are known.
