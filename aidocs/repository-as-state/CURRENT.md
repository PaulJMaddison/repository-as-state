# Repository-as-State — CURRENT

Updated: 2026-09-04 11:09 Europe/London

## Programme status

- Authoritative progress ledger: **60/67 complete**.
- Item 58 is **COMPLETE**: corrected Subject-B P2 Level-2 design frozen at **4 tasks × 3 repetitions × 2 conditions = 24 runs**.
- Item 59 is **COMPLETE**: corrected four-task execution-authoritative selection and neutral disclosed contracts are frozen.
- Item 60 is **COMPLETE**: source-only semantic hidden verifiers for all 13 final behaviours are implemented, qualified and privately frozen.
- **Item 61 is ACTIVE**: freeze final P2 preregistration, exact model/runtime/prompts/randomisation/execution lock with zero P2 task-solving model runs.
- P2 experimental agent runs: **0**.
- P2 task-solving model invoked: **FALSE**.
- P2 executed: **FALSE**.
- P2 preregistered: **FALSE** until item 61 is accepted.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Corrected P2 corpus and design — authoritative

Final candidates in chronological order:

`C07 → C08 → C09 → C10`

V2 execution mapping:

- `P2V2_T01 = C07`
- `P2V2_T02 = C08`
- `P2V2_T03 = C09`
- `P2V2_T04 = C10`

Final governing behaviour counts:

- C07: **2**
- C08: **3**
- C09: **4**
- C10: **4**
- total: **13**

Historical `P2_T02_B02` is removed as an over-curated non-delta and has no replacement. C06 remains ineligible and excluded.

Accepted Level-2 design:

**4 tasks × 3 repetitions × 2 conditions = 24 runs**.

- Condition A: 3 mutually independent persistent-session chains × 4 chronological tasks = 12 runs
- Condition B: 12 fresh mutually independent sessions
- primary matched unit: task × repetition
- matched units: 12
- fresh exact PRE every run
- generated implementation never carries between runs/tasks
- Condition-A continuity is reasoning/session continuity only
- repetitions are independent replications, not retries
- full-block blindness requires all 24 outputs to be frozen before hidden correctness release
- durable resource telemetry remains separate from correctness
- no-human-rescue and no post-activity model-quality retry remain authoritative
- interpretation remains descriptive replication
- formal equivalence and formal non-inferiority remain unsupported
- complexity limitation: 3 LOW / 1 MEDIUM / 0 HIGH

## Accepted item-58 identities

- design repair v2: `D4CCB92E84CC8112EF304E1A674F5E6D98185CD0B212390514B49563632311A4`
- invariant audit v2: `E7D6D969B24F7158DEADE121DEB91352DDFFCB32AF06E7C5752BA81B74FF6BD1`
- design freeze v2: `782ADD46591FCCDCABB796D25DC3BE71B03627FCC082372B1FD018875DE1248A`
- design package v2: `C5124105BD1701A2336211776AF1E3D7E1ED98270665ABAA39910385B81C41F3`

## Accepted item-59 identities

- task-selection freeze v2: `02025A0BBE6913DB280F0E830F4E5932729910C7FCD3150DCC551F8AFA1283DA`
- contract-repair manifest v2: `2FB6FAE1FAEC520CC2CEC2BDD0A56E3834E9475FF26724E8919C871EE74BD973`
- final contract-to-history audit v2: `22BB4E333C78C1FC02F189994F207AA67B669A58DEDA58258E1D32B1D7C1D911`
- curation package v2: `FC6CFDAEF1B5599FE2242C88B1B82985D423F4F64732497F65FAFD3BFAD8C867`
- item-59 freeze v2: `FE254B6786D9F800674B88576A99336EA118784481FD8252CC76BEE8F102A9E9`

All four task fairness audits pass. Undisclosed, future-history, verifier-only and implementation-specific governing requirements are all zero. All 13 final behaviours are PRE=false / POST=true under the accepted contract-history audit.

## Accepted item-60 semantic hidden-verifier qualification

Terminal state:

`VALID_TERMINAL_A_ITEM60_SEMANTIC_VERIFIERS_QUALIFIED`

The source-only verifier package covers exactly the four execution-authoritative tasks and 13 frozen governing behaviours.

Historical qualification:

- P2V2_T01: PRE fail / POST pass
- P2V2_T02: PRE fail / POST pass
- P2V2_T03: PRE fail / POST pass
- P2V2_T04: PRE fail / POST pass

Qualification gates:

- all governing behaviours implemented: **13/13**
- arbitrary candidate repository root supported: **TRUE**
- commit identity used as verdict: **FALSE**
- historical source hash used as verdict: **FALSE**
- negative controls detected: **13/13**
- false-positive decoys accepted as pass: **0**
- implementation-independence audit complete: **TRUE**
- unjustified historical implementation coupling: **0**
- alternate-valid controls accepted: **13/13**
- verifier self-tests: **PASS**
- self-test fixtures used as candidate correctness evidence: **FALSE**
- determinism runs per historical control: **3**
- total historical determinism invocations: **24**
- all repeated verdict vectors deterministic: **TRUE**
- C10 previous oracle-mapping defects reintroduced: **0**
- hidden verifier private: **TRUE**
- experimental-agent access to hidden verifier: **FALSE**
- item-59 contract bytes unchanged: **TRUE**
- item-59 freeze identity unchanged: **TRUE**

Absolute item-60 prohibition was respected:

- build commands: **0**
- test commands: **0**
- restore commands: **0**
- compiler commands: **0**
- P2 experimental agent runs: **0**
- P2 task-solving model invoked: **FALSE**

Accepted item-60 private identities:

- semantic verifier manifest: `B2526D4AC1B8FE5D88E373B6728E1A6A64C260303A3E9F41D2F1CE1924268034`
- semantic seam manifest: `18B72556F1F0BBE22C77F64708C5222C14E90D5C06C4DEDDBF1F18DFD86F64EC`
- negative-control manifest: `E683673C1AE090F5385FA64398AC20F4FFC7B93FC23DEC7C06424945D8D835AA`
- alternate-valid qualification: `DF3C9EBC74F039AA13740E97D75B251F93A170C835AB32197C8C098785B138AA`
- determinism audit: `3C3934EA95AAFF202DF27EEA10A690F8388C13A9978F0092638E3BDBB281734A`
- qualification summary: `230EBC784773BC35771533305F7588000BCDB490EC7FA56CCD5D541933FFD22A`
- verifier freeze: `EF4DEAFBD34E3411C316241AB02A1F19C14A852031B722BAB75CC8DAB97553E1`
- verifier package: `D3C77EDE2D3B41716035F0EEB5977F69898D97C46D9015E4C74C61EA244FDD48`

All item-60 SHA-256 identities are 64 hex characters with repeat matches, and the verifier package internal bindings validate.

Public-safe evidence:

- `results/public/subject-b-p2-semantic-verifier-qualification-v1.md`
- `results/public/subject-b-p2-semantic-verifier-qualification-v1.json`

## Item 61 active gate

Freeze the final execution-authoritative P2 preregistration and execution lock before any task-solving model invocation.

Item 61 must bind at minimum:

- exact accepted item-58 design and item-59/item-60 package identities;
- exact model identity `gpt-5.6-luna`; if unavailable, stop for methodology review and do not silently substitute;
- exact Codex CLI/runtime/toolchain identity;
- neutral prompt bytes derived only from the item-59 disclosed task contracts;
- prompt equality across A/B except for continuity mechanism outside the prompt;
- three independent persistent A chains in chronological task order;
- 12 independent fresh B sessions;
- random seed and final interleaving chosen and frozen before model activity while preserving chronological order within each A chain;
- fresh exact PRE workspace for every run;
- generated code never carries between runs or tasks;
- timeout and retry discipline;
- durable resource telemetry;
- full-block blindness and output-freeze rules;
- hidden verifier isolation and adjudication boundary;
- execution lock/public binding/final zero-model gate.

Item 61 must perform **zero P2 task-solving model runs**. No hidden correctness result may be exposed.

## Remaining gates

61. Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock — **ACTIVE**.
62. Execute accepted 24-run P2 same-repository replication.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish Level-2 P2 evidence and update paper claims/evidence.
65. Select Subject C and perform cross-repository / Level-3 replication.
66. Final hostile review, claims/statistics/limitations/reproducibility audit.
67. Final paper + reproducibility package + submission-ready release.

## Coordinator/Codex rule

Persist authoritative state; reconstruct computation. Items 58–60 are now frozen. Item 61 must freeze the execution protocol before any experimental model activity and must stop rather than silently substituting the model or changing the accepted treatment structure.
