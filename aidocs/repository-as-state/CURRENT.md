# Repository-as-State — CURRENT

Updated: 2026-09-03 23:58 Europe/London

## Programme status

- Authoritative progress ledger: **59/67 complete**.
- **Item 60 is ACTIVE but paused for contract-to-history adjudication.**
- Item 59 is **not reopened yet**.
- P2 experimental agent runs: **0**.
- P2 task-solving model invoked: **FALSE**.
- P2 executed: **FALSE**.
- P2 preregistered: **FALSE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Absolute item-60 methodology rule

**NO BUILD, TEST, RESTORE OR COMPILER EXECUTION IS PERMITTED AS PART OF P2 VERIFIER QUALIFICATION.**

Forbidden includes full-solution, targeted-project, minimal-project, probe and candidate builds/tests/compilation. Compilation/test-runner success or failure is not PRE/POST qualification evidence.

Item 60 is semantic hidden-verifier qualification against frozen repository state.

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

## P2 accepted design

- 10 historical candidates inventoried
- 5 objectively eligible/selected
- 0 substitutions
- 0 outcome-based exclusions
- complexity: 3 LOW / 2 MEDIUM / 0 HIGH
- repetitions: 3
- planned A runs: 15
- planned B runs: 15
- planned total: 30
- full-block blindness
- descriptive replication; no formal non-inferiority claim

Design-input manifest:

`D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`

Task-selection freeze:

`829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`

Private curation package:

`5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

| Task | Candidate | PRE | POST | Complexity | Behaviours |
|---|---|---|---|---|---:|
| P2_T01 | C06 | `a120b02abf4dd2bef11ae621d7283282159622f3` | `ddb2d79c65342e8585ef5aefe966e7b2e70b9406` | MEDIUM | 4 |
| P2_T02 | C07 | `5941869627443548a9042d900b1a4ffeda58dacb` | `c265580ac53a4e85a164a7f62a5b90f3ecf04cfe` | MEDIUM | 3 |
| P2_T03 | C08 | `142a007c64d1c20136742155b672055100128056` | `a740ce1965ba26ab5e06ed5c466430f1e28c5ac5` | LOW | 3 |
| P2_T04 | C09 | `c3b813d14973c28ed3bc063c2440224b26dc2a87` | `d7199f391983eb94bb48d8524915245898831a3a` | LOW | 4 |
| P2_T05 | C10 | `e9eb063944d604ec0c4cf6b3534f5db87fff82c0` | `a64a727d1ce22dfb851419e46958f08014a48b04` | LOW | 4 |

## Item 60 history

### Fixture-only oracle

Rejected. It encoded expected semantic state instead of deriving observations from frozen candidate state.

### Build-based stops

Rejected. Build/test activity is outside item 60.

### No-build structural-oracle attempt — current state

The latest worker obeyed the corrected protocol:

- build commands executed: 0
- test commands executed: 0
- compiler commands executed: 0
- experimental runs: 0

It built a structural source-derived oracle and then returned Terminal B claiming PRE/POST materialisation inconsistency because some files were byte-identical across PRE and POST.

That Terminal-B diagnosis is **NOT YET ACCEPTED**.

Coordinator verification against authoritative Git history shows:

### P2_T05 / C10

POST `a64a727d...` is `Implement cross-instance acquisition host leases`.

The only changed production file is:

`src/SearchForCars.Infrastructure/AcquisitionSourceRepositories.cs`

The POST adds real in-memory and PostgreSQL implementations of `TryAcquireHostLeaseAsync` and `ReleaseHostLeaseAsync`.

Therefore `src/SearchForCars.Application/AcquisitionAbstractions.cs` being byte-identical PRE/POST is **expected** and is not a materialisation defect. If the structural oracle treated interface equality as failure, that is an **oracle/behaviour-seam mapping defect**.

### P2_T01 / C06

PRE→POST `a120b02... -> ddb2d79...` changes:

- `Dockerfile`
- `src/SearchForCars.Infrastructure/TraderSubscriptionRepositories.cs`
- `src/SearchForCars.Web/TraderEndpoints.cs`
- regression/security/readiness test files

It does **not** change `src/SearchForCars.Web/Program.cs` or `SellerReportService.cs`.

Therefore those files being byte-identical in correctly materialised PRE/POST states is not itself corruption.

However, this creates a genuine methodology question: if any of the frozen four T01 governing behaviours claim a behavioural delta in unchanged/pre-existing production semantics (for example production-startup refusal already present in PRE), then the frozen T01 contract may violate the P2 eligibility rule `PRE lacks behaviour; POST contains behaviour`.

We must distinguish:

1. **oracle mapping defect** — verifier inspected the wrong seam/file while the frozen behaviour is valid elsewhere in the actual POST delta; from
2. **frozen contract defect** — the disclosed governing behaviour was already satisfied by PRE or is not introduced by the selected POST.

Do not reopen item 59 until this adjudication is complete.

## Active next work package

Run a **NO-BUILD CONTRACT-TO-HISTORY ADJUDICATION** across all five P2 tasks, with special focus on T01 and T05.

For every one of the 18 frozen governing behaviours, read the exact frozen statement and requirement mapping, then compare it to the authoritative PRE/POST Git objects and classify:

- VALID_BEHAVIOURAL_DELTA — PRE lacks governed semantic property; POST introduces/satisfies it;
- ORACLE_MAPPING_DEFECT — frozen behaviour is valid but previous verifier inspected the wrong semantic seam;
- FROZEN_CONTRACT_DEFECT — frozen behaviour was already satisfied by PRE, is absent from POST, or is otherwise not a valid PRE→POST behavioural delta;
- UNRESOLVED — evidence genuinely insufficient.

No build/test/restore/compiler commands. No experimental model. No frozen artifact mutation during adjudication.

If all 18 behaviours are VALID_BEHAVIOURAL_DELTA or ORACLE_MAPPING_DEFECT, item 59 remains complete and item 60 resumes with corrected semantic seams.

If any behaviour is FROZEN_CONTRACT_DEFECT, then and only then reopen item 59 for methodology-controlled re-curation/selection repair.

## Remaining gates

60. Implement and qualify genuine P2 semantic hidden verifiers — **ACTIVE / adjudication substep**.
61. Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock.
62. Execute 30-run P2 same-repository replication.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish Level-2 P2 evidence and update paper claims/evidence.
65. Select Subject C and perform cross-repository / Level-3 replication.
66. Final hostile review, claims/statistics/limitations/reproducibility audit.
67. Final paper + reproducibility package + submission-ready release.

## Coordinator/Codex rule

Never reintroduce build/test/compile activity into item 60. A file being unchanged across PRE/POST is not automatically a defect; adjudicate against the actual frozen behaviour and actual historical delta.