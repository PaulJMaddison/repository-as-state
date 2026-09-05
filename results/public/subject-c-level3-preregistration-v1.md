# Subject C Level-3 preregistration — coordinator-accepted Phase C binding

Item 65 remains active. Programme state remains **64/67 complete**.

Subject C is an independently selected private repository with three sequential historical tasks: `SC_T01`, `SC_T02`, and `SC_T03`.

The frozen Level-3 design uses **3 tasks × 3 repetitions × 2 conditions = 18 scheduled model runs**, producing **9 matched task × repetition units**. The governing semantic-behaviour denominator was frozen at **10 behaviours** before experimental execution.

Condition A preserves reasoning/session continuity through `SC_T01 -> SC_T02 -> SC_T03` within each repetition. Every task still receives a fresh frozen PRE workspace and generated code is not carried between tasks. Condition B uses a fresh independent session for every task. Model, runtime, source state, prompts, permissions and acceptance semantics are matched across conditions.

The accepted runtime binding is `gpt-5.6-luna` via `codex-cli 0.153.0-alpha.5` under the qualified non-admin restricted identity.

Phase C created and sealed the private randomisation schedule and blind mapping, materialised 18 isolated source-only PRE workspaces, and froze the final execution lock. All 18 workspaces passed future-history, private-material and reparse-point leak gates.

The experimental policy is explicit: **no project build, compiler/typechecker, public tests or lint are used during the experiment.** Correctness is not inspected during execution. All 18 outputs must be frozen before the hidden source/state semantic verifier is run against any model output.

Phase-C activity counters were all zero for project builds, compilers, public tests, lint, Subject-C task-model runs, correctness adjudications and hidden-verifier runs against model output.

Accepted private package commitments:

- Phase A: `6b54c793b07c706362f82efa7a64dd59276b059dd12aa583b43e99f78aa26373`
- Phase B v2: `ee2c288203cf1e36c368624e9efb18ffe0983d29aa89f698eeddef350081fadf`
- Semantic verifier v2: `18aa90e28afbf1f36d2aa909417cb436279ddf20fc8c99e516ae25f42f25c0cd`
- Phase C execution lock: `9538cc1b9af91b732127d08085a7f2211f37f15fd5bd091d8b03a2493f770afe`

The private seed, schedule, blind mapping, repository identity, historical commit identities and hidden-verifier implementation are not published.

Item 65 is **not complete**. The next step is the locked 18-run execution block. Item 66 remains blocked.
