# Subject-B P2 execution lock v2

Status: **Item 61 complete. Fresh post-isolation P2 execution is publicly locked and Item 62 may begin.**

This record is the coordinator's public-safe acceptance of the final zero-model Item-61 Phase-B execution lock.

The accepted worker terminal was:

`VALID_TERMINAL_A_ITEM61_POST_ISOLATION_PHASE_B_FINAL_ZERO_MODEL_LOCK_READY_FOR_COORDINATOR_ACCEPTANCE`

The worker validated the corrected public preregistration-v2 commitment against the unchanged private Phase-A package, requalified the restricted execution boundary, independently repeated the schedule/workspace/package checks, created the private execution-lock-v2 package, and stopped with zero fresh experimental activity.

## Programme state at lock publication

- completed items: **61 / 67**
- Item 61: **COMPLETE**
- Item 62: **ACTIVE**
- fresh accepted P2 experimental units: **0**
- fresh model completions: **0**
- fresh correctness adjudications: **0**
- hidden-verifier runs against fresh candidates: **0**
- P2 executed: **false**

## Public-binding integrity

Phase B observed the expected public head:

`74fe1a64c4dfeb618f15f9cea59ed4f04efbf9de`

The public repository was not modified by the worker.

The corrected public preregistration binding matched the private Phase-A state exactly.

- corrected model-binding SHA-256: `28705DB131283F57853578076830DBCADE2E90695198B289A5BD6645C2CC1DA4`
- public preregistration-v2 JSON SHA-256: `156A41127AAD0C2FD7FCD656F9B75D1ACE3CF43594798135071B7EF223B5C5C1`
- public preregistration-v2 Markdown SHA-256: `AEF7DEFC69E7CCE4ACB4546897D25335AA4952EBD4CB6A3884B4111564E82C6D`
- Phase-A execution-authoritative bytes changed after publication: **false**
- correction history present: **true**

The earlier 63-character coordinator transcription defect remains explicitly preserved in the preregistration-v2 correction history and Git history. It did not alter the private experiment.

## Final private execution-lock commitments

- execution-lock manifest SHA-256: `A1D0B4837228E7A2F115FCB6E8A6D8A65930FA88BC031D600382C69A1E492094`
- execution-lock package SHA-256: `A48928533D173C9AEEF31CA9CDFE92D884788A6A3482D9D7B646C6696C8F53F8`
- all Phase-B SHA-256 identities are 64 characters: **true**
- repeated hashes match: **true**
- execution-lock package internal bindings: **valid**

## Execution boundary

- exact model: `gpt-5.6-luna`
- model availability confirmed without completion
- task-solving Windows identity: `DESKTOP-BFTREBH\ras-p2-experimental`
- task-solving identity is Administrator: **false**
- coordinator and experimental identities separate: **true**
- protected private access denial requalified: **pass**
- experimental workspace access requalified: **pass**
- restricted launcher SHA-256: `6D1DECCD2DB3B29D32D736C5930D0724669B500324CA53BEBA7175BC33B33687`
- launcher stores password: **false**
- launcher runs task model as Administrator: **false**
- persistent-session resume mechanism: **valid**
- fresh PRE workspace on resume: **supported**

## Frozen experiment

The accepted design remains unchanged:

- 4 tasks
- 13 governing behaviours
- 3 repetitions
- 2 conditions
- 24 total runs
- 12 matched task × repetition units
- Condition A: three independent persistent-session chains, each `T01 → T02 → T03 → T04`
- Condition B: twelve fresh independent sessions
- fresh exact PRE workspace for every unit
- generated implementation never carries between units
- Condition-A continuity is model/session reasoning continuity only

Phase-B requalification confirmed:

- fresh PRE workspaces: **24**
- future-history leak gate: **24/24**
- private-material leak gate: **24/24**
- reparse-point escape gate: **24/24**
- schedule units: **24**
- deterministic schedule repeat: **match**
- A-chain order preserved in all three repetitions
- outcome information used for scheduling: **false**
- blind IDs: **24**
- new blind IDs created during Phase B: **false**
- condition mapping remains sealed

## Frozen execution discipline

- run timeout: **1800 seconds**
- repetitions are retries: **false**
- best-of-N selection: **false**
- model-quality retry allowed: **false**
- human rescue allowed: **false**
- full-block blindness: **true**
- outputs required before hidden adjudication: **24**
- resource telemetry schema frozen: **true**
- hidden correctness fields in telemetry: **0**

The contaminated historical execution remains excluded. Its candidate code was not reused, its session was not resumed, its correctness was not inspected, and its output did not influence the fresh schedule.

## Zero-model final gate

At final lock creation and coordinator acceptance:

- fresh accepted P2 units: **0**
- model completions generated: **0**
- P2 task-solving model invoked: **false**
- P2 experimental agent runs: **0**
- hidden verifier runs against fresh experimental candidates: **0**
- P2 correctness adjudications: **0**
- P2 executed: **false**

## Sealed material

This public record does **not** publish the randomisation seed, private execution schedule, blind-to-condition mapping, hidden-verifier implementation, credentials, or correctness results.

## Next gate

Item 62 may now execute the exact locked 24-run fresh post-isolation P2 experiment. The execution must follow the frozen private schedule and blind mapping without modification, run task-solving Codex processes only under the restricted experimental identity, preserve full-block blindness, and freeze all 24 outputs before any hidden correctness adjudication.
