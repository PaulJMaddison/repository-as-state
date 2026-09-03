# Repository-as-State — CURRENT

Updated: 2026-09-03 23:36 Europe/London

## Programme status

- Authoritative progress ledger: **59/67 complete**.
- **Item 60 is ACTIVE:** implement and qualify genuine P2 semantic hidden verifiers for the already-frozen five-task corpus.
- Item 59 remains complete.
- P2 experimental agent runs: **0**.
- P2 task-solving model invoked: **FALSE**.
- P2 executed: **FALSE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Non-negotiable methodology rule

**Whole-solution or whole-project greenness is not the accepted-boundary model.**

Do not use `dotnet build SearchForCars.sln`, `dotnet test SearchForCars.sln`, or failure of an unrelated project as a reason to invalidate a frozen historical work-package boundary.

The accepted unit is the validated work-package behavioural/public-contract boundary. Hidden verification must use the narrowest implementation-independent semantic seam that actually exercises the governed candidate behaviour.

A build may be used only as an implementation detail of a semantic probe, not as the scientific verdict itself.

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

## P2 accepted design

P2 is a Level-2 same-repository descriptive replication.

- historical candidates inventoried: 10
- eligible and selected: 5
- substitutions: 0
- outcome-based exclusions: 0
- repetitions: 3
- Condition A: three independent five-task persistent chains = 15 runs
- Condition B: fifteen fresh sessions = 15 runs
- total planned runs: 30
- full-block blindness
- no formal non-inferiority claim
- durable resource telemetry

Complexity composition: **3 LOW, 2 MEDIUM, 0 HIGH**.

## P2 frozen task selection and contracts — VALID

Design-input manifest:

`D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`

Task-selection freeze:

`829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`

Private curation package:

`5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

| P2 task | Candidate | PRE | POST | Complexity | Behaviours |
|---|---|---|---|---|---:|
| P2_T01 | C06 | `a120b02abf4dd2bef11ae621d7283282159622f3` | `ddb2d79c65342e8585ef5aefe966e7b2e70b9406` | MEDIUM | 4 |
| P2_T02 | C07 | `5941869627443548a9042d900b1a4ffeda58dacb` | `c265580ac53a4e85a164a7f62a5b90f3ecf04cfe` | MEDIUM | 3 |
| P2_T03 | C08 | `142a007c64d1c20136742155b672055100128056` | `a740ce1965ba26ab5e06ed5c466430f1e28c5ac5` | LOW | 3 |
| P2_T04 | C09 | `c3b813d14973c28ed3bc063c2440224b26dc2a87` | `d7199f391983eb94bb48d8524915245898831a3a` | LOW | 4 |
| P2_T05 | C10 | `e9eb063944d604ec0c4cf6b3534f5db87fff82c0` | `a64a727d1ce22dfb851419e46958f08014a48b04` | LOW | 4 |

Totals:

- task-spec statements: 20
- governing behaviours: 18
- undisclosed governing requirements: 0
- unmapped governing behaviours: 0
- implementation-specific behavioural requirements: 0
- fairness audits: 5/5 PASS

## Item 60 verifier history

### Attempt 1 — fixture-only oracle: REJECTED

The first verifier worker used hand-authored semantic-state JSON. It did not execute candidate code. Its apparent PRE/POST, negative-control, alternate-valid and self-test evidence is invalid and quarantined.

### Attempt 2 — whole-solution build blocker: REJECTED

A coordinator prompt incorrectly introduced full solution buildability as a gate. T03 POST produced `CS0535` because Infrastructure implementations do not implement a newly declared interface member. That observation does not invalidate the work-package boundary.

### Attempt 3 — targeted project-build blocker: REJECTED

The corrected prompt explicitly required genuine semantic fallback seams before Terminal B. The worker instead ran:

- targeted `SearchForCars.Application` build — PASS;
- targeted `SearchForCars.Infrastructure` build — FAIL with the same `CS0535`;
- Git-history searches.

It then labelled application/infrastructure build paths as two candidate-code seams and returned `VALID_TERMINAL_B`.

Coordinator ruling: **reject Terminal B**.

Two compilation attempts are not two materially different semantic observation seams. The worker never executed a behaviour-level semantic verifier, returned `CANDIDATE_CODE_ACTUALLY_EXERCISED=FALSE`, created zero genuine negative controls, zero alternate-valid controls and no valid self-test package.

## Concrete P2_T03 semantic route

The T03 POST commit `a740ce1965ba26ab5e06ed5c466430f1e28c5ac5` is titled `Add complete source snapshot lifecycle contract` and modifies only the public `IMarketInventoryRepository` declaration in `src/SearchForCars.Application/Abstractions.cs`, adding `ReconcileCompleteSourceSnapshotAsync(...)`.

The targeted `SearchForCars.Application` build already passes.

Therefore the preferred T03 verifier seam is:

1. build **only** the actual historical `SearchForCars.Application` project for PRE and POST;
2. load the produced actual Application assembly;
3. reflect the actual `IMarketInventoryRepository` public metadata;
4. evaluate the three frozen T03 governing behaviours from that public contract metadata;
5. treat absence/wrong signature in PRE as `HARNESS_VALID + BEHAVIOURAL_FAIL` where appropriate;
6. require the POST assembly to expose the correct frozen contract;
7. do **not** load or build Infrastructure unless a frozen T03 behaviour explicitly requires it;
8. create genuine negative-control variants of the Application public contract and genuine alternate-valid source/assembly variants to prove the verifier is not source-text/layout coupled.

The verifier must derive its result from the compiled actual candidate Application contract, not source-string matching and not hand-authored expected-state JSON.

## Active item 60

Continue genuine semantic-verifier engineering for **all five tasks**, not T03 only.

For each task:

1. read frozen disclosed task spec and governing behaviours;
2. select a behaviour-level semantic seam;
3. execute/observe actual candidate code or compiled public contract;
4. PRE overall FAIL / POST PASS;
5. genuine per-behaviour negative controls;
6. alternate-valid implementations/structures;
7. implementation-independence audit;
8. harness self-tests;
9. 3× PRE/POST determinism;
10. ACL isolation;
11. final verifier freeze only after every gate passes.

Normal engineering work remaining is not Terminal B.

## Remaining gates

60. Implement and qualify genuine P2 semantic hidden verifiers for all five tasks — **ACTIVE**.
61. Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock.
62. Execute 30-run P2 same-repository replication.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish Level-2 P2 evidence and update paper claims/evidence.
65. Select Subject C and perform cross-repository / Level-3 replication.
66. Final hostile review, statistical/claims/limitations and reproducibility audit.
67. Final paper + reproducibility package + submission-ready release.

## Coordinator/Codex rule

Future prompts must specify the actual required semantic observation route where one is known. Do not let compiler/test-runner convenience silently replace the scientific verifier contract.