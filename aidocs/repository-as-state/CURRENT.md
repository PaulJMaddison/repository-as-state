# Repository-as-State — CURRENT

Updated: 2026-09-04 15:37 Europe/London

## Programme status

- Authoritative progress ledger: **60/67 complete**.
- Items 58, 59 and 60 are **COMPLETE**.
- **Item 61 is REOPENED and ACTIVE — repair restricted Codex runtime accessibility and create a superseding execution lock.**
- **Item 62 is BLOCKED.**
- Items 63–67 remain pending.
- Fresh accepted P2 experimental units: **0**.
- Fresh scheduled P2 units with genuine model activity: **0/24**.
- Fresh P2 correctness adjudications: **0**.
- Hidden verifier executions against fresh experimental candidates: **0**.
- P2 fresh experiment executed: **FALSE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Core framing

- Persist authoritative state; reconstruct computation.
- Do not allow ephemeral state to become authoritative state.
- The unit of progress is validated repository state, not accumulated agent conversation.
- Repository-as-State is not repository-as-prompt.

## Frozen P2 design remains unchanged

- `P2V2_T01 = C07`
- `P2V2_T02 = C08`
- `P2V2_T03 = C09`
- `P2V2_T04 = C10`
- governing behaviours: **13**
- design: **4 tasks × 3 repetitions × 2 conditions = 24 runs**
- matched unit: task × repetition
- Condition A: three independent persistent-session chains, each `T01 → T02 → T03 → T04`, fresh PRE workspace per task, reasoning/session continuity only
- Condition B: 12 fresh independent sessions
- repetitions are replications, not retries
- no best-of-N
- no human rescue
- no post-model quality retry
- full-block blindness
- all 24 outputs freeze before hidden adjudication
- resource telemetry separate from correctness

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

Dedicated experimental identity:

`DESKTOP-BFTREBH\ras-p2-experimental`

It remains separate from the coordinator identity and non-Administrator. Protected private/coordinator roots must remain inaccessible while the experimental workspace remains usable.

## Contaminated historical Item-62 attempt

The superseded same-user Item-62 attempt remains permanently excluded from evidence:

- accepted units: **0**
- units with genuine model activity: **1**
- hidden verifier runs: **0**
- correctness adjudications: **0**
- private correctness-related material exposed: **TRUE**

Evidence:

- event log: `CB8CB6A38424A4D8BFADDAFCCB943BF600775F727A00B9FD7EC51DB03026CBCA`
- partial candidate manifest: `7E72A6004BA07C43A61765E84CC6A3A43CAB445B0945516587DDCF03B0DA31D3`

Never reuse its session, candidate, schedule, blind mapping, execution lock or correctness.

## Fresh Item-61 Phase A — still authoritative

The fresh Phase-A experimental choices remain frozen and unchanged:

- runtime manifest: `5FC248F380A623BEF2D83C960FFBEC14F59B58A60C3846165D90F400384FA191`
- model binding: `28705DB131283F57853578076830DBCADE2E90695198B289A5BD6645C2CC1DA4`
- prompt manifest: `DE05F68970B7E4DDE86990335C3621C88C36FB880C86591FC207131ACF164CC4`
- randomisation manifest: `6878648FBB56E03F2BA7EECA6AD17FAB8760203F115CAA515CD3736CAB7D3947`
- experimental-unit manifest: `73DD340957D5850FE059E07F25DAFB84101E9E72C03B3245C5009D07DB6F82BF`
- blind-ID mapping: `CB6AB22AA185E45FF085C89104086743DA26262274BE053ECF40768646A9D498`
- PRE-workspace manifest: `209FA8ADA0282569B43A4A626DE3750853671CAC268CA5D5A19DC388ED980456`
- original restricted execution launcher: `6D1DECCD2DB3B29D32D736C5930D0724669B500324CA53BEBA7175BC33B33687`
- pre-model readiness audit: `5C1D8B7C4332D50EC3B51C335C1DE90321FB5598D15587C49A25FAAA07B7D99D`
- preregistration manifest: `808253DC67896B108BA1B94EE3F9E8243A22BFA02738D3F95D36AA25658F0447`
- preregistration package: `132C3D38170518458FFC8D2F81E458420AFDAE5E2F7CF14FD80F17D2372997B3`

The randomisation seed, schedule, blind mapping and hidden verifier remain sealed.

The earlier coordinator transcription correction to the public model-binding commitment remains historical and resolved; private Phase-A bytes were never changed.

## Superseded Item-61 execution lock

The previous zero-model Phase-B lock was accepted with:

- manifest: `A1D0B4837228E7A2F115FCB6E8A6D8A65930FA88BC031D600382C69A1E492094`
- package: `A48928533D173C9AEEF31CA9CDFE92D884788A6A3482D9D7B646C6696C8F53F8`

It is now **preserved as historical evidence but superseded for execution-readiness**.

## Live runtime-access falsification

During the first fresh Item-62 live preflight, before any scheduled task-model activity, the restricted credential was validated and the experimental identity remained non-admin, but Windows denied execution of the frozen Codex executable under that identity.

Worker terminal:

`BLOCKED_PRE_MODEL_RESTRICTED_CODEX_EXECUTABLE_ACCESS_DENIED`

Observed state:

- required public HEAD: `69de3dc9577e38058f0b8c084e669e3d15e2e742`
- public repository modified by worker: **FALSE**
- restricted credential valid: **TRUE**
- restricted identity non-admin: **TRUE**
- frozen Codex executable runnable as restricted identity: **FALSE — Access denied before model process start**
- scheduled units with model activity: **0/24**
- accepted fresh units: **0**
- hidden verifier runs: **0**
- correctness adjudications: **0**
- experimental attempt consumed: **FALSE**
- Item 62 executed: **FALSE**

Public evidence:

- `results/public/subject-b-p2-item61-runtime-access-falsification-v2.json`
- `results/public/subject-b-p2-item61-runtime-access-falsification-v2.md`

Scientific ruling:

- this is **not** experimental contamination;
- it **does** falsify the accepted Item-61 live execution-readiness claim;
- Item 61 is reopened;
- Item 62 is blocked;
- Phase-A experimental choices remain frozen and must not be regenerated.

## Active next gate

Repair only the restricted Codex runtime-access boundary.

The repair must:

- identify the exact current Codex executable/runtime path and ACL/access cause;
- make the exact required Codex runtime executable by `DESKTOP-BFTREBH\ras-p2-experimental` without granting access to protected coordinator/private roots;
- prefer an isolated experimental runtime installation/copy under an experimental-readable root over weakening coordinator-root ACLs;
- prove executable/runtime bytes and exact Codex CLI/model identity;
- prove the restricted identity can launch the runtime;
- preserve the hard private-material deny boundary;
- preserve all prompts, task selection, PRE states, model choice, randomisation, schedule, blind IDs/mapping, timeout, retry discipline and full-block blindness;
- execute **zero scheduled Item-62 task units** during repair;
- create a fresh superseding Item-61 execution-readiness qualification and zero-model execution lock;
- produce public-safe drafts for coordinator publication.

Only after coordinator acceptance/publication of the superseding execution lock may Item 61 return to complete and Item 62 become active again.
