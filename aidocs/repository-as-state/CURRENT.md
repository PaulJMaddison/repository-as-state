# Repository-as-State — CURRENT

Updated: 2026-09-05 18:15 Europe/London

## Programme status

- Authoritative progress ledger: **63/67 complete**.
- Items 58, 59, 60, 61, 62 and 63 are **COMPLETE**.
- **Item 64 is ACTIVE — publish the Level-2 P2 evidence and update the paper claims/evidence to reflect the accepted floor-effect result.**
- Items 65–67 remain pending.
- Fresh accepted P2 experimental units: **24**.
- Fresh scheduled P2 units with genuine model activity: **24/24**.
- Accepted Item-63 blinded correctness adjudications: **24/24**.
- P2 fresh execution completed: **TRUE**.
- P2 output freeze completed: **TRUE**.
- P2 blind adjudication completed: **TRUE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.
- P2 task rerun: **FALSE**.

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

Public evidence:

- `results/public/subject-b-p2-item62-output-freeze-v3.json`
- `results/public/subject-b-p2-item62-output-freeze-v3.md`

## Item 63 blind adjudication and scientific interpretation — accepted

The first Item-63 Stage-A attempt remains permanently quarantined. Its 24 coordinator-side placeholder calls produced no valid adjudication output, and its one real sealed-verifier diagnostic call occurred after premature unblinding and is excluded from accepted correctness evidence.

The accepted recovery used a new neutral blind-ID-only candidate bundle and the unchanged qualified semantic verifier package.

Accepted recovery integrity:

- frozen Item-62 candidates: **24**
- candidates rerun: **0**
- candidates modified: **0**
- accepted blind adjudications: **24/24**
- unique blind IDs: **24**
- accepted recovery real-verifier runs: **24**
- quarantined real-verifier diagnostic runs: **1**
- total real sealed-verifier executions across Item 63: **25**
- condition information used during accepted Stage-A scoring: **FALSE**
- accepted Stage A frozen before accepted unblinding: **TRUE**
- additional task-model runs during Item 63: **0**
- verifier changed: **FALSE**

A derived denominator defect was found after the first recovery report. It was repaired using the already-frozen Stage-A records and accepted unblinding only; no verifier/model/candidate rerun occurred and all frozen Stage-A evidence remained byte-identical.

### Accepted P2 correctness result

- behaviour observations per condition: **39**
- Condition A behaviours satisfied: **0/39**
- Condition B behaviours satisfied: **0/39**
- Condition A behaviours failed: **39/39**
- Condition B behaviours failed: **39/39**
- matched behaviour agreements: **39**
- matched behaviour disagreements: **0**
- disagreements favouring A: **0**
- disagreements favouring B: **0**
- Condition A candidate overall passes: **0/12**
- Condition B candidate overall passes: **0/12**

Scientific interpretation:

> No behavioural correctness difference was observed between the persistent-session and fresh-session conditions in P2: both conditions satisfied 0 of 39 evaluated behaviour observations, with 39 matched agreements and no disagreements.

This is a **floor-effect result**. It does not demonstrate successful behavioural preservation by either condition and cannot by itself be interpreted as evidence of behavioural equivalence or repository-state sufficiency.

P1 remains contextual and is not pooled into P2. P1 observed A=18/30 and B=18/30 with 30 agreements and 0 disagreements. P2 observed equal zero behavioural performance, so P2 provides no positive evidence that either condition successfully solved the four Level-2 tasks.

Accepted Item-63 identities:

- recovery blind manifest: `CD181156AA2CAC4B38ADDBFCD88674CDF48248D9FA7C3A386C09239CB2648822`
- recovery Stage-A package: `1EBE21C62D8CCB2814FC42D14E4F9B698079110AE793CD3659164F0FC99D991D`
- matched analysis: `8D22F6B75421F8263C8E9DA065CE31761F7527D4DD1035F357F925E6D2629F33`
- scientific interpretation: `8983393D51B3BDD53162B610D98C1BADD7C4157E08E02DE72B1541E2E36E9A1B`
- final package: `EECB0F2682B376D5BB0EC856D63164081B0F7C41B9332E5C359F5047A9B85681`

Public evidence:

- `results/public/subject-b-p2-item63-results-v2.json`
- `results/public/subject-b-p2-item63-results-v2.md`
- `results/public/subject-b-p2-item63-blind-adjudication-falsification-v1.json`
- `results/public/subject-b-p2-item63-blind-adjudication-falsification-v1.md`

## Active Item 64

Publish the complete Level-2 P2 evidence narrative and update the research paper/evidence/claims surfaces so they accurately represent both P1 and P2.

Required claim discipline:

- retain the P1 bounded result exactly;
- retain the P2 floor-effect result exactly;
- do not describe P2 as equivalence, non-inferiority, successful preservation, or proof of Repository-as-State sufficiency;
- distinguish `no observed A/B difference` from `successful task performance`;
- preserve the Item-63 recovery/falsification history;
- keep resource claims separate from correctness claims;
- do not begin Subject C / Item 65 until Item 64 is coordinator-accepted.

## Contaminated historical Item-62 attempt

The earlier same-user contaminated Item-62 attempt remains permanently excluded. Never reuse or inspect its session, code, candidate, output, correctness, schedule, blind mapping or execution lock.
