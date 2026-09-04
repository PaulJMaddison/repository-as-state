# Repository-as-State — CURRENT

Updated: 2026-09-04 12:20 Europe/London

## Programme status

- Authoritative progress ledger: **61/67 complete**.
- Item 58 is **COMPLETE**: corrected Subject-B P2 Level-2 design frozen at **4 tasks × 3 repetitions × 2 conditions = 24 runs**.
- Item 59 is **COMPLETE**: corrected four-task selection and 13 neutral disclosed governing behaviours frozen.
- Item 60 is **COMPLETE**: source-only semantic hidden verifiers qualified and privately frozen.
- Item 61 is **COMPLETE**: final preregistration/runtime/prompts/randomisation/public binding/zero-model execution lock accepted.
- **Item 62 is ACTIVE — controlled 24-run P2 execution.**
- P2 preregistered: **TRUE**.
- P2 executed: **FALSE**.
- P2 experimental agent runs at item-61 lock: **0**.
- P2 task-solving model invoked at item-61 lock: **FALSE**.
- Model completions at item-61 lock: **0**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Authoritative P2 corpus and design

Final chronological candidates:

`C07 → C08 → C09 → C10`

V2 mapping:

- `P2V2_T01 = C07`
- `P2V2_T02 = C08`
- `P2V2_T03 = C09`
- `P2V2_T04 = C10`

Final governing behaviour counts: **2 + 3 + 4 + 4 = 13**.

Historical `P2_T02_B02` is removed as an over-curated non-delta with no replacement. C06 remains ineligible.

Accepted Level-2 design:

**4 tasks × 3 repetitions × 2 conditions = 24 runs**.

- A: three mutually independent persistent-session chains, each `T01 → T02 → T03 → T04` = 12 runs
- B: 12 fresh mutually independent sessions
- primary matched unit: task × repetition
- matched units: 12
- fresh exact PRE every experimental unit
- generated implementation never carries between runs/tasks
- A continuity is exact reasoning/session continuity only
- repetitions are independent replications, not retries
- full-block blindness: all 24 outputs frozen before hidden correctness adjudication
- resource telemetry remains separate from correctness
- no human rescue
- no post-activity model-quality retry
- descriptive replication only
- formal equivalence/non-inferiority unsupported
- complexity limitation: 3 LOW / 1 MEDIUM / 0 HIGH

## Item-58 identities

- design repair: `D4CCB92E84CC8112EF304E1A674F5E6D98185CD0B212390514B49563632311A4`
- invariant audit: `E7D6D969B24F7158DEADE121DEB91352DDFFCB32AF06E7C5752BA81B74FF6BD1`
- design freeze: `782ADD46591FCCDCABB796D25DC3BE71B03627FCC082372B1FD018875DE1248A`
- design package: `C5124105BD1701A2336211776AF1E3D7E1ED98270665ABAA39910385B81C41F3`

## Item-59 identities

- task-selection freeze: `02025A0BBE6913DB280F0E830F4E5932729910C7FCD3150DCC551F8AFA1283DA`
- contract-repair manifest: `2FB6FAE1FAEC520CC2CEC2BDD0A56E3834E9475FF26724E8919C871EE74BD973`
- final contract-history audit: `22BB4E333C78C1FC02F189994F207AA67B669A58DEDA58258E1D32B1D7C1D911`
- curation package: `FC6CFDAEF1B5599FE2242C88B1B82985D423F4F64732497F65FAFD3BFAD8C867`
- item-59 freeze: `FE254B6786D9F800674B88576A99336EA118784481FD8252CC76BEE8F102A9E9`

All four task fairness audits pass. Undisclosed, future-history, verifier-only and implementation-specific governing requirements are zero. All 13 behaviours are PRE=false / POST=true under the accepted contract-history audit.

## Item-60 semantic hidden-verifier identities

- semantic verifier manifest: `B2526D4AC1B8FE5D88E373B6728E1A6A64C260303A3E9F41D2F1CE1924268034`
- semantic seam manifest: `18B72556F1F0BBE22C77F64708C5222C14E90D5C06C4DEDDBF1F18DFD86F64EC`
- negative-control manifest: `E683673C1AE090F5385FA64398AC20F4FFC7B93FC23DEC7C06424945D8D835AA`
- alternate-valid qualification: `DF3C9EBC74F039AA13740E97D75B251F93A170C835AB32197C8C098785B138AA`
- determinism audit: `3C3934EA95AAFF202DF27EEA10A690F8388C13A9978F0092638E3BDBB281734A`
- qualification summary: `230EBC784773BC35771533305F7588000BCDB490EC7FA56CCD5D541933FFD22A`
- verifier freeze: `EF4DEAFBD34E3411C316241AB02A1F19C14A852031B722BAB75CC8DAB97553E1`
- verifier package: `D3C77EDE2D3B41716035F0EEB5977F69898D97C46D9015E4C74C61EA244FDD48`

Qualification: historical PRE fail / POST pass on all four tasks; 13/13 negative controls detected; 13/13 alternate-valid controls accepted; zero false-positive decoys; implementation-independence audit complete; 24 repeated historical verifier vectors deterministic; C10 prior seam defects reintroduced 0; hidden verifier private and inaccessible to experimental agents; build/test/restore/compiler commands 0.

## Item 61 final preregistration and execution lock — accepted

Final worker terminal:

`VALID_TERMINAL_A_ITEM61_FINAL_EXECUTION_LOCKED`

### Model/runtime

- exact model: `gpt-5.6-luna`
- Codex CLI: `0.153.0-alpha.5`
- execution-relevant effective Codex configuration identity: `8249A208C5DED9B173BBC6B22B8EA6E1A11AB8E29BFF4B7B006A396BF8FA0093`
- runtime-manifest SHA-256: `4FC602F42CA6974BFF0AC13AA4D06FF8FA0831790398F05D55EEFBCB66239674`
- raw `config.toml` SHA observed during Phase B: `B321C224F46DCE5C01F500AD813D626D34513738F446644450D0A4D1DF16DF1E`
- runtime drift: **FALSE**
- timeout: **1800 seconds**

### Phase-A private preregistration identities

- model binding: `5F50ED53B7627253DF5814CA3FE157E52E45B1D21514B9C7D00953A56F398397`
- prompt manifest: `36EE1B1FC458D37821F1805B6E0FEC9AAC12C0BB4A0E1754CFDA22E11E7A2879`
- randomisation manifest: `CEC19FC3891F516F5AB57C47DC28BC427BB8B366A5D80C2FC7B359C975FA1428`
- experimental-unit manifest: `FD47BCF1A81066CF3DD80C240B5C5A1B62D177A1A831B66848FC86D068CE9681`
- blind-ID mapping: `A100F2AA35CBFDB59CC6D5FBD6AB0B7CDFFF83577AB81952F25812DAEA8F09FE`
- PRE-workspace manifest: `C059081C3228C72644E546A14833F339CF9E9211C12037C0196D8C819CF670E3`
- execution-command templates: `38435B615C38264DF1E888159FB7F830CEE0B0956CD5125DA469AC6DB1B9B8F4`
- pre-model readiness audit: `DF99C3B064C7FD3D6E857BA1C15F92A959BAAA23A886819EB3B239B70E24259B`
- preregistration manifest: `221E19675EFAFB37E96FA4950D178BE729C27D16D3B4C955D4DBCBABA2DFCF48`
- preregistration package: `86EAF3411A89D45F3563D7CD64411C0F9927FC5CE5815DB4ECFBA7B0C6DC5F59`

### Corrected public preregistration binding

Original erroneous publication is preserved in Git history.

Execution-authoritative corrected two-file public commitment:

- commit: `a3da5fb11df577034ef364c4790deb170ef37f77`
- corrected JSON blob: `e4f8419238c336833ee5aec306f0734406091ada`
- corrected binding matches frozen Phase-A private commitments: **TRUE**
- republication required: **FALSE**

### Final pre-execution integrity

- prompts unchanged: **TRUE**
- randomisation regenerated: **FALSE**
- randomisation manifest unchanged: **TRUE**
- schedule unchanged: **TRUE**
- blind mapping unchanged/sealed: **TRUE**
- PRE workspaces present: **24/24**
- PRE workspaces clean: **24/24**
- PRE workspaces future-history safe: **24/24**
- PRE workspaces hidden-verifier-free: **24/24**
- PRE workspaces sealed-mapping-free: **24/24**
- persistent-session exact resume mechanism valid: **TRUE**
- fresh workspace on session resume supported: **TRUE**
- hidden verifier private: **TRUE**
- experimental-agent access to hidden verifier: **FALSE**
- experimental-agent access to sealed mapping: **FALSE**
- pre-existing P2 outputs: **0**
- pre-existing P2 correctness results: **0**
- pre-existing P2 task sessions: **0**
- stale P2 experimental processes: **0**

### Final execution-lock identities

- public-binding audit: `D02218A1206BF2C7B2CC4730523D48E99EF02E949C608FB9CCA160DD8D747E41`
- Phase-A integrity audit: `816388AC58FE331CC3924F4DE21F051410B22419A6B514FB04DD4658A78284FC`
- final zero-model gate: `8344F950C7AF7820C088C2761194FDAA6F0F4780D9590F397B5B644E3063DFF3`
- execution-lock manifest: `3E3760D3B57C2BBA4D62B45B154C84633A44DB13025E618E66CE061C92924E9E`
- execution-lock freeze: `9FC8D4B6011BF5A7CDD5C956C0E08D105890AD345577A0A06488A1AA1F424890`
- execution-lock package: `CD8E28A9CAECEFF95B666FD19BD7CB64D19D71F93401CCEBA1C5DC60520AA3C6`

All six execution-lock hashes are 64-character SHA-256 values, repeat checks match, and package internal bindings validate.

### Final zero-model gate

At lock freeze:

- model completions generated: **0**
- P2 experimental agent runs: **0**
- P2 task-solving model invoked: **FALSE**
- P2 executed: **FALSE**
- hidden-verifier experimental adjudications: **0**

Private randomisation seed, schedule, blind-condition mapping and hidden verifier remain sealed.

Public-safe evidence:

- `results/public/subject-b-p2-preregistration-binding-v1.json/.md`
- `results/public/subject-b-p2-execution-lock-v1.json/.md`

## Item 62 active gate

Execute exactly the **24 frozen experimental units** in the already-frozen private schedule.

Execution must obey the item-61 lock without modification:

- exact `gpt-5.6-luna`
- exact frozen runtime/effective configuration
- exact canonical prompt bytes
- A persistent-session chains and B fresh sessions exactly as preregistered
- exact private schedule
- one attempt per experimental unit
- no human rescue or mid-run prompt injection
- no model-quality retry
- exact 1800-second timeout
- fresh frozen PRE workspace per unit
- no generated-code carry
- collect frozen resource telemetry only; **do not run the hidden correctness verifier during execution**
- freeze every candidate output
- all 24 output freezes must exist before item 63 hidden adjudication

If an infrastructure issue occurs before genuine model activity, only the preregistered infrastructure-only repair policy applies. After genuine model activity, do not replace the session or rerun for model quality.

## Remaining gates

62. Execute accepted 24-run P2 same-repository replication — **ACTIVE**.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish Level-2 P2 evidence and update paper claims/evidence.
65. Select Subject C and perform cross-repository / Level-3 replication.
66. Final hostile review, statistical/claims/limitations and reproducibility audit.
67. Final paper + reproducibility package + submission-ready release.

## Coordinator/Codex rule

Persist authoritative state; reconstruct computation. Item 62 must execute the frozen protocol exactly. No correctness information may be released until all 24 output states are frozen.
