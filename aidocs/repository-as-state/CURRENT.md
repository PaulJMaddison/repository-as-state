# Repository-as-State — CURRENT

Updated: 2026-09-03 23:38 Europe/London

## Programme status

- Authoritative progress ledger: **59/67 complete**.
- **Item 60 is ACTIVE:** implement and qualify genuine P2 semantic hidden verifiers for the already-frozen five-task corpus.
- Item 59 remains complete.
- P2 experimental agent runs: **0**.
- P2 task-solving model invoked: **FALSE**.
- P2 executed: **FALSE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## ABSOLUTE ITEM-60 RULE — NO BUILD OR TEST EXECUTION

The coordinator repeatedly and incorrectly reintroduced build/test activity into P2 verifier qualification after the user had already ruled it out.

This is now an absolute protocol rule for item 60:

**DO NOT RUN BUILD OR TEST COMMANDS AS PART OF P2 VERIFIER QUALIFICATION.**

Forbidden includes, without exception:

- `dotnet build`
- `dotnet test`
- full-solution builds/tests
- targeted project builds/tests
- minimal-project builds/tests
- probe builds/tests
- candidate compilation used as a qualification gate
- any attempt to classify PRE/POST validity from compilation or test-runner success/failure.

Do not rename build activity as a "semantic seam", "targeted compilation", "probe compilation", "dependency build", or similar.

Item 60 is about **semantic behavioural verification**, not build verification.

Historical PRE/POST identities remain frozen and valid under the accepted work-package boundary model. Whole-repository/project greenness is irrelevant to this gate.

Any previous item-60 evidence whose conclusion depended on build/test success or failure is **NON-AUTHORITATIVE FOR QUALIFICATION**.

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

The first verifier worker used hand-authored semantic-state JSON. It did not derive results from the actual frozen candidate semantics. Its apparent PRE/POST, negative-control, alternate-valid and self-test evidence is invalid.

### Attempts 2/3 — build-based stops: REJECTED

Subsequent workers were given bad coordinator prompts that reintroduced solution/project build activity. They stopped on compile errors around T03.

Those stops are rejected because build/test activity is outside the item-60 qualification protocol.

They do not reopen item 59 and do not invalidate T03.

## Active item 60 — correct task

For each P2 task:

1. read the frozen disclosed task specification and governing behaviours;
2. derive an implementation-independent semantic verifier directly from those frozen behaviours;
3. observe the relevant candidate semantics without invoking build/test commands;
4. establish PRE overall FAIL and POST PASS for the frozen disclosed behaviours;
5. create genuine per-behaviour semantic negative controls without using build/test as their verdict mechanism;
6. create alternate-valid semantic implementations/structures sufficient to demonstrate verifier implementation independence;
7. distinguish verifier/harness failure from behavioural failure;
8. prove determinism;
9. preserve hidden-material isolation;
10. freeze final verifier packages only after every semantic qualification gate passes.

The verifier may inspect repository state, source structure, public contract declarations, deterministic data/configuration and other behaviour-relevant artifacts as required, but must not reduce correctness to exact historical source text, patch identity, helper names, test names, commit identity or hand-authored expected-result files.

If a behaviour truly requires runtime execution that cannot be observed without prohibited build/test activity, stop and escalate to the coordinator **before inventing a new gate**. Do not silently convert the experiment into a build qualification study.

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

**Never put build or test execution back into item 60.**

Normal verifier engineering work remaining is not a valid terminal state. No new methodology gate may be introduced merely because it is convenient for the worker.