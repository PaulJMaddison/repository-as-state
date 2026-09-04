# Repository-as-State — CURRENT

Updated: 2026-09-04 16:46 Europe/London

## Programme status

- Authoritative progress ledger: **62/67 complete**.
- Items 58, 59, 60, 61 and 62 are **COMPLETE**.
- **Item 63 is ACTIVE — recover the blind adjudication after quarantining the invalid first Stage-A attempt, then scientifically interpret the 24 frozen P2 outputs.**
- Items 64–67 remain pending.
- Fresh accepted P2 experimental units: **24**.
- Fresh scheduled P2 units with genuine model activity: **24/24**.
- Accepted Item-63 blinded correctness adjudications: **0/24**.
- Real sealed-verifier diagnostic executions during the invalid Item-63 attempt: **1**, quarantined and not accepted as a blind adjudication.
- P2 fresh execution completed: **TRUE**.
- P2 output freeze completed: **TRUE**.
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
- full-block blindness through Item 62
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

## Item 61 v3 runtime repair — accepted

The exact Codex runtime was isolated under `C:\Kyntic\ras-p2-experimental-runtime-v2`.

Accepted facts:

- exact CLI: `codex-cli 0.153.0-alpha.5`
- exact model: `gpt-5.6-luna`
- restricted identity: `DESKTOP-BFTREBH\ras-p2-experimental`
- administrator: **FALSE**
- elevated: **FALSE**
- runtime depends on coordinator-profile paths: **FALSE**
- protected private/coordinator roots remain denied
- experimental workspace remains usable

Accepted v3 identities:

- execution-lock manifest: `A0A8D89CDC226EE5619C9AA0BE80F936EC84B6218EA14E84F992B650699844DD`
- execution-lock contents manifest: `C774396F9F56DD94CFE0194E2916F891CF5D9CF6DD29D63F6E97AE48A9FBFC73`
- execution-lock package: `908CCB709B08379E616EF62C04B996DB7A526ED91BB66E73491CDE3D8C377D99`

The earlier v2 execution lock and runtime-access falsification remain preserved as history.

## Item 62 execution — accepted

The fresh locked 24-run P2 block completed with all outputs frozen before any correctness adjudication.

Accepted execution facts:

- scheduled units: **24**
- final frozen unit records: **24**
- model-active units: **24**
- workspace gates passed: **24/24**
- schedule order changed: **FALSE**
- unscheduled executions: **0**
- model substitutions: **0**
- A chains: **3**
- A new T01 sessions: **3**
- A expected resumes: **9**
- A successful resumes: **9**
- A cross-repetition session reuse: **0**
- B fresh sessions: **12**
- B resumes: **0**
- generated code carry: **FALSE**
- pre-model infrastructure retries: **3**
- post-model quality retries: **0**
- best-of-N: **FALSE**
- human rescue: **FALSE**
- hidden verifier runs during execution: **0**
- correctness adjudications during execution: **0**
- condition mapping remained sealed: **TRUE**

The UAC/sandbox defect was repaired under the frozen recovery rule: seven already model-active units were preserved and never rerun; subsequent failed slot-8 attempts were pre-model only and were retried legally after switching to the supported `unelevated` sandbox configuration.

Accepted Item-62 identities:

- execution manifest: `334EFF9B6F85AE92766DEC6EF3AEF562F62E97C2DCC8E09C80E6BE5743F1FDBC`
- output-freeze manifest: `2A27C6110E99D712D99D1680B58F568512301B866A78E802C5D79D933414BC4E`
- execution package: `31898756356B676CB76F7D67596DE206B902659B5E8D58E5A4620250F55607C1`

All Item-62 hashes repeat and package internal bindings validate.

Public evidence:

- `results/public/subject-b-p2-item62-output-freeze-v3.json`
- `results/public/subject-b-p2-item62-output-freeze-v3.md`

## Item 63 first attempt — invalid and quarantined

The first Item-63 Stage-A worker used coordinator-side placeholder verifier entrypoints for its initial 24 calls. Those calls produced no correctness adjudication output and are not accepted as blinded adjudications.

The worker then unblinded the mapping before discovering the path mismatch and made one diagnostic call to the real sealed verifier. That diagnostic call occurred after condition information was available, so it is quarantined and cannot be accepted as a blind Stage-A adjudication.

The Item-62 experiment remains intact:

- frozen candidates modified: **0**
- frozen candidates rerun: **0**
- task-solving model runs during Item 63: **0**
- accepted blind adjudications from failed attempt: **0**
- real diagnostic verifier calls: **1**, excluded

Public falsification evidence:

- `results/public/subject-b-p2-item63-blind-adjudication-falsification-v1.json`
- `results/public/subject-b-p2-item63-blind-adjudication-falsification-v1.md`

## Active Item 63 recovery

Preserve and quarantine the entire failed Item-63 attempt. Do not reuse its Stage-A records, unblinding analysis or diagnostic correctness output.

Recovery rules:

- do not execute, regenerate or modify any Item-62 experimental unit;
- use the unchanged 24 frozen candidates and unchanged sealed qualified semantic verifier;
- construct a neutral blind-ID-only adjudication bundle with candidate locations/names that reveal no A/B condition, repetition-condition mapping or condition-named workspace path;
- run accepted Stage A through a scoring process whose accessible inputs exclude the blind-to-condition mapping and condition labels;
- the scoring process may know blind ID and task only;
- freeze exactly 24 accepted blinded adjudication records before any accepted unblinding;
- the previous diagnostic verifier result is excluded even if numerically identical to the fresh blind result;
- document the real verifier execution count transparently: the quarantined diagnostic call plus the accepted blind calls;
- after the fresh Stage-A package is frozen, perform one accepted unblinding and matched analysis from those frozen records only;
- analyse the 12 matched task × repetition units under the frozen methodology;
- keep resource telemetry separate from correctness;
- use bounded claims only;
- do not begin Item 64 until coordinator acceptance of Item 63.

## Contaminated historical Item-62 attempt

The earlier same-user contaminated Item-62 attempt remains permanently excluded. Never reuse or inspect its session, code, candidate, output, correctness, schedule, blind mapping or execution lock.
