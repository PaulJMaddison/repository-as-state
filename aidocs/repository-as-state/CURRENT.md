# Repository-as-State — CURRENT

Updated: 2026-09-04 12:40 Europe/London

## Programme status

- Authoritative progress ledger: **59/67 complete**.
- Items 58 and 59 remain **COMPLETE**.
- **Item 60 is REOPENED / ACTIVE for hidden-material isolation only.** The 13 source-only semantic verifier behaviours, negative controls, alternate-valid qualification, determinism and semantic freeze remain accepted; the previously accepted claim that the experimental agent could not access hidden verifier material has been falsified by live item-62 execution.
- Item 61 is **NO LONGER COMPLETE / BLOCKED**. Its preregistration and execution lock depended on the now-falsified hidden-material isolation claim and cannot be reused for a new experiment.
- Item 62 is **BLOCKED**. The current execution instance is abandoned.
- Item 63+ remain pending.
- P2 accepted experimental units completed: **0**.
- P2 units with genuine model activity before blocker: **1**.
- P2 correctness adjudications: **0**.
- Hidden verifier executions against experimental candidates: **0**.
- Correctness-related private information was exposed to the contaminated experimental session: **TRUE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Authoritative corpus/design that remain unchanged

Final candidates/order:

`C07 → C08 → C09 → C10`

V2 mapping:

- `P2V2_T01 = C07`
- `P2V2_T02 = C08`
- `P2V2_T03 = C09`
- `P2V2_T04 = C10`

Final governing behaviours: **13** (`2 + 3 + 4 + 4`). Historical `P2_T02_B02` remains removed as an over-curated non-delta with no replacement. C06 remains ineligible.

Accepted Level-2 design remains:

**4 tasks × 3 repetitions × 2 conditions = 24 runs**.

- A: three mutually independent persistent-session chains, each `T01 → T02 → T03 → T04`
- B: 12 fresh independent sessions
- matched task×repetition units: 12
- fresh exact PRE every unit
- generated implementation never carries between units
- A continuity is reasoning/session continuity only
- repetitions are replications, not retries
- full-block blindness
- no human rescue
- no post-activity model-quality retry
- descriptive replication only

## Accepted item-58 identities

- design repair: `D4CCB92E84CC8112EF304E1A674F5E6D98185CD0B212390514B49563632311A4`
- invariant audit: `E7D6D969B24F7158DEADE121DEB91352DDFFCB32AF06E7C5752BA81B74FF6BD1`
- design freeze: `782ADD46591FCCDCABB796D25DC3BE71B03627FCC082372B1FD018875DE1248A`
- design package: `C5124105BD1701A2336211776AF1E3D7E1ED98270665ABAA39910385B81C41F3`

## Accepted item-59 identities

- task-selection freeze: `02025A0BBE6913DB280F0E830F4E5932729910C7FCD3150DCC551F8AFA1283DA`
- contract-repair manifest: `2FB6FAE1FAEC520CC2CEC2BDD0A56E3834E9475FF26724E8919C871EE74BD973`
- final contract-history audit: `22BB4E333C78C1FC02F189994F207AA67B669A58DEDA58258E1D32B1D7C1D911`
- curation package: `FC6CFDAEF1B5599FE2242C88B1B82985D423F4F64732497F65FAFD3BFAD8C867`
- item-59 freeze: `FE254B6786D9F800674B88576A99336EA118784481FD8252CC76BEE8F102A9E9`

## Item 60 semantic verifier state — semantics accepted, isolation reopened

Accepted verifier identities remain historical/technical evidence:

- semantic verifier manifest: `B2526D4AC1B8FE5D88E373B6728E1A6A64C260303A3E9F41D2F1CE1924268034`
- semantic seam manifest: `18B72556F1F0BBE22C77F64708C5222C14E90D5C06C4DEDDBF1F18DFD86F64EC`
- negative-control manifest: `E683673C1AE090F5385FA64398AC20F4FFC7B93FC23DEC7C06424945D8D835AA`
- alternate-valid qualification: `DF3C9EBC74F039AA13740E97D75B251F93A170C835AB32197C8C098785B138AA`
- determinism audit: `3C3934EA95AAFF202DF27EEA10A690F8388C13A9978F0092638E3BDBB281734A`
- qualification summary: `230EBC784773BC35771533305F7588000BCDB490EC7FA56CCD5D541933FFD22A`
- verifier freeze: `EF4DEAFBD34E3411C316241AB02A1F19C14A852031B722BAB75CC8DAB97553E1`
- verifier package: `D3C77EDE2D3B41716035F0EEB5977F69898D97C46D9015E4C74C61EA244FDD48`

The semantic qualification itself remains strong: PRE fail / POST pass on all four tasks; 13/13 negative controls detected; 13/13 alternate-valid controls accepted; false-positive decoys 0; 24 repeated historical vectors deterministic; no build/test/restore/compiler gates.

However, item 60 also required:

`EXPERIMENTAL_AGENT_ACCESS_TO_HIDDEN_VERIFIER=FALSE`

Live item-62 execution falsified that claim. Therefore item 60 is reopened specifically to repair and prove the actual OS/runtime access boundary using the real experimental identity.

## Superseded item-61 execution lock

The previous item-61 lock was correctly created before model activity, but it is no longer execution-authoritative because it bound a false hidden-material isolation claim.

Historical lock identities are retained for audit:

- public-binding audit: `D02218A1206BF2C7B2CC4730523D48E99EF02E949C608FB9CCA160DD8D747E41`
- Phase-A integrity audit: `816388AC58FE331CC3924F4DE21F051410B22419A6B514FB04DD4658A78284FC`
- final zero-model gate: `8344F950C7AF7820C088C2761194FDAA6F0F4780D9590F397B5B644E3063DFF3`
- execution-lock manifest: `3E3760D3B57C2BBA4D62B45B154C84633A44DB13025E618E66CE061C92924E9E`
- execution-lock freeze: `9FC8D4B6011BF5A7CDD5C956C0E08D105890AD345577A0A06488A1AA1F424890`
- execution-lock package: `CD8E28A9CAECEFF95B666FD19BD7CB64D19D71F93401CCEBA1C5DC60520AA3C6`

Do **not** resume item 62 under this lock and do **not** retry the contaminated slot.

## Item-62 isolation failure — authoritative

Worker terminal:

`VALID_TERMINAL_B_ITEM62_EXECUTION_METHODOLOGY_BLOCKER`

Observed state:

- accepted units completed: **0**
- units started with genuine model activity: **1**
- units not executed: **23**
- active process terminated after breach confirmation: **TRUE**
- hidden verifier runs: **0**
- partial correctness adjudications: **0**
- correctness-related private information exposed to the experimental session: **TRUE**
- existing completed units remain valid: **FALSE** (there are zero accepted completed units)

Exact methodological failure: the experimental task-solving agent could read private item-60 hidden-verifier / qualification material through paths outside the candidate workspace after genuine model activity had begun.

Preserved private evidence:

- contaminated event log SHA-256: `CB8CB6A38424A4D8BFADDAFCCB943BF600775F727A00B9FD7EC51DB03026CBCA`
- partial candidate manifest SHA-256: `7E72A6004BA07C43A61765E84CC6A3A43CAB445B0945516587DDCF03B0DA31D3`

Public-safe evidence:

- `results/public/subject-b-p2-item62-hidden-material-isolation-blocker-v1.json`
- `results/public/subject-b-p2-item62-hidden-material-isolation-blocker-v1.md`

## Scientific ruling

The contaminated attempt is **not** an ordinary failed run and is not part of the 24-run evidence set.

It may not be retried selectively under the existing preregistration because genuine model activity occurred and private correctness-related material was exposed.

The entire current execution instance is abandoned. The next valid path is:

1. repair hidden-material isolation without changing item-59 task contracts or item-60 semantic behaviour logic;
2. prove isolation against the actual experimental execution identity/process, including explicit deny/read-failure tests for private verifier, qualification, sealed mapping and methodology roots;
3. freeze a repaired item-60 isolation package;
4. create a **fresh item-61 preregistration/public commitment/execution lock** after the repair;
5. use a newly committed deterministic randomisation instance that cannot be selected based on model outcome; preserve the 4×3×2 design and all substantive task/model rules unless a methodology review proves another change is required;
6. only then begin a new item-62 execution from zero accepted units.

No correctness result from the contaminated attempt may be used to choose the reset schedule, prompts, model, tasks, repetitions or conditions.

## Remaining gates

60. Repair/prove hidden-verifier isolation against actual experimental identity — **ACTIVE / REOPENED**.
61. Fresh post-repair preregistration/public binding/execution lock — **BLOCKED**.
62. Fresh controlled 24-run execution — **BLOCKED**.
63. Blind adjudication and scientific interpretation — pending.
64. Publish Level-2 evidence/update paper — pending.
65. Subject C / Level-3 replication — pending.
66. Final hostile review/statistics/claims/reproducibility audit — pending.
67. Final paper/repro package/submission-ready release — pending.

## Coordinator/Codex rule

Persist authoritative state; reconstruct computation. The isolation breach is evidence that the previous boundary was insufficient. Repair the boundary; do not reinterpret the contaminated model attempt as an experimental result and do not continue the old execution schedule.
