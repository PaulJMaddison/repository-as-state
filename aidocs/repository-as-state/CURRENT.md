# Repository-as-State — CURRENT

Updated: 2026-09-04 15:58 Europe/London

## Programme status

- Authoritative progress ledger: **61/67 complete**.
- Items 58, 59, 60 and 61 are **COMPLETE**.
- **Item 62 is ACTIVE — execute the fresh locked post-isolation 24-run P2 replication using the accepted isolated runtime and v3 execution lock.**
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

## Frozen P2 design

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

It is separate from the coordinator identity, non-Administrator and non-elevated. Protected private/coordinator roots remain inaccessible while the experimental workspace and isolated runtime remain usable.

## Contaminated historical Item-62 attempt

The superseded same-user attempt remains permanently excluded:

- accepted units: **0**
- units with genuine model activity: **1**
- hidden verifier runs: **0**
- correctness adjudications: **0**
- private correctness-related material exposed: **TRUE**

Evidence:

- event log: `CB8CB6A38424A4D8BFADDAFCCB943BF600775F727A00B9FD7EC51DB03026CBCA`
- partial candidate manifest: `7E72A6004BA07C43A61765E84CC6A3A43CAB445B0945516587DDCF03B0DA31D3`

Never reuse its session, candidate, schedule, blind mapping, execution lock or correctness.

## Fresh Phase-A commitments — unchanged

- runtime manifest: `5FC248F380A623BEF2D83C960FFBEC14F59B58A60C3846165D90F400384FA191`
- model binding: `28705DB131283F57853578076830DBCADE2E90695198B289A5BD6645C2CC1DA4`
- prompt manifest: `DE05F68970B7E4DDE86990335C3621C88C36FB880C86591FC207131ACF164CC4`
- randomisation manifest: `6878648FBB56E03F2BA7EECA6AD17FAB8760203F115CAA515CD3736CAB7D3947`
- experimental-unit manifest: `73DD340957D5850FE059E07F25DAFB84101E9E72C03B3245C5009D07DB6F82BF`
- blind-ID mapping: `CB6AB22AA185E45FF085C89104086743DA26262274BE053ECF40768646A9D498`
- PRE-workspace manifest: `209FA8ADA0282569B43A4A626DE3750853671CAC268CA5D5A19DC388ED980456`
- original restricted launcher: `6D1DECCD2DB3B29D32D736C5930D0724669B500324CA53BEBA7175BC33B33687`
- pre-model readiness audit: `5C1D8B7C4332D50EC3B51C335C1DE90321FB5598D15587C49A25FAAA07B7D99D`
- preregistration manifest: `808253DC67896B108BA1B94EE3F9E8243A22BFA02738D3F95D36AA25658F0447`
- preregistration package: `132C3D38170518458FFC8D2F81E458420AFDAE5E2F7CF14FD80F17D2372997B3`

The randomisation seed, schedule, blind mapping and hidden verifier remain sealed.

## Runtime-access falsification and repair history

The original Item-61 v2 lock was accepted with:

- manifest: `A1D0B4837228E7A2F115FCB6E8A6D8A65930FA88BC031D600382C69A1E492094`
- package: `A48928533D173C9AEEF31CA9CDFE92D884788A6A3482D9D7B646C6696C8F53F8`

The first fresh Item-62 live preflight later proved that the restricted identity could authenticate but could not execute the coordinator-profile Codex runtime. Windows returned `Access is denied` before any task model process started.

That event did not contaminate Item 62 but empirically falsified Item-61 execution readiness. Item 61 was therefore reopened and the v2 lock preserved as historical evidence.

Public falsification evidence:

- `results/public/subject-b-p2-item61-runtime-access-falsification-v2.json`
- `results/public/subject-b-p2-item61-runtime-access-falsification-v2.md`

## Item 61 v3 runtime repair — accepted

The repair provisioned the exact Codex runtime under:

`C:\Kyntic\ras-p2-experimental-runtime-v2`

Accepted runtime facts:

- exact CLI: `codex-cli 0.153.0-alpha.5`
- exact target model: `gpt-5.6-luna`
- restricted identity: `DESKTOP-BFTREBH\ras-p2-experimental`
- administrator: **FALSE**
- elevated: **FALSE**
- runtime depends on coordinator-profile paths: **FALSE**
- protected private root denied: **TRUE**
- protected coordinator root denied: **TRUE**
- protected coordinator Codex home denied: **TRUE**
- experimental workspace access: **PASS**
- prompts/randomisation/schedule/blind mapping/PRE workspaces/model changed: **FALSE**
- scheduled Item-62 units with model activity during repair: **0**
- Item-62 accepted units: **0**
- hidden verifier runs: **0**
- correctness adjudications: **0**
- plaintext credentials in artifacts/templates/public drafts: **0**

Accepted v3 identities:

- execution-lock manifest: `A0A8D89CDC226EE5619C9AA0BE80F936EC84B6218EA14E84F992B650699844DD`
- execution-lock contents manifest: `C774396F9F56DD94CFE0194E2916F891CF5D9CF6DD29D63F6E97AE48A9FBFC73`
- execution-lock package: `908CCB709B08379E616EF62C04B996DB7A526ED91BB66E73491CDE3D8C377D99`

All v3 SHA-256 values are 64 characters, repeat matches are true and package internal bindings validate.

Public v3 evidence:

- `results/public/subject-b-p2-execution-lock-v3.json`
- `results/public/subject-b-p2-execution-lock-v3.md`

The v3 lock supersedes v2 for execution. The falsification history and v2 lock remain preserved.

## Active Item 62

Execute the exact locked 24-run experiment using the accepted isolated runtime.

Absolute rules:

- use the frozen private schedule and blind mapping exactly;
- do not regenerate schedule, blind IDs, prompts, workspaces or model binding;
- task-solving processes run only as `DESKTOP-BFTREBH\ras-p2-experimental`;
- runtime executable is the accepted isolated runtime under `C:\Kyntic\ras-p2-experimental-runtime-v2`;
- exact model `gpt-5.6-luna`; no silent substitute;
- 1800-second timeout per unit;
- fresh exact PRE workspace every unit;
- Condition A carries session/reasoning continuity only, never generated code;
- Condition B sessions remain fresh;
- once genuine model activity occurs, that unit has consumed its one attempt;
- retry only frozen-policy permitted pre-model infrastructure failures;
- no best-of-N, human rescue or post-model quality retry;
- no hidden correctness verifier or partial correctness adjudication until all 24 outputs are frozen;
- contaminated historical execution remains quarantined and unused.

Item 62 completes only after all 24 locked units have been attempted under the frozen rules and their output states/evidence are frozen without hidden correctness inspection.
