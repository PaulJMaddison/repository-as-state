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

**CONTROLLED EMPIRICAL EVIDENCE STATUS: NOT YET AVAILABLE.**

P0 — the Forced-State-Reset Pilot — has not yet been executed. The repository currently contains theory, formal models, an experimental protocol foundation, a preregistration template, initial research tooling, and a publication-oriented manuscript draft. It does **not** contain evidence that RaS has been empirically validated.

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

- **P0:** forced-state-reset pilot on a private subject with public sanitised aggregates.
- **P1:** replicated tasks across multiple repositories and controlled persistence/reset conditions.
- **P2:** semantic-state ablations to identify which repository artefacts carry continuity.
- **P3:** tiered-execution experiments separating high-capability reasoning from constrained execution workers.
- **P4:** cross-model and cross-repository replication with reconstruction-cost scaling analysis.

See [docs/](docs/), [paper/](paper/), and [experiments/P0/](experiments/P0/).

## Public/private boundary

This repository is public. Proprietary source code, private diffs, hidden verifier source, private traces containing proprietary source, credentials, customer or employer data, and unnecessary personal filesystem paths must never be committed. Private experiment subjects must cross an explicit sanitisation boundary before any aggregate evidence is published.

## Licence and citation

Research software is licensed under Apache-2.0. Paper text and third-party material retain their applicable rights; do not assume the software licence grants rights to third-party content. Citation metadata is provided in [CITATION.cff](CITATION.cff).
