# Repository-as-State — CURRENT

Updated: 2026-09-03 23:32 Europe/London

## Programme status

- Authoritative progress ledger: **59/67 complete**.
- **Item 60 is ACTIVE:** implement and qualify genuine P2 semantic hidden verifiers for the already-frozen five-task corpus.
- Item 59 remains complete.
- P2 experimental agent runs: **0**.
- P2 task-solving model invoked: **FALSE**.
- P2 executed: **FALSE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Important correction — full-solution build is NOT an accepted-boundary gate

A coordinator prompt on 2026-09-03 incorrectly instructed the P2 verifier worker to use full historical solution build/test success as a qualification condition and then incorrectly reopened item 59 when `dotnet build SearchForCars.sln` failed for P2_T03.

That was a methodology/prompt error by the coordinator.

The established Repository-as-State protocol treats the accepted work-package boundary and frozen disclosed behavioural contract as authoritative. **Commit/whole-repository greenness is not itself the accepted-boundary model.**

For P2 verifier qualification:

- do **not** run `dotnet build SearchForCars.sln` or `dotnet test SearchForCars.sln` as an eligibility/accepted-boundary gate;
- do **not** invalidate a frozen PRE/POST identity merely because the entire historical solution does not compile in isolation;
- do exercise the actual candidate implementation through the narrowest implementation-independent semantic seam required by each disclosed behaviour;
- a private semantic probe/adaptor may itself compile a minimal project or relevant candidate dependency set when necessary to exercise real candidate code;
- targeted compilation/loading used by a semantic probe is evidence about that probe seam, not a whole-repository greenness requirement;
- if a particular semantic seam cannot be exercised, try alternate legitimate seams such as reflection, dynamic loading, minimal compile adapters, process/public API behaviour, deterministic fakes, or stable behavioural observation before considering a genuine blocker;
- source/test-name selectors and fixture-only verdicts remain forbidden.

The earlier public `subject-b-p2-corpus-freeze-correction-v1` record is therefore itself **SUPERSEDED by coordinator correction v2**. Its conclusion that the T03 POST was invalid solely because the full solution build failed must not be used.

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

## Item 60 history

### Rejected fixture-only attempt

The first verifier attempt used hand-authored semantic-state JSON rather than actual candidate execution. Its apparent PRE/POST, negative-control, alternate-valid and self-test evidence is invalid and quarantined.

### Over-strict full-solution build attempt — not a corpus blocker

The next worker correctly quarantined the fixture-only oracle but then followed the coordinator's incorrect instruction to build the entire historical SearchForCars solution. T03 produced `CS0535` under that whole-solution build.

That observation may be retained as engineering context, but **it does not invalidate the frozen T03 task identity and does not reopen item 59**.

The correct next action is to continue semantic-verifier engineering using the P1 pattern: direct behaviour probes against actual candidate code with narrow adapters/fixtures, no test-name selectors and no whole-solution greenness gate.

## Active item 60

For each P2 task, complete genuine semantic verifier qualification:

1. read frozen disclosed task spec/behaviours;
2. identify the narrowest real semantic observation seam;
3. exercise actual candidate code through that seam;
4. obtain historical PRE overall FAIL and POST PASS under the semantic verifier;
5. use genuine semantic negative controls, not fixture verdict files;
6. use alternate valid implementations/structures to prove implementation independence;
7. self-test harness-invalid vs behavioural-fail classification;
8. prove determinism;
9. preserve hidden-material isolation;
10. freeze final verifier packages only after all gates pass.

Do not use full `SearchForCars.sln` build/test success as a completion requirement.

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

Normal verifier engineering work remaining is never a valid terminal state. Do not add new methodology gates that were not part of the frozen protocol. In particular, do not conflate whole-repository greenness with a validated work-package boundary.