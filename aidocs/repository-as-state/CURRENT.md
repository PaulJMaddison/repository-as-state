# Repository-as-State — CURRENT

Updated: 2026-09-04 09:19 Europe/London

## Programme status

- Authoritative progress ledger: **58/67 complete**.
- **Item 59 is ACTIVE:** the previous five-task selection/contract freeze cannot be repaired as written and now requires a full ten-candidate eligibility re-audit under the original frozen selection criteria.
- Item 60 is **BLOCKED** until item 59 is re-completed.
- Item 58 remains complete **for now**. It is reopened only if the corrected eligibility audit proves that the accepted five-task Level-2 design no longer has five eligible tasks.
- P2 experimental agent runs: **0**.
- P2 task-solving model invoked: **FALSE**.
- P2 executed: **FALSE**.
- P2 preregistered: **FALSE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Absolute methodology rule

**NO BUILD, TEST, RESTORE OR COMPILER EXECUTION IS PERMITTED IN THE CURRENT P2 CONTRACT / ELIGIBILITY / VERIFIER WORK.**

Do not use whole-solution, targeted-project, minimal-project, probe or candidate build/test/compile outcomes as corpus, contract or verifier evidence.

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

## P2 historical Level-2 design state

Historical design:

- 10 historical candidates inventoried
- 5 originally classified eligible and therefore selected
- selection rule: **all eligible candidates in the historical inventory window, ordered by POST date then commit ID**
- 0 substitutions
- 0 outcome-based exclusions
- historical complexity: 3 LOW / 2 MEDIUM / 0 HIGH
- repetitions: 3
- historical planned A runs: 15
- historical planned B runs: 15
- historical planned total: 30
- full-block blindness
- descriptive replication; no formal non-inferiority claim

Design-input manifest:

`D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`

Historical task-selection freeze:

`829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`

Historical private curation package:

`5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

These identities remain immutable historical evidence. The old item-59 freeze is not execution-authoritative.

| Task | Candidate | PRE | POST | Complexity | Historical behaviour count |
|---|---|---|---|---|---:|
| P2_T01 | C06 | `a120b02abf4dd2bef11ae621d7283282159622f3` | `ddb2d79c65342e8585ef5aefe966e7b2e70b9406` | MEDIUM | 4 |
| P2_T02 | C07 | `5941869627443548a9042d900b1a4ffeda58dacb` | `c265580ac53a4e85a164a7f62a5b90f3ecf04cfe` | MEDIUM | 3 |
| P2_T03 | C08 | `142a007c64d1c20136742155b672055100128056` | `a740ce1965ba26ab5e06ed5c466430f1e28c5ac5` | LOW | 3 |
| P2_T04 | C09 | `c3b813d14973c28ed3bc063c2440224b26dc2a87` | `d7199f391983eb94bb48d8524915245898831a3a` | LOW | 4 |
| P2_T05 | C10 | `e9eb063944d604ec0c4cf6b3534f5db87fff82c0` | `a64a727d1ce22dfb851419e46958f08014a48b04` | LOW | 4 |

## Accepted contract-to-history adjudication

Private adjudication artifact SHA256:

`4A57493EC8B70732C5AFABC71F055153DA423867F32564233FBD1EF59A17D5F5`

Repeat-hash verification: **TRUE**.

Accepted counts:

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

Public-safe adjudication:

- `results/public/subject-b-p2-contract-to-history-adjudication-v1.md`
- `results/public/subject-b-p2-contract-to-history-adjudication-v1.json`

## Accepted item-59 contract-repair blocker

The exact repair worker obeyed the no-build/no-test/no-compile protocol and returned `VALID_TERMINAL_B`.

Private blocker record SHA256:

`667E9CA48B9FF69F7548C1CB0916A2C93240470E29C218452191E3005E458668`

It established:

- the current five-task freeze cannot be repaired **as written** simply by rewriting the five defective behaviours;
- all four historical T01/C06 behaviours are contract defects;
- T02/C07 has one defective behaviour (`P2_T02_B02`) but two already accepted genuine deltas (`P2_T02_B01`, `P2_T02_B03`);
- no repaired behaviour was fabricated;
- no v2 curation package or item-59 refreeze was created;
- task substitutions: 0;
- outcome-based exclusions/reselection: 0;
- build/test/compiler commands: 0;
- P2 experimental runs: 0.

Public-safe records:

- `results/public/subject-b-p2-item59-contract-repair-blocker-v2.md`
- `results/public/subject-b-p2-item59-contract-repair-blocker-v2.json`

## Coordinator ruling

Do **not** infer from the repair blocker that both C06 and C07 must automatically be discarded.

- **C06/T01:** because all four curated behaviours failed the historical-delta requirement, its eligibility is now in serious doubt. The next audit must determine whether the historical work package has any legitimate disclosed PRE=false / POST=true governing behaviour under the original criteria. If not, C06 is ineligible.
- **C07/T02:** do not discard it merely because B02 was over-curated. B01 and B03 are already adjudicated as valid deltas. The next audit must determine whether the original eligibility criteria allow a task with a complete fair two-behaviour contract; if yes, C07 remains eligible with B02 removed rather than inventing a replacement requirement.
- **C08/C09:** their current governing behaviours were adjudicated as valid behavioural deltas.
- **C10:** its four disclosed behaviours remain valid; only the future verifier seam was mapped incorrectly.

The historical selection rule selected **all eligible candidates**, not a ranked top five. Therefore there is no legitimate automatic “next candidate”.

The next step is a **complete C01–C10 eligibility re-audit under the original frozen criteria**. The five previously excluded candidates must be rechecked under exactly the same criteria. An originally excluded candidate may enter only if its original exclusion is objectively shown to have been wrong; it must not be used as a convenient replacement for C06/C07.

### Design consequence rule

- If the corrected eligible set contains **five tasks**, preserve item 58 and complete a new item-59 selection/contract freeze from that corrected set.
- If the corrected eligible set contains **not five tasks**, do not force the sample back to five. Item 58 must then be reopened for a transparent Level-2 design repair before item 59 can complete.
- Do not increase repetitions, add replacements, or otherwise preserve 30 runs post hoc without a separate accepted item-58 methodology decision.

## Active next work package

Run a no-build/no-test/no-compile **full ten-candidate P2 eligibility re-audit** using the original inventory window, eligibility rules, anti-cherry-picking rule and historical requirement evidence.

The worker must first establish whether the required PRE=false / POST=true disclosed behavioural-delta condition was already explicit or logically required by the accepted design. It must not silently add a new eligibility criterion after seeing the defects. If making that condition an eligibility criterion would itself be a new methodological rule rather than clarification of the existing one, stop for coordinator review.

Then reclassify C01–C10 and apply the frozen selection rule mechanically: all corrected eligible candidates, ordered by POST date then commit ID.

## Remaining gates

59. Re-audit all ten P2 candidates under the original eligibility rule and repair/re-freeze the execution-authoritative task selection/contracts — **ACTIVE**.
60. Implement and qualify genuine P2 semantic hidden verifiers — **BLOCKED pending #59**.
61. Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock.
62. Execute the accepted P2 same-repository replication design.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish Level-2 P2 evidence and update paper claims/evidence.
65. Select Subject C and perform cross-repository / Level-3 replication.
66. Final hostile review, claims/statistics/limitations/reproducibility audit.
67. Final paper + reproducibility package + submission-ready release.

## Coordinator/Codex rule

No ad-hoc substitution. No post-hoc balancing. No build/test/compile evidence. Reconstruct the objective eligibility rule from the pre-existing design evidence, audit all ten candidates, and let the corrected eligible set determine whether item 58 remains valid.
