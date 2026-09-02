# P0 accepted-boundary definition

P0 resets reasoning only after a **validated accepted engineering transition**.

A selected boundary is credible when the historical post-state is a committed, coherent engineering state and the selected requirement has deterministic local behavioural contracts appropriate to the task. Evidence may include:

- committed repository state;
- deterministic unit/integration tests;
- local build/compile viability;
- deterministic proof harnesses;
- fail-closed contract checks;
- coherent progression into the next historical engineering task;
- no known intentionally incomplete work merely required to make the selected requirement valid.

## Historical acceptance versus current reproduction

These are deliberately separate:

**HISTORICAL ACCEPTANCE EVIDENCE** describes what the historical repository state contains and records.

**CURRENT REPRODUCTION EVIDENCE** is a new deterministic build/test execution of that historical boundary.

For the selected P0 corpus, all five boundaries are judged credible accepted states from the committed programme structure plus deterministic behavioural test/proof contracts. Exact historical CI/check runs are not attached to those five boundary commits, and current private-source historical build reproduction was not available in the connector-only curator runtime.

This limitation is frozen into the preregistration. It must not later be rewritten as if exact historical CI evidence had been observed.

## Boundary rule

P0 must never move the reset boundary into partially completed work merely to obtain a favourable comparison. The experiment is explicitly about handoff **after acceptance**, not arbitrary interruption.
