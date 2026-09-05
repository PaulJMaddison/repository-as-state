# Repository-as-State aidocs

This directory is the durable coordinator-facing state for the Repository-as-State research programme.

## Read order

When resuming the work, read in this order:

1. `CURRENT.md` — authoritative mutable current state.
2. latest `HANDOFF-*.md` — exact continuation point and active work package.
3. `PROGRAMME-MATRIX.md` — explicit 1–67 progress ledger.
4. `SESSION-2026-09-03.md` — major decisions and results from the current research session.
5. public experiment/methodology evidence under `experiments/`, `results/public/` and `paper/`.

## Rules

- Public/shared GitHub changes are owned by the ChatGPT/coordinator unless explicitly delegated.
- Codex is primarily used for local/private implementation, execution, verifier qualification and evidence generation.
- P0 is immutable and must never be rerun.
- P1 is complete, adjudicated, interpreted and publicly recorded; it must never be silently rerun or amended.
- P2 is a completed, accepted Level-2 same-repository replication with a documented floor-effect result; repetitions were independent observations, not retries.
- Hidden verifier source/oracle implementation must not be copied into public `aidocs`.
- A verifier may be hidden. A requirement may not be hidden.
- Do not upgrade bounded empirical results into equivalence, non-inferiority, universal repository sufficiency, cost superiority, security or tiering claims without the required evidence.

`CURRENT.md` should be updated after every accepted research gate.
