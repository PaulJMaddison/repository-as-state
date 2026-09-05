# Repository-as-State (RaS)

**Repository-as-State: Externalising Agent Continuity for Stateless High-Capability Reasoning**

**Independent research by Paul Maddison**

Repository-as-State (RaS) is a software-engineering research project investigating whether durable engineering continuity can live primarily in the repository rather than inside a long-lived high-capability reasoning session.

The central proposition is not that “Git can store agent memory”. It is that **durable engineering continuity does not necessarily need to live inside the expensive high-capability reasoning process**. RaS asks whether high-capability reasoning can be invoked transactionally, allowed to disappear, and later reconstructed from authoritative repository state plus the current task.

> **Core systems principle:** Persist authoritative state. Reconstruct computation.

## Author

**Paul Maddison**  
Independent Researcher  
Liverpool, United Kingdom

This research is published under Paul Maddison's name and is not presented as research produced by, sponsored by, or affiliated with a company or employer.

## Status

**CONTROLLED EMPIRICAL EVIDENCE STATUS: BOUNDED SUBJECT-B P1/P2 EVIDENCE AVAILABLE.**

P0 — the original Forced-State-Reset methodology pilot — was executed exactly once and classified `MIXED_METHODOLOGY_AND_MODEL_FAILURE`; its A/B correctness outcome is not treated as causally interpretable and P0 is not rerun. Subject-B P1 observed equal non-zero behavioural performance (18/30 versus 18/30; 30 matched agreements). Subject-B P2, a four-task, three-repetition Level-2 block, observed equal zero performance (0/39 versus 0/39; 39 agreements and no disagreements), a floor effect that provides no positive evidence of successful behavioural preservation by either condition. These are bounded results, not proof of equivalence, universal repository sufficiency, or general validation.

See the [P1 result](results/public/subject-b-p1-results-v1.md), the [P2 Level-2 evidence summary](results/public/subject-b-p2-level2-evidence-v1.md), and the [paper](paper/).

## Architecture

    Durable Repository State R_t
                +
    Current Engineering Task U_t
                |
                v
    Ephemeral High-Capability Reasoning
                |
                v
    Bounded Work Package / State Transition
                |
                v
    Lower-Cost / Stateful / Local Execution
                |
                v
    Compiler + Tests + Runtime Evidence
                |
                v
    Durable Repository State R_(t+1)

The high-capability reasoning process may then disappear. A later fresh reasoning process receives the updated repository state and a new task, reconstructs only the relevant subset of engineering state, and attempts the next validated state transition.

RaS is **not repository-as-prompt**. A repository may be arbitrarily large; active inference should reconstruct a bounded, task-relevant subset.

## Research questions

1. **Continuity:** Can durable repository state substitute for persistent conversational or agent state as the primary continuity mechanism for long-horizon software-engineering work?
2. **State economics:** Can continuity externalisation reduce the amount of high-capability state/context required per successful unit of engineering work?
3. **Tiered execution:** Can high-capability reasoning be separated from lower-cost stateful execution without materially reducing engineering success?
4. **Repository sufficiency:** Which repository artefacts are actually responsible for successful reconstruction?

## Forced-reset evaluation

The defining evaluation deliberately destroys conversational continuity between bounded engineering stages. A fresh reasoning process receives only the repository and the next task. No previous conversation, resume state, external summary, or copied hidden memory survives.

The proposed **Repository Resumability Index (RRI)** is:

    successful correct continuations after complete agent-state reset
    ----------------------------------------------------------------
                         eligible forced resets

RRI is a proposed research metric, not an established standard.

## Cost hypothesis

The provider-neutral comparison is:

    C_persistent =
        C_reasoning + C_context/history + C_agent-state
        + C_execution + C_tools + C_orchestration

    C_RaS =
        C_reconstruction + C_reasoning
        + C_shallow-execution + C_repository-state

The research question is whether the second quantity can be lower over sufficiently long engineering programmes while preserving engineering quality. RaS makes no claim about any provider's unobservable internal costs.

## Research roadmap

- **P0:** completed once as a methodology pilot; classified `MIXED_METHODOLOGY_AND_MODEL_FAILURE`, with no causal A/B correctness claim and no rerun.
- **P1:** completed Subject-B controlled three-task study; 18/30 behaviours in each condition with 30 matched agreements and no disagreements.
- **P2:** completed Subject-B Level-2 same-repository replication; 0/39 behaviours in each condition with 39 matched agreements and no disagreements, explicitly floor-limited.
- **Next:** Subject C cross-repository replication to test external validity beyond SearchForCars/Subject B.
- **Later:** semantic-state ablation, tiered-execution, reconstruction-scaling, and cross-model continuity studies.

See [docs/](docs/), [paper/](paper/), and [experiments/P0/](experiments/P0/).

## Public/private boundary

This repository is public. Proprietary source code, private diffs, hidden verifier source, private traces containing proprietary source, credentials, customer or employer data, and unnecessary personal filesystem paths must never be committed. Private experiment subjects must cross an explicit sanitisation boundary before any aggregate evidence is published.

## Licence and citation

Research software is licensed under Apache-2.0. Paper text and third-party material retain their applicable rights; do not assume the software licence grants rights to third-party content. Citation metadata is provided in [CITATION.cff](CITATION.cff).
