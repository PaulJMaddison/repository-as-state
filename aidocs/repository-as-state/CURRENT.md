# Repository-as-State — CURRENT

Updated: 2026-09-04 09:41 Europe/London

## Programme status

- Authoritative progress ledger: **57/67 complete**.
- **Item 58 is ACTIVE again:** repair and freeze the Subject-B P2 Level-2 design after the accepted ten-candidate eligibility re-audit reduced the eligible corpus from five tasks to four.
- Item 59 is **BLOCKED behind item 58**. The corrected four-task selection/contracts cannot become execution-authoritative until the Level-2 design is repaired and accepted.
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

The experimental unit remains validated work-package behavioural state, not whole-repository greenness.

## Immutable P1 state

Historical P1 preregistration binding:

`d95e2cdc47f8082a805fa2d5b09cdb272cf977ef`

P1 interpretation manifest:

`3952AC8FD23A95BAD54DB67300F701B14D53F27CC4D078FA68D25BACEF869BAF`

P1 result:

- persistent A: 18/30
- fresh B: 18/30
- matched behaviour agreement: 30/30
- disagreement: 0/30

P1 remains complete and immutable.

## Historical P2 Level-2 design — superseded pending repair

Historical accepted design:

- 10 historical candidates inventoried
- 5 historically classified eligible and therefore selected
- selection rule: **all eligible candidates in the historical inventory window, ordered by POST date then commit ID**
- 5 tasks × 3 repetitions × 2 conditions = 30 planned runs
- complexity: 3 LOW / 2 MEDIUM / 0 HIGH
- full-block blindness
- descriptive replication; no formal non-inferiority claim

Design-input manifest:

`D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`

Historical task-selection freeze:

`829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`

Historical private curation package:

`5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

These remain immutable historical evidence but are **not execution-authoritative**.

## Accepted contract-to-history adjudication

Private adjudication SHA256:

`4A57493EC8B70732C5AFABC71F055153DA423867F32564233FBD1EF59A17D5F5`

Accepted result:

- 18 governing behaviours audited
- 9 valid behavioural deltas
- 4 oracle-mapping defects
- 5 frozen contract defects
- 0 unresolved

Exact frozen contract defects:

- `P2_T01_B01`
- `P2_T01_B02`
- `P2_T01_B03`
- `P2_T01_B04`
- `P2_T02_B02`

Exact oracle-mapping defects whose disclosed contracts remain valid:

- `P2_T05_B01`
- `P2_T05_B02`
- `P2_T05_B03`
- `P2_T05_B04`

Exact valid behavioural deltas:

- `P2_T02_B01`
- `P2_T02_B03`
- `P2_T03_B01`
- `P2_T03_B02`
- `P2_T03_B03`
- `P2_T04_B01`
- `P2_T04_B02`
- `P2_T04_B03`
- `P2_T04_B04`

## Accepted item-59 repair blocker

Private blocker SHA256:

`667E9CA48B9FF69F7548C1CB0916A2C93240470E29C218452191E3005E458668`

The no-build/no-test/no-compile repair attempt proved that the previous five-task contract freeze could not be repaired as written without methodology review. No v2 selection/curation freeze was fabricated.

## Accepted ten-candidate eligibility re-audit v2

Terminal state:

`VALID_TERMINAL_B_ITEM58_REOPEN_REQUIRED`

Private re-audit SHA256:

`D55B610B6E2FFB1B032137F30C348FEFE9EF3542321720090C6690885D749E41`

Repeat hash: **TRUE**.

The audit re-applied the original pre-existing eligibility criteria to all ten candidates. It established that the required observable PRE→POST behavioural-delta criterion was **explicit or logically required by the original methodology**, not added after seeing the defects.

### Corrected eligibility

| Candidate | Historical | Corrected | Consequence |
|---|---|---|---|
| C01 | INELIGIBLE | INELIGIBLE | unchanged |
| C02 | INELIGIBLE | INELIGIBLE | unchanged |
| C03 | INELIGIBLE | INELIGIBLE | unchanged |
| C04 | INELIGIBLE | INELIGIBLE | unchanged |
| C05 | INELIGIBLE | INELIGIBLE | unchanged |
| C06 | ELIGIBLE | **INELIGIBLE** | no legitimate disclosed governing behaviour remains with required PRE=false / POST=true delta |
| C07 | ELIGIBLE | ELIGIBLE | remains eligible with two genuine governing behaviours; `P2_T02_B02` removed as over-curated non-delta |
| C08 | ELIGIBLE | ELIGIBLE | unchanged |
| C09 | ELIGIBLE | ELIGIBLE | unchanged |
| C10 | ELIGIBLE | ELIGIBLE | unchanged |

Corrected eligible set:

`C07, C08, C09, C10`

Corrected selected order under the original rule:

`C07 → C08 → C09 → C10`

Corrected eligible total: **4**.

Corrected complexity distribution:

- LOW: **3**
- MEDIUM: **1**
- HIGH: **0**

Corrected governing behaviours: **13**.

All 13 retained behaviours have PRE=false / POST=true historical deltas. Undisclosed governing requirements: **0**. Fairness audits: **PASS**.

Anti-cherry-picking audit:

- outcome-based eligibility decisions: 0
- model-performance information used: false
- verifier ease used as criterion: false
- desired sample size used as criterion: false
- desired complexity balance used as criterion: false
- ad-hoc replacement tasks: 0
- post-hoc slot filling: false

Public-safe records:

- `results/public/subject-b-p2-ten-candidate-eligibility-reaudit-v2.md`
- `results/public/subject-b-p2-ten-candidate-eligibility-reaudit-v2.json`
- `results/public/subject-b-p2-level2-design-impact-v2.md`
- `results/public/subject-b-p2-level2-design-impact-v2.json`

## Coordinator ruling

The old **5 tasks × 3 repetitions × 2 conditions = 30 runs** Level-2 design is no longer valid because the objective eligible corpus now contains four tasks and there is no legitimate reserve candidate.

Item 58 is therefore reopened.

Do **not**:

- reintroduce C06;
- promote C01–C05 merely to fill a slot;
- invent a fifth task;
- change repetitions merely to recreate 30 runs;
- use model outcomes or verifier convenience to alter the corpus.

The natural repair candidate is **4 tasks × 3 repetitions × 2 conditions = 24 runs**, because that preserves the already accepted repetition count and A/B treatment structure while changing only the task count forced by the corrected eligibility corpus. This is a coordinator hypothesis for the active repair work, **not yet a frozen design**.

The item-58 worker must formally test that repair against the pre-existing Level-2 design invariants, document any consequence for matched units, persistent A chains, fresh B sessions, blindness, resource telemetry and descriptive interpretation, then freeze a superseding design if valid.

## Active next work package

Repair and freeze P2 Level-2 design item 58 from the corrected four-task corpus.

If the 4 × 3 × 2 = 24 design preserves the accepted causal treatment and replication logic without introducing a new post-hoc advantage, freeze it transparently and preserve the historical 30-run design as superseded evidence.

If it does not, stop for coordinator methodology review rather than manipulating the task set or repetition count.

## Remaining gates

58. Repair and freeze P2 Level-2 design after corrected four-task eligibility re-audit — **ACTIVE**.
59. Freeze corrected four-task neutral selection/contracts — **BLOCKED pending #58**.
60. Implement and qualify genuine P2 semantic hidden verifiers for final selected tasks — **BLOCKED pending #59**.
61. Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock.
62. Execute accepted P2 same-repository replication.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish Level-2 P2 evidence and update paper claims/evidence.
65. Select Subject C and perform cross-repository / Level-3 replication.
66. Final hostile review, claims/statistics/limitations/reproducibility audit.
67. Final paper + reproducibility package + submission-ready release.

## Coordinator/Codex rule

Persist authoritative state; reconstruct computation. Do not force progress by changing objective eligibility, adding replacement tasks or manipulating repetitions to preserve a historical run count. Repair the design from the corrected corpus first, then re-freeze contracts and only then resume verifier qualification.
