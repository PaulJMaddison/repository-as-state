# Repository-as-State — CURRENT

Updated: 2026-09-04 10:20 Europe/London

## Programme status

- Authoritative progress ledger: **57/67 complete**.
- **Item 58 remains ACTIVE:** the corrected four-task 24-run Level-2 design has passed the substantive invariant audit, but the private Terminal-A freeze is not yet accepted because one reported SHA256 identity is malformed/truncated.
- Item 59 is **BLOCKED behind item 58**.
- Item 60 remains blocked behind item 59.
- P2 experimental agent runs: **0**.
- P2 task-solving model invoked: **FALSE**.
- P2 executed: **FALSE**.
- P2 preregistered: **FALSE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Absolute methodology rule

**NO BUILD, TEST, RESTORE OR COMPILER EXECUTION IS PERMITTED IN THE CURRENT P2 DESIGN / CONTRACT / ELIGIBILITY / VERIFIER METHODOLOGY WORK.**

Do not use whole-solution, targeted-project, minimal-project, probe or candidate build/test/compile outcomes as corpus, design, contract or verifier evidence.

## Corrected P2 corpus — accepted

The full ten-candidate eligibility re-audit remains accepted.

Corrected eligible set:

`C07, C08, C09, C10`

Corrected order:

`C07 → C08 → C09 → C10`

Corrected task total: **4**.

Corrected governing behaviours: **13**.

Corrected complexity:

- LOW: **3**
- MEDIUM: **1**
- HIGH: **0**

Eligibility re-audit SHA256:

`D55B610B6E2FFB1B032137F30C348FEFE9EF3542321720090C6690885D749E41`

C06 remains ineligible. C07 remains eligible with two genuine governing behaviours and `P2_T02_B02` removed as an over-curated non-delta. C08, C09 and C10 remain eligible.

## Item-58 substantive design result — provisionally valid

The latest privileged design worker returned:

`VALID_TERMINAL_A_ITEM58_DESIGN_REFROZEN`

Substantive result:

- corrected design: **4 tasks × 3 repetitions × 2 conditions = 24 runs**
- 18 original design invariants audited
- repetition count 3 remains independently justified
- Condition A: 3 mutually independent persistent-session chains × 4 chronological tasks = 12 runs
- Condition B: 12 fresh mutually independent sessions
- primary matched unit: task × repetition
- matched units: 12
- fresh exact PRE every run
- generated code never carries between runs/tasks
- A continuity is reasoning/session continuity only
- full-block blindness retained; 24 outputs required before hidden adjudication
- resource telemetry retained and separate from correctness
- pre-activity infrastructure-only repair principle retained
- no model-quality retry after genuine activity
- no-human-rescue retained
- pre-execution randomisation still required and deferred to item 61
- interpretation remains descriptive replication
- no formal non-inferiority or equivalence claim
- no task/sample/complexity manipulation
- build/test/compiler commands: 0
- P2 experimental runs: 0

Reported valid design identities:

- design repair: `D4CCB92E84CC8112EF304E1A674F5E6D98185CD0B212390514B49563632311A4`
- design freeze: `782ADD46591FCCDCABB796D25DC3BE71B03627FCC082372B1FD018875DE1248A`
- design package: `C5124105BD1701A2336211776AF1E3D7E1ED98270665ABAA39910385B81C41F3`

## Item-58 integrity blocker

The worker reported the invariant-audit identity as:

`E7D6D969B24F7152DDFFCB32AF06E7C5752BA81B74FF6BD1`

That value is only **48 hexadecimal characters**, not the 64 required for a SHA-256 digest, even though the worker also reported `P2_LEVEL2_INVARIANT_AUDIT_V2_REPEAT_MATCH=TRUE`.

Therefore the coordinator does **not** yet accept the item-58 freeze.

This is a narrow artifact-identity blocker, not a substantive design failure. The next worker must inspect the actual private `P2-LEVEL2-INVARIANT-AUDIT-v2.json`, recompute its full SHA256 twice, and verify all dependent freeze/manifest/package references. If the malformed value exists only in the terminal response, return the correct 64-character identity without changing the package. If any frozen artifact contains the malformed/truncated identity internally, regenerate every dependent deterministic artifact and return their new full hashes.

Do not re-run the design analysis unless an internal binding inconsistency actually requires it.

## Historical evidence retained

Historical design-input manifest:

`D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`

Historical task-selection freeze:

`829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`

Historical private curation package:

`5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

Accepted contract-to-history audit:

`4A57493EC8B70732C5AFABC71F055153DA423867F32564233FBD1EF59A17D5F5`

Accepted item-59 blocker:

`667E9CA48B9FF69F7548C1CB0916A2C93240470E29C218452191E3005E458668`

These remain immutable historical evidence.

## Remaining gates

58. Verify/fix the item-58 v2 freeze identities and accept the corrected 4×3×2 Level-2 design — **ACTIVE**.
59. Freeze corrected four-task neutral selection/contracts — **BLOCKED pending #58**.
60. Implement and qualify genuine P2 semantic hidden verifiers — **BLOCKED pending #59**.
61. Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock.
62. Execute accepted P2 same-repository replication.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish Level-2 P2 evidence and update paper claims/evidence.
65. Select Subject C and perform cross-repository / Level-3 replication.
66. Final hostile review, claims/statistics/limitations/reproducibility audit.
67. Final paper + reproducibility package + submission-ready release.

## Coordinator/Codex rule

Persist authoritative state; reconstruct computation. Do not force progress through a malformed freeze identity. Verify the deterministic private bindings first; only then accept item 58 and reactivate item 59.
