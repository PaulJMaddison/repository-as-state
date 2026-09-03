# Repository-as-State — CURRENT

Updated: 2026-09-03 23:19 Europe/London

## Programme status

- Authoritative progress ledger: **59/67 complete**.
- **Item 60 remains active:** implement and qualify genuine P2 semantic hidden verifiers for all five frozen tasks.
- The first item-60 verifier attempt is **REJECTED / PROVISIONAL ONLY** because it evaluated hand-authored semantic-state fixtures instead of the actual candidate workspaces.
- P2 experimental agent runs: **0**.
- P2 task-solving model invoked: **FALSE**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Public repository

Repository: `PaulJMaddison/repository-as-state`

Branch: `research/p0-subject-b-corpus-preregistration`

Historical P1 preregistration binding:

`d95e2cdc47f8082a805fa2d5b09cdb272cf977ef`

P1 public result/claims state before later documentation/P2 publication:

`525d30f5cc59dbad2ff6996ab3b7fbec62bc90e6`

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

P1 interpretation manifest:

`3952AC8FD23A95BAD54DB67300F701B14D53F27CC4D078FA68D25BACEF869BAF`

Bounded conclusion: no behavioural correctness difference was observed between persistent-session and fresh-session conditions in the three matched tasks. This is not proof of equivalence/non-inferiority or universal repository sufficiency.

## P2 accepted design

P2 is a Level-2 same-repository descriptive replication.

- historical candidates: 10
- eligible and selected: 5
- substitutions: 0
- outcome-based exclusions: 0
- complexity: 3 LOW, 2 MEDIUM, 0 HIGH
- repetitions: 3
- A: three independent five-task persistent chains = 15 runs
- B: fifteen independent fresh sessions = 15 runs
- total planned runs: 30
- all 30 outputs frozen before hidden verdict release
- no formal non-inferiority claim
- durable resource telemetry required

The lack of HIGH-complexity eligible tasks is an explicit limitation.

## P2 frozen task selection and contracts

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
- unmapped behaviours: 0
- implementation-specific behavioural requirements: 0
- fairness audits: 5/5 PASS

## Item 60 — rejected provisional verifier attempt

The first verifier worker correctly materialised all ten historical PRE/POST workspaces and identified that the repository's full test suite was unsuitable as a hidden oracle in the isolated controls because it hung.

It then created a provisional `oracle_runner.py` that judged hand-authored `pre-state.json`, `post-state.json`, negative-state JSON and alternate-valid JSON fixtures.

That approach is **scientifically invalid** for P2 because the purported verifier did not observe the real candidate implementation. Therefore:

- provisional PRE/POST discrimination does **not count**;
- provisional 18/18 negative-control detection does **not count**;
- provisional alternate-valid passes do **not count**;
- provisional self-test claims do **not count**;
- provisional verifier hashes/package must **never** enter P2 preregistration;
- deterministic output from the fixture runner is not sufficient evidence.

The worker returned `VALID_TERMINAL_B`, but the coordinator rejects that terminal classification: this is ordinary verifier engineering work, not a methodology blocker requiring frozen-contract changes.

Positive evidence that remains usable from the attempt:

- exact per-task behaviour counts are now known: 4/3/3/4/4 = 18;
- all ten exact historical candidate workspaces were materialised;
- hidden-verifier ACL isolation was established while preserving coordinator access;
- P2 experimental runs remain 0;
- no task-solving model was invoked;
- frozen P2 design/task-selection/curation identities were not changed.

## Active item 60 remediation requirement

Reimplement genuine candidate-workspace semantic probes.

The final verifier must derive every behavioural verdict from the actual candidate workspace/process/public contract, not hand-authored expected-state files.

For each task the worker must:

1. inspect the frozen disclosed behaviour contract;
2. identify implementation-independent executable semantic seams;
3. build a verifier/probe that loads, invokes or runs the actual candidate code;
4. obtain HARNESS_VALID PRE overall FAIL and POST PASS;
5. create real negative-control candidate variants from the historical POST, one per behaviour, and prove the semantic verifier detects them;
6. create real alternate-valid candidate implementations that differ materially from historical POST internals and still pass;
7. run harness self-tests that distinguish invalid harness from behavioural failure;
8. prove 3x PRE/POST determinism;
9. preserve hidden-material isolation;
10. only then freeze final per-task verifier hashes and the overall verifier package.

Hand-authored files may configure deterministic fixtures/dependency responses, but they may not directly state the behavioural verdict or substitute for executing/observing candidate code.

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

Normal verifier engineering work remaining is never a valid terminal state. `VALID_TERMINAL_B` is reserved for a genuine blocker that cannot be solved without changing a frozen scientific contract/identity.

Whenever Codex returns, the coordinator must assess the evidence, update aidocs/public evidence where appropriate, and provide the exact next prompt in the same response.