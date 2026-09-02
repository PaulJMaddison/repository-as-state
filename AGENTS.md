# AGENTS.md

## Purpose

This is a public research repository for Repository-as-State (RaS). Treat scientific validity, provenance, reproducibility, and the public/private boundary as first-class engineering constraints.

## Required behaviour

- Read this file before modifying the repository.
- Preserve the distinction between THEORETICAL, OBSERVED, EMPIRICAL, EXTERNAL, HYPOTHESIS, and IMPLICATION claims.
- Never convert a hypothesis or observed motivation into an empirical result without controlled evidence.
- Never fabricate measurements, tables, citations, baselines, statistical significance, or experimental outcomes.
- Keep the manuscript, claims register, protocols, and public results mutually consistent.
- Prefer primary papers and first-party technical sources.
- Treat reconstruction cost as a potential falsifier, not an implementation detail.
- Keep active reconstruction bounded and task relevant; RaS is not repository-as-prompt.
- Maintain reproducible protocols and deterministic evidence formats where practical.

## Public repository safety

Never commit proprietary KynticAI source, private diffs, hidden proprietary verifier code, private source snapshots, credentials, secrets, customer data, Very Group material, or model traces containing proprietary source. Do not add unnecessary personal filesystem paths.

Private experimental evidence must remain outside this repository until sanitised into public aggregate evidence.

## Validation

Before a research change is considered complete:

1. inspect the diff;
2. run relevant tests;
3. compile or structurally validate the manuscript;
4. validate citations introduced by the change;
5. check claims-register alignment;
6. confirm no private material or fabricated results were introduced.
