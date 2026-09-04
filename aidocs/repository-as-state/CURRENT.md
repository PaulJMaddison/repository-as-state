# Repository-as-State — CURRENT

Updated: 2026-09-04 14:48 Europe/London

## Programme status

- Authoritative progress ledger: **60/67 complete**.
- Items 58, 59 and 60 are **COMPLETE**.
- **Item 61 is ACTIVE**.
- Fresh post-isolation Item-61 Phase A is accepted.
- The public preregistration-v2 binding has been corrected and republished after a Phase-B integrity audit detected a one-character coordinator transcription defect in the public model-binding SHA-256.
- Item-61 Phase B final zero-model execution lock must now be rerun against the corrected public binding.
- Item 62 is **BLOCKED** until that lock is accepted.
- Items 63–67 remain pending.
- Fresh accepted P2 experimental units: **0**.
- Fresh P2 model completions: **0**.
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

It is separate from the coordinator identity, non-Administrator, and live qualification established that protected private/coordinator roots were inaccessible while the experimental workspace remained usable.

## Contaminated historical Item-62 attempt

The first live Item-62 task-solving invocation falsified the original same-user isolation assumption. It was stopped immediately.

Authoritative contaminated state:

- accepted experimental units: **0**;
- units with genuine model activity: **1**;
- hidden verifier runs: **0**;
- correctness adjudications: **0**;
- correctness-related private material exposed: **TRUE**.

Evidence:

- event log: `CB8CB6A38424A4D8BFADDAFCCB943BF600775F727A00B9FD7EC51DB03026CBCA`
- partial candidate manifest: `7E72A6004BA07C43A61765E84CC6A3A43CAB445B0945516587DDCF03B0DA31D3`

The attempt is permanently excluded from scientific evidence. Its session, candidate output, correctness, old schedule, old blind mapping and old execution lock must not be reused.

## Fresh Item-61 Phase A — accepted

Terminal:

`VALID_TERMINAL_A_ITEM61_POST_ISOLATION_PHASE_A_READY_FOR_PUBLIC_BINDING`

Accepted properties include:

- zero task-solving model completions;
- zero fresh P2 experimental runs;
- exact target model `gpt-5.6-luna` available without completion;
- four exact pre-contamination prompt files;
- hidden prompt requirements: 0;
- 24 fresh PRE workspaces;
- future-history leak gate: 24/24;
- private-material leak gate: 24/24;
- reparse-point escape gate: 24/24;
- restricted launcher targets non-admin `ras-p2-experimental` and stores no password;
- one deterministic new randomisation candidate only;
- no contaminated output influence;
- 24 schedule units with deterministic repeat match;
- all three A chains preserve T01→T02→T03→T04;
- 24 fresh blind IDs;
- condition mapping sealed;
- Phase-A package internal bindings valid.

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

The randomisation seed, schedule, blind mapping and hidden verifier remain sealed.

## Phase-B public-binding integrity blocker and correction

The first post-publication Phase-B worker correctly stopped with:

`VALID_TERMINAL_B_ITEM61_PHASE_B_PUBLIC_PHASE_A_MODEL_BINDING_MISMATCH`

It found that the first coordinator-published preregistration-v2 JSON and Markdown had accidentally truncated the final hexadecimal character from the model-binding SHA-256.

Erroneous public value:

`28705DB131283F57853578076830DBCADE2E90695198B289A5BD6645C2CC1DA`

Length: **63**.

Unchanged private Phase-A artifact and original Phase-A terminal value:

`28705DB131283F57853578076830DBCADE2E90695198B289A5BD6645C2CC1DA4`

Length: **64**.

Pre-correction audit identities:

- branch HEAD: `cd43146f5e27ace334c1ef30ab3ce3d154bbe924`
- JSON blob: `04c3019dc427b794cd025b8e5d23a5fc7e6a5c62`
- Markdown blob: `f6d0a70acf0e7ef27954049a11c54034c8891d05`

Scientific ruling:

- this was a coordinator publication/transcription defect only;
- private Phase-A execution-authoritative bytes changed: **FALSE**;
- prompts changed: **FALSE**;
- randomisation changed: **FALSE**;
- schedule changed: **FALSE**;
- blind mapping changed: **FALSE**;
- model changed: **FALSE**;
- timeout changed: **FALSE**;
- fresh model completions before correction: **0**;
- fresh accepted P2 units before correction: **0**;
- correctness adjudications before correction: **0**.

The public v2 JSON and Markdown have now been corrected and explicitly record this correction history. The original erroneous publication remains auditable through Git history and the identities above.

## Active next gate

Item 61 remains **ACTIVE** at **60/67**.

Run a fresh Item-61 Phase-B zero-model integrity/lock worker against the corrected public preregistration-v2 binding.

The worker must not regenerate Phase A, change any experimental choice, invoke a task-solving model, inspect contaminated correctness, or execute Item 62.

Only after the Phase-B lock is accepted and public-safe execution-lock evidence is published may Item 61 become **61/67** and Item 62 become active.
