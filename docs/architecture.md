# Architecture

## State transition

A RaS engineering step is modelled as:

    (R_t, U_t) -> reasoning transaction -> proposed bounded work
               -> execution -> validation -> R_(t+1)

R_t is the durable repository state and U_t the current engineering task. The reasoner should not require the complete prior dialogue. It should reconstruct the smallest sufficient subset of repository information, reason over the task, and leave durable evidence for the next step.

## Layers

1. **Durable repository state** — versioned source, tests, documentation, schemas, build rules and Git history.
2. **Reconstruction** — retrieval, file inspection, dependency tracing and selective context assembly.
3. **High-capability reasoning** — architecture, decomposition, difficult debugging, review and interpretation.
4. **Bounded execution** — editing, compilation, tests, formatting and restricted Git/environment operations.
5. **External adjudication** — compiler, test suites, runtime measurements, hidden verification and human review where pre-registered.
6. **Persistence** — accepted changes become the next repository state.

## Invariants

- Repository state is authoritative; conversation is not.
- Reconstruction is selective; repository size is not equivalent to prompt size.
- State transitions require evidence appropriate to the task.
- Hypotheses, measurements and conclusions are distinct artefacts.
- Private experiment subjects and public research evidence are separated by a sanitisation boundary.
