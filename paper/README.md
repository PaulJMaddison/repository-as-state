# Paper v0.1

Working title: **Repository-as-State: Externalising Agent Continuity for Stateless High-Capability Reasoning**

Author: **Paul Maddison**  
Affiliation: **Independent Researcher**  
Location: **Liverpool, United Kingdom**  
Version: **0.1.0**

This is the first canonical full theoretical/systems/research-design paper for Repository-as-State (RaS).

## Evidence status

**CONTROLLED EMPIRICAL EVIDENCE IS NOT YET AVAILABLE.**

P0 — the Forced-State-Reset Pilot — has not been executed. The manuscript contains no positive controlled empirical RaS result and no fabricated example result.

## Scope of v0.1

The paper establishes:

- Repository-as-State as a continuity architecture;
- the formal reconstruction/reasoning/execution/validation loop;
- approximate repository sufficiency;
- the full-history versus bounded-reconstruction context model;
- reconstruction cost and Reconstruction Token Fraction;
- provider-neutral state economics;
- transactional high-capability reasoning;
- tiered execution;
- tests and durable semantic state;
- selective durable documentation;
- least privilege;
- Forced-State-Reset Evaluation;
- the proposed Repository Resumability Index;
- the state-reconstruction probe;
- the P0 experimental method;
- repository-state versus agent-state scalability;
- related-work and novelty boundaries.

## Build

From the paper directory:

    pdflatex main.tex
    bibtex main
    pdflatex main.tex
    pdflatex main.tex

A convenient alternative is:

    latexmk -pdf main.tex

The paper uses standard LaTeX packages plus TikZ for source-controlled conceptual figures.

## Research discipline

- Do not invent empirical values.
- Keep hypotheses labelled.
- Treat reconstruction cost as a central falsification route.
- Add only verifiable citations.
- Keep `claims-register.md` consistent with the manuscript.
- Keep private experimental source/evidence outside this public repository.
- Do not treat conceptual figures as measured curves.

## Draft AI-assistance disclosure

Generative AI was used extensively to assist with formalisation, mathematical framing, drafting, literature synthesis, experiment design, and research-software design. The human author controls the research direction, hypotheses, engineering observations, experimental decisions, interpretation, and final claims. AI systems are not listed as authors.

This disclosure remains in the repository rather than the manuscript until the target venue's disclosure requirements are known.
