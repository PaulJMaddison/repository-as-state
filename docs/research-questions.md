# Research questions

## RQ1 — Continuity

Can durable repository state substitute for persistent conversational or agent state as the primary continuity mechanism for long-horizon software-engineering work?

Conceptually:

    P(S | R_t, U_t) ≈ P(S | H_t, R_t, U_t)

where S is successful engineering outcome, R_t durable repository state, H_t accumulated agent or conversation history, and U_t the current task.

The equality is not assumed; it is the object of measurement.

## RQ2 — State economics

Can externalising engineering continuity materially reduce the amount of high-capability model state or context required per successful unit of engineering work?

The principal claim under investigation is not “reasoning becomes cheap”. It is that high-capability reasoning may become **disposable** between transactions.

## RQ3 — Tiered execution

Can high-capability reasoning be separated from lower-cost or local stateful execution without materially reducing engineering success?

## RQ4 — Repository sufficiency

Which repository artefacts are responsible for successful reconstruction of engineering state? Candidate carriers include source, tests, Git history, architecture records, concise state documentation, schemas and reproducible build information.
