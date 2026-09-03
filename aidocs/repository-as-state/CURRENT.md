# Repository-as-State — CURRENT

Updated: 2026-09-03 23:27 Europe/London

## Programme status

- Authoritative progress ledger: **58/67 complete**.
- **Item 59 is reopened and ACTIVE:** repair and re-freeze the P2 task corpus after discovery that the frozen P2_T03 POST is not a valid buildable accepted boundary.
- Item 60 verifier qualification is paused until the corpus is repaired and re-frozen.
- P2 experimental agent runs: **0**.
- P2 task-solving model invoked: **FALSE**.
- P2 executed: **FALSE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Public repository

Repository: `PaulJMaddison/repository-as-state`

Branch: `research/p0-subject-b-corpus-preregistration`

Historical P1 preregistration binding:

`d95e2cdc47f8082a805fa2d5b09cdb272cf977ef`

P1 interpretation manifest:

`3952AC8FD23A95BAD54DB67300F701B14D53F27CC4D078FA68D25BACEF869BAF`

P1 remains complete and immutable.

## P1 result

| Task | Persistent A | Fresh B | Difference |
|---|---:|---:|---:|
| WP04 | 8/8 | 8/8 | 0 |
| WP05 | 10/10 | 10/10 | 0 |
| WP06 | 0/12 | 0/12 | 0 |
| Total | 18/30 | 18/30 | 0 |

Matched behaviour-vector agreement: **30/30**.
Matched disagreement: **0/30**.

Bounded conclusion: no behavioural correctness difference was observed between persistent-session and fresh-session conditions in the three matched tasks. This is not proof of equivalence/non-inferiority or universal repository sufficiency.

## P2 design before corpus defect discovery

The accepted P2 design targeted a Level-2 same-repository descriptive replication:

- historical candidates inventoried: 10
- initially classified eligible/selected: 5
- repetitions: 3
- initially planned Condition A runs: 15
- initially planned Condition B runs: 15
- initially planned total: 30
- full-block blindness
- no formal non-inferiority claim
- durable resource telemetry

The initial corpus freeze selected P2_T01..P2_T05 and was bound by:

- design-input manifest: `D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`
- task-selection freeze: `829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`
- curation package: `5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

Those P2 task-selection/curation freezes are now **SUPERSEDED PENDING CORPUS REPAIR**. They must not enter final P2 preregistration unchanged.

## Genuine blocker discovered during verifier remediation

The genuine candidate-workspace verifier remediation materialised and attempted to build the exact frozen historical candidates.

For P2_T03 / candidate C08:

PRE:
`142a007c64d1c20136742155b672055100128056`

Frozen POST:
`a740ce1965ba26ab5e06ed5c466430f1e28c5ac5`

The exact POST fails compilation with `CS0535` because both:

- `InMemoryMarketInventoryRepository`
- `PostgresMarketInventoryRepository`

lack the newly declared `IMarketInventoryRepository.ReconcileCompleteSourceSnapshotAsync(...)` member.

This is a candidate compile-time contract failure, not a verifier-harness failure.

Therefore the frozen P2_T03 POST cannot currently satisfy the accepted requirement that a selected historical POST be a validated executable accepted boundary.

Worker classification: **VALID_TERMINAL_B — accepted by coordinator for this run**.

The earlier fixture-only verifier attempt remains superseded and invalid for qualification.

## Methodology consequence

Item 59 is reopened because the task-selection freeze itself contains a defective historical POST identity.

The next worker must perform an auditable corpus-boundary repair, not silently patch the candidate or substitute a convenient task.

It must determine one of two valid outcomes for C08:

1. **Correct historical accepted POST exists:** prove that `a740ce1...` was an intermediate/non-accepted boundary and identify the actual accepted C08 POST from contemporaneous historical evidence. Re-run all frozen eligibility/materialisability/buildability/contract checks and create a new superseding task-selection/curation freeze.

2. **No valid accepted C08 POST exists:** reclassify C08 as ineligible under the already-existing accepted-boundary/deterministic-execution criteria, mechanically recompute the complete 10-candidate pool, and redesign/re-freeze P2 using all tasks that remain eligible. Do not substitute an excluded task merely to preserve a five-task count.

The worker must also mechanically build/test the exact POST boundary for every task that remains eligible so this defect cannot recur.

## Current frozen task identities under review

| P2 task | Candidate | PRE | Previously frozen POST | Complexity | Status |
|---|---|---|---|---|---|
| P2_T01 | C06 | `a120b02abf4dd2bef11ae621d7283282159622f3` | `ddb2d79c65342e8585ef5aefe966e7b2e70b9406` | MEDIUM | revalidate |
| P2_T02 | C07 | `5941869627443548a9042d900b1a4ffeda58dacb` | `c265580ac53a4e85a164a7f62a5b90f3ecf04cfe` | MEDIUM | revalidate |
| P2_T03 | C08 | `142a007c64d1c20136742155b672055100128056` | `a740ce1965ba26ab5e06ed5c466430f1e28c5ac5` | LOW | **invalid POST / repair required** |
| P2_T04 | C09 | `c3b813d14973c28ed3bc063c2440224b26dc2a87` | `d7199f391983eb94bb48d8524915245898831a3a` | LOW | revalidate |
| P2_T05 | C10 | `e9eb063944d604ec0c4cf6b3534f5db87fff82c0` | `a64a727d1ce22dfb851419e46958f08014a48b04` | LOW | revalidate |

## Active work package

**P2 CORPUS BOUNDARY METHODOLOGY REPAIR — C08 / FULL SELECTED-POOL REVALIDATION**

No P2 hidden verifier may be finally qualified and no P2 preregistration/execution may begin until the corrected corpus is frozen.

## Remaining gates

59. Repair/re-freeze exact P2 task selection + valid accepted PRE/POST boundaries + complexity/contracts — **ACTIVE / REOPENED**.
60. Implement and qualify genuine P2 semantic hidden verifiers against corrected corpus.
61. Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock.
62. Execute P2 same-repository replication using corrected preregistered run count.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish Level-2 P2 evidence and update paper claims/evidence.
65. Select Subject C and perform cross-repository / Level-3 replication.
66. Final hostile review, statistical/claims/limitations and reproducibility audit.
67. Final paper + reproducibility package + submission-ready release.

## Coordinator/Codex rule

Frozen evidence can be reopened when later evidence demonstrates that the freeze itself was methodologically invalid. The repair must be explicit, append-only, auditable and completed before any experimental model run.

No silent candidate patching, no outcome-based substitution and no P2 execution are permitted.