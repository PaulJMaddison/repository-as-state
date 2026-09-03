# P0 corpus selection protocol v2

Status: corpus preparation only. No experimental agent run has occurred.

## Why this protocol exists

SearchForCars Subject-B has now exhausted its allowed three-task recovery path under the accepted-boundary and coherent-work-package rules. The final two recovery intervals were independently adjudicated as forced composites, so no replacement contracts were frozen.

That result closes SearchForCars as the primary three-task P0 corpus. It does **not** invalidate SearchForCars as observational evidence or as a later replication source.

Because no A/B experimental agent has run, a replacement P0 subject can still be selected transparently before any causal result exists.

## Pre-existing repository order

Before the SearchForCars recovery failure, the durable RaS replication plan already identified this progression:

1. SearchForCars — primary P0 candidate;
2. RoomBundle — best close replication;
3. KynticAI Marketing — heterogeneous replication;
4. KynticAI Agent Swarm — heterogeneous systems replication;
5. Fortress — high-complexity stress test;
6. main KynticAI platform — broad natural-history replication.

SearchForCars is now closed for the minimum three-task P0. The next candidate is therefore **RoomBundle**, not a repository selected after inspecting which alternative gives a favourable result.

## Subject naming

Preserve the audit trail:

- Subject-A: original Fortress preparation, rejected before P0;
- Subject-B: SearchForCars, rejected as a three-task P0 corpus before P0;
- Subject-C: RoomBundle, next replacement P0 candidate.

Do not relabel Subject-B after the fact.

## RoomBundle curation protocol

The RoomBundle history must be curated without experimental execution and without using discriminator outcomes to select boundaries.

### 1. Freeze the source history

Identify the exact local repository whose Git remote is `PaulJMaddison/roombundle`.

Fetch its authoritative remote without altering the live worktree.

Freeze:

- remote/default branch name;
- exact HEAD commit;
- exact tree SHA;
- first-parent history;
- merged PR/work-package metadata available at freeze time.

### 2. Enumerate natural work-package boundaries

Prefer pre-existing engineering boundaries such as:

- merged PR completion;
- reviewed branch integration;
- explicit build/fix/test completion;
- committed SESSION/state handoff that marks work-package completion.

Do not use individual commit greenness as the definition of acceptance.

Broken implementation commits may exist inside one accepted work package.

### 3. Accepted-boundary gate

A proposed boundary is accepted only if exact historical materialisation can establish the repository's required health gate.

Use the historical repository/toolchain configuration.

Where a monolithic runner hangs after deterministic test completion, preserve the caveat and use a frozen deterministic partitioned replay only if needed to establish complete test accounting.

Harness defects are not product failures.

### 4. Minimum sequence

P0 requires at least four accepted states producing three sequential coherent work-package transitions.

Do not combine unrelated programmes merely to reach three tasks.

If fewer than three coherent transitions exist, stop RoomBundle and move to the next repository in the pre-existing order.

### 5. Coherence before contract construction

For each candidate transition, independently determine whether it is one defensible historical engineering work package.

A large multi-layer task is allowed.

A convenient bundle of unrelated objectives is not.

Do not use hidden PRE/POST discriminator outcomes when deciding coherence.

### 6. Freeze task contracts before discriminator execution

Only after a transition passes boundary and coherence gates:

- write a neutral task specification;
- write comprehensive hidden behavioural requirements;
- hash both;
- record PRE/POST identities;
- freeze before any new hidden behavioural execution.

Do not tune requirements after observing PRE/POST.

### 7. Hidden verifier architecture

Hidden task verification should be a fast behavioural oracle, not a full historical CI runner.

Prefer direct deterministic service/public-seam scenarios with private fakes.

The accepted-boundary full suite and hidden task discriminator are separate mechanisms.

### 8. Discriminator gate

For a candidate to enter the P0 corpus:

- verifier harness valid;
- every frozen requirement evaluated on PRE and POST;
- PRE overall task result FAIL because at least one material task-introduced behaviour is absent;
- POST all frozen requirements PASS;
- meaningful behavioural negative controls discriminate;
- verifier remains implementation-independent.

Not every individual frozen requirement needs to fail on PRE.

### 9. Experimental isolation

No P0 A/B agent may run until:

- minimum three-task chain is fully verifier-valid;
- private lock/preregistration is created;
- runtime/model/network isolation is frozen;
- cross-session memory leakage controls are in place.

Experimental generated code is never carried into the next task. Both conditions rematerialise the same frozen historical accepted PRE for each task.

## Stop/fallback rule

If RoomBundle cannot produce a valid three-task chain, do not search arbitrary boundaries or weaken the protocol.

Record the failure and proceed to the next repository in the already-frozen order:

`KynticAI Marketing -> KynticAI Agent Swarm -> Fortress -> main KynticAI platform`

Each repository gets the same accepted-boundary/coherence/contract/discriminator gates.

## Epistemic status

Corpus curation outcomes are feasibility evidence, not positive causal evidence for Repository-as-State.

As of this protocol freeze:

- experimental agent runs: 0;
- P0 executed: false;
- positive empirical RaS result: false.
