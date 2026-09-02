# Repository-as-State (RaS)

**Independent research by Paul Maddison**

Repository-as-State (RaS) is a software-engineering and AI-systems research project investigating whether durable engineering continuity can live primarily in the repository rather than inside a long-lived high-capability reasoning session.

The central proposition is:

> **Durable engineering continuity does not necessarily need to live inside the expensive high-capability reasoning process.**

RaS explores an architecture in which high-capability reasoning is invoked transactionally, while durable engineering state remains in versioned repository artefacts such as source code, tests, schemas, documentation, build information, architecture records, Git history, and reproducible evidence.

The core systems principle is:

> **Persist authoritative state. Reconstruct computation.**

## Working paper

**Repository-as-State: Externalising Agent Continuity for Stateless High-Capability Reasoning**

Author: **Paul Maddison**  
Location: **Liverpool, United Kingdom**

This is independent research published under Paul Maddison's name.

## Current status

**CONTROLLED EMPIRICAL EVIDENCE STATUS: NOT YET AVAILABLE.**

The current work establishes the theoretical model, research questions, proposed metrics, experimental design, claims discipline, and the foundation for the first forced-state-reset pilot.

P0 — the Forced-State-Reset Pilot — has **not** yet been executed. No controlled empirical claim that RaS works, reduces cost, or preserves engineering quality has been made.

## Research questions

RaS currently investigates four questions:

1. Can repository state substitute for persistent conversational or agent state as the primary continuity mechanism for long-horizon software-engineering work?
2. Can externalising continuity reduce high-capability model state or context required per successful unit of engineering work?
3. Can high-capability reasoning be separated from lower-cost or constrained execution without materially reducing engineering success?
4. Which repository artefacts actually carry enough semantic state for a fresh reasoning process to continue correctly?

## Current research branch

The initial paper, theory, protocols, claims register, experiment templates, bibliography, and research tooling are being developed on:

**`research/initial-paper-foundation`**

[View the current research foundation](https://github.com/PaulJMaddison/repository-as-state/tree/research/initial-paper-foundation)

The research branch remains separate from `main` while the initial foundation is reviewed and the P0 experiment is prepared.

## Research discipline

This project distinguishes carefully between:

- **THEORETICAL** — derived from stated assumptions;
- **OBSERVED** — practical motivation or experience;
- **EMPIRICAL** — supported by controlled experiment;
- **EXTERNAL** — supported by cited third-party evidence;
- **HYPOTHESIS** — a proposition to be tested;
- **IMPLICATION** — a conditional consequence if underlying claims hold.

Hypotheses are not silently upgraded into empirical claims.

## Public repository

This is a public research repository. Proprietary source code, private experimental evidence, credentials, customer or employer data, and other confidential material must not be committed.

Private experimental subjects, if used, remain outside this repository until results are sanitised into publication-safe evidence.

## Licence

Research software in this repository is licensed under Apache-2.0 unless otherwise stated. Paper text and third-party material remain subject to their applicable rights and eventual publication terms.
