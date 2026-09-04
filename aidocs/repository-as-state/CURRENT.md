# Repository-as-State — CURRENT

Updated: 2026-09-04 14:57 Europe/London

## Programme status

- Authoritative progress ledger: **61/67 complete**.
- Items 58, 59, 60 and 61 are **COMPLETE**.
- **Item 62 is ACTIVE — execute the fresh locked post-isolation 24-run P2 replication.**
- Items 63–67 remain pending.
- Fresh accepted P2 experimental units before Item-62 execution: **0**.
- Fresh P2 model completions before Item-62 execution: **0**.
- Fresh P2 correctness adjudications: **0**.
- Hidden verifier executions against fresh experimental candidates: **0**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Core framing

- Persist authoritative state; reconstruct computation.
- Do not allow ephemeral state to become authoritative state.
- The unit of progress is validated repository state, not accumulated agent conversation.
- Repository-as-State is not repository-as-prompt.

## Accepted P2 Level-2 design

Final task order:

- `P2V2_T01 = C07`
- `P2V2_T02 = C08`
- `P2V2_T03 = C09`
- `P2V2_T04 = C10`

Governing behaviours: **13** (`2 + 3 + 4 + 4`).

Design: **4 tasks × 3 repetitions × 2 conditions = 24 runs**.

Condition A:

- 3 independent persistent-session chains;
- each chain `T01 → T02 → T03 → T04`;
- fresh exact PRE workspace for every task;
- generated code never carries between units;
- only model/session reasoning continuity carries.

Condition B:

- 12 fresh independent sessions.

Matched unit: task × repetition.

Frozen discipline:

- repetitions are replications, not retries;
- no best-of-N;
- no human rescue;
- no post-activity model-quality retry;
- full-block blindness;
- all 24 outputs freeze before hidden adjudication;
- resource telemetry separate from correctness;
- descriptive replication only.

## Accepted upstream identities

Item 58:

- design freeze: `782ADD46591FCCDCABB796D25DC3BE71B03627FCC082372B1FD018875DE1248A`
- design package: `C5124105BD1701A2336211776AF1E3D7E1ED98270665ABAA39910385B81C41F3`

Item 59:

- item-59 freeze: `FE254B6786D9F800674B88576A99336EA118784481FD8252CC76BEE8F102A9E9`
- curation package: `FC6CFDAEF1B5599FE2242C88B1B82985D423F4F64732497F65FAFD3BFAD8C867`

Item 60 semantic:

- semantic verifier freeze: `EF4DEAFBD34E3411C316241AB02A1F19C14A852031B722BAB75CC8DAB97553E1`
- semantic verifier package: `D3C77EDE2D3B41716035F0EEB5977F69898D97C46D9015E4C74C61EA244FDD48`

Item 60 isolation:

- isolation freeze: `9CD6FE3E1F2B204864B6973B115831411CD911EF4363A5F1139DBFBE795AE266`
- isolation package: `CF652E017FE9E84B95EB671087537294C1953611B2D705BD74BFB55791FB5895`

The dedicated experimental identity remains:

`DESKTOP-BFTREBH\ras-p2-experimental`

It is separate from the coordinator identity, non-Administrator, and live qualification established that protected private/coordinator roots are inaccessible while the experimental workspace remains usable.

## Contaminated historical Item-62 attempt

The first live Item-62 task-solving invocation under the superseded same-user boundary was stopped after it proved private methodology was readable by absolute path.

Authoritative contaminated state:

- accepted experimental units: **0**;
- units with genuine model activity: **1**;
- hidden verifier runs: **0**;
- correctness adjudications: **0**;
- correctness-related private material exposed: **TRUE**.

Evidence:

- event log: `CB8CB6A38424A4D8BFADDAFCCB943BF600775F727A00B9FD7EC51DB03026CBCA`
- partial candidate manifest: `7E72A6004BA07C43A61765E84CC6A3A43CAB445B0945516587DDCF03B0DA31D3`

The attempt is permanently excluded from scientific evidence. Its session, candidate output, correctness, old schedule, old blind mapping and old execution lock must never be reused.

## Fresh Item-61 Phase A — accepted

Terminal:

`VALID_TERMINAL_A_ITEM61_POST_ISOLATION_PHASE_A_READY_FOR_PUBLIC_BINDING`

Execution-authoritative Phase-A commitments:

- runtime manifest: `5FC248F380A623BEF2D83C960FFBEC14F59B58A60C3846165D90F400384FA191`
- model binding: `28705DB131283F57853578076830DBCADE2E90695198B289A5BD6645C2CC1DA4`
- prompt manifest: `DE05F68970B7E4DDE86990335C3621C88C36FB880C86591FC207131ACF164CC4`
- randomisation manifest: `6878648FBB56E03F2BA7EECA6AD17FAB8760203F115CAA515CD3736CAB7D3947`
- experimental-unit manifest: `73DD340957D5850FE059E07F25DAFB84101E9E72C03B3245C5009D07DB6F82BF`
- blind-ID mapping: `CB6AB22AA185E45FF085C89104086743DA26262274BE053ECF40768646A9D498`
- PRE-workspace manifest: `209FA8ADA0282569B43A4A626DE3750853671CAC268CA5D5A19DC388ED980456`
- restricted execution launcher: `6D1DECCD2DB3B29D32D736C5930D0724669B500324CA53BEBA7175BC33B33687`
- pre-model readiness audit: `5C1D8B7C4332D50EC3B51C335C1DE90321FB5598D15587C49A25FAAA07B7D99D`
- preregistration manifest: `808253DC67896B108BA1B94EE3F9E8243A22BFA02738D3F95D36AA25658F0447`
- preregistration package: `132C3D38170518458FFC8D2F81E458420AFDAE5E2F7CF14FD80F17D2372997B3`

Accepted readiness:

- exact model `gpt-5.6-luna` available without completion;
- prompt files: 4; hidden requirements: 0;
- fresh PRE workspaces: 24;
- future-history/private-material/reparse gates: 24/24 each;
- restricted non-admin launcher stores no password;
- one deterministic randomisation candidate only;
- 24 schedule units with deterministic repeat match;
- all three A-chain orders preserved;
- 24 fresh blind IDs;
- condition mapping sealed;
- package internal bindings valid.

The randomisation seed, schedule, blind mapping and hidden verifier remain sealed.

## Public preregistration-v2 correction history

The first Phase-B audit correctly stopped because the coordinator-published model-binding commitment had accidentally dropped its final hexadecimal character.

Erroneous 63-character value:

`28705DB131283F57853578076830DBCADE2E90695198B289A5BD6645C2CC1DA`

Correct unchanged 64-character Phase-A value:

`28705DB131283F57853578076830DBCADE2E90695198B289A5BD6645C2CC1DA4`

Pre-correction identities:

- public HEAD: `cd43146f5e27ace334c1ef30ab3ce3d154bbe924`
- JSON blob: `04c3019dc427b794cd025b8e5d23a5fc7e6a5c62`
- Markdown blob: `f6d0a70acf0e7ef27954049a11c54034c8891d05`

This was a public transcription defect only. No private Phase-A bytes, prompts, model, randomisation, schedule, blind mapping, timeout or experimental output changed. The corrected public binding preserves the history explicitly.

## Item 61 Phase B — accepted and publicly locked

Accepted terminal:

`VALID_TERMINAL_A_ITEM61_POST_ISOLATION_PHASE_B_FINAL_ZERO_MODEL_LOCK_READY_FOR_COORDINATOR_ACCEPTANCE`

Phase B revalidated:

- expected/observed pre-lock public HEAD: `74fe1a64c4dfeb618f15f9cea59ed4f04efbf9de`;
- public repository modified by worker: **FALSE**;
- corrected public binding matches private Phase A: **TRUE**;
- Phase-A execution-authoritative bytes changed after publication: **FALSE**;
- item-58/item-59/item-60 semantic/item-60 isolation identities valid: **TRUE**;
- target model: exact `gpt-5.6-luna`, available without completion;
- prompts unchanged: **TRUE**;
- fresh workspace gates: **24/24 each**;
- restricted identity remains non-admin and isolated;
- restricted launcher unchanged and stores no password;
- schedule unchanged and deterministic repeat-match: **TRUE**;
- A-chain order preserved for all three repetitions;
- blind IDs unchanged; mapping sealed;
- contaminated execution/session/code/correctness not reused or inspected;
- plaintext credentials in artifacts/templates/public drafts: **0**;
- fresh accepted P2 units: **0**;
- model completions: **0**;
- P2 task-solving model invoked: **FALSE**;
- hidden verifier runs against fresh candidates: **0**;
- P2 correctness adjudications: **0**;
- P2 executed: **FALSE**.

Final private execution-lock identities:

- execution-lock manifest: `A1D0B4837228E7A2F115FCB6E8A6D8A65930FA88BC031D600382C69A1E492094`
- execution-lock package: `A48928533D173C9AEEF31CA9CDFE92D884788A6A3482D9D7B646C6696C8F53F8`

All Phase-B SHA-256 identities are 64 characters, repeat matches are true, and package internal bindings validate.

Public-safe lock evidence:

- `results/public/subject-b-p2-execution-lock-v2.json`
- `results/public/subject-b-p2-execution-lock-v2.md`

## Active Item 62

Item 62 must execute the **exact locked 24-run experiment**.

Absolute execution rules:

- use the frozen private schedule and blind mapping exactly;
- do not regenerate the schedule, blind IDs, prompts, workspaces or model binding;
- task-solving processes run only as `DESKTOP-BFTREBH\ras-p2-experimental` and never as coordinator/Admin;
- exact model `gpt-5.6-luna`; no silent substitute;
- 1800-second timeout per unit;
- fresh exact PRE workspace every unit;
- Condition A continuity is session/reasoning continuity only; generated implementation never carries;
- B sessions remain fresh;
- repetitions are independent replications, not retries;
- no best-of-N, human rescue or post-model quality retry;
- no hidden correctness verifier or partial correctness adjudication until **all 24 outputs are frozen**;
- resource telemetry remains separate from correctness;
- contaminated historical execution must remain quarantined and unused.

A run that reaches genuine model activity counts as that unit's one attempt even if the output is poor or incomplete. Do not selectively retry it for quality.

Item 62 completes only after all 24 locked units have been attempted under the frozen rules and their output states/evidence have been frozen without hidden correctness inspection.
