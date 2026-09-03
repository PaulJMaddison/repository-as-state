# Repository-as-State — CURRENT

Updated: 2026-09-03 23:05 Europe/London

## Programme status

- Authoritative progress ledger: **59/67 complete**.
- **Item 60 is active:** implement and qualify P2 semantic hidden verifiers for all five frozen tasks.
- P2 experimental agent runs: **0**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Public repository

Repository: `PaulJMaddison/repository-as-state`

Branch: `research/p0-subject-b-corpus-preregistration`

Historical P1 preregistration binding point:

`d95e2cdc47f8082a805fa2d5b09cdb272cf977ef`

P1 public-results / claims state before later aidocs/P2-publication commits:

`525d30f5cc59dbad2ff6996ab3b7fbec62bc90e6`

Later documentation and P2-publication commits do not alter the historical P1 preregistration binding.

## P1 — complete and immutable

Frozen execution order:

`B1 -> A1 -> A2 -> B2 -> B3 -> A3`

P1 result:

| Task | Persistent A | Fresh B | Paired difference |
|---|---:|---:|---:|
| WP04 | 8/8 | 8/8 | 0 |
| WP05 | 10/10 | 10/10 | 0 |
| WP06 | 0/12 | 0/12 | 0 |
| **Total** | **18/30** | **18/30** | **0** |

Matched behaviour-vector agreement: **30/30**.
Matched disagreement: **0/30**.

No behavioural correctness difference was observed between persistent-session and fresh-session conditions in these three matched tasks. This is not a proof of equivalence/non-inferiority or universal repository sufficiency.

WP06 classification: high-confidence **common foundational-capability omission**, not a differential session-continuity effect.

P1 six-run blinded freeze:

`F426272137C6A39E6D1B60361B1792365853C70DD979036BB92C539768822D3C`

P1 raw adjudication manifest:

`5B80CB2655B974149C89F086A1135F47C6427009A2525EB5ABA5F9A686710DF5`

P1 interpretation manifest:

`3952AC8FD23A95BAD54DB67300F701B14D53F27CC4D078FA68D25BACEF869BAF`

## P2 accepted design

P2 is a Level-2 same-repository replication, not a rerun of P1.

Accepted design:

- historical candidates inventoried: 10
- eligible: 5
- excluded: 5
- selection rule: all eligible candidates in the historical inventory window, ordered by POST date then commit ID
- substitutions: 0
- outcome-based exclusions: 0
- repetitions: 3
- Condition A: three independent five-task persistent chains = 15 runs
- Condition B: fifteen fresh sessions = 15 runs
- total planned model runs: 30
- primary analysis unit: matched task × repetition outcome
- formal non-inferiority: not justified; descriptive replication
- blindness: all 30 outputs frozen before hidden verdict release
- retry: infrastructure-only repair before model activity; no model-quality retry after activity
- resource telemetry: strengthened/durable

Complexity composition: **3 LOW, 2 MEDIUM, 0 HIGH**.

The lack of HIGH-complexity eligible tasks is an explicit P2 limitation.

## P2 task-selection + contract freeze — COMPLETE

Accepted design-input manifest:

`D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`

Deterministic private task-selection freeze:

`829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`

Private curation package:

`5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

Exact frozen P2 corpus:

| P2 task | Candidate | PRE | POST | Complexity |
|---|---|---|---|---|
| P2_T01 | C06 | `a120b02abf4dd2bef11ae621d7283282159622f3` | `ddb2d79c65342e8585ef5aefe966e7b2e70b9406` | MEDIUM |
| P2_T02 | C07 | `5941869627443548a9042d900b1a4ffeda58dacb` | `c265580ac53a4e85a164a7f62a5b90f3ecf04cfe` | MEDIUM |
| P2_T03 | C08 | `142a007c64d1c20136742155b672055100128056` | `a740ce1965ba26ab5e06ed5c466430f1e28c5ac5` | LOW |
| P2_T04 | C09 | `c3b813d14973c28ed3bc063c2440224b26dc2a87` | `d7199f391983eb94bb48d8524915245898831a3a` | LOW |
| P2_T05 | C10 | `e9eb063944d604ec0c4cf6b3534f5db87fff82c0` | `a64a727d1ce22dfb851419e46958f08014a48b04` | LOW |

Curation totals:

- task-spec statements: **20**
- governing behaviours: **18**
- undisclosed governing requirements: **0**
- unmapped governing behaviours: **0**
- implementation-specific behaviour requirements: **0**
- fairness audits: **5/5 PASS**
- historical PRE expected overall: **FAIL for all five**
- historical POST expected overall: **PASS for all five**
- P2 experimental agent runs: **0**

Public-safe selection/contract summaries are published under `results/public/subject-b-p2-*`.

## Active work package — item 60

Next worker:

**IMPLEMENT AND QUALIFY P2 SEMANTIC HIDDEN VERIFIERS**

Required outcome for all five frozen tasks:

1. implementation-independent semantic verifier implementation;
2. exact historical PRE overall FAIL;
3. exact historical POST PASS;
4. all 18 governing behaviours mechanically observed;
5. per-behaviour negative-control detection;
6. alternate valid implementation compatibility where feasible;
7. implementation-independence audit;
8. determinism/repeatability;
9. hidden-material access isolation from future experimental identities;
10. frozen task-verifier hashes and overall P2 verifier-package hash;
11. no P2 experimental model invocation;
12. no final P2 preregistration yet until verifier/runtime/prompt/order identities are ready.

Expected next stage after item 60:

**61. Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock.**

## Remaining programme gates

60. Implement and qualify P2 semantic hidden verifiers for all five tasks — ACTIVE.
61. Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock.
62. Execute 30-run P2 same-repository replication.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish Level-2 P2 evidence and update paper claims/evidence.
65. Select Subject C and perform cross-repository / Level-3 replication.
66. Final hostile review, statistical/claims/limitations and reproducibility audit.
67. Final paper + reproducibility package + submission-ready release.

## Coordinator/Codex division of labour

Coordinator/ChatGPT owns public/shared GitHub changes, methodology acceptance, public-safe publication, claim boundaries and exact next Codex work-package prompts.

Codex primarily owns local/private implementation, verifier work, deterministic historical materialisation, experiment execution and local/private evidence generation.

Whenever Codex returns a work package, the coordinator must in the same response:

1. assess validity and what was proved;
2. make any safe public/shared GitHub changes directly;
3. update `CURRENT.md`, `PROGRAMME-MATRIX.md` and a timestamped handoff;
4. provide the exact next Codex prompt.
