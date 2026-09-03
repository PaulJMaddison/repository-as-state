# Repository-as-State — CURRENT

Updated: 2026-09-03 22:58 Europe/London

## Programme status

- Authoritative progress ledger: **58/67 complete**.
- **Item 59 is active:** P2 task-selection freeze + neutral contract curation.
- P2 experimental agent runs: **0**.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.

## Public repository

Repository: `PaulJMaddison/repository-as-state`

Branch: `research/p0-subject-b-corpus-preregistration`

Historical P1 preregistration binding point:

`d95e2cdc47f8082a805fa2d5b09cdb272cf977ef`

P1 public-results / claims state before aidocs commits:

`525d30f5cc59dbad2ff6996ab3b7fbec62bc90e6`

The later `aidocs` commits are post-experiment documentation only. They do not alter the historical P1 preregistration binding.

## P1 — complete

P1 experimental execution is complete.

Frozen execution order:

`B1 -> A1 -> A2 -> B2 -> B3 -> A3`

Treatment:

- Condition A: predecessor reasoning-session continuity; exact A session resumed across tasks; repository code state independently rematerialised at each historical PRE.
- Condition B: fresh independent reasoning session for every task; same historical PRE and byte-identical matched task prompt.
- Generated experimental code never carried between tasks.

Model/runtime used for P1:

- model: `gpt-5.6-luna`
- Codex CLI: `codex-cli 0.151.0-alpha.7.2`
- config SHA256: `03CD941A69E301F8BD31B19D71C47291613E9C73BBB11BDBEAB20A746B49943E`
- timeout: 1800 seconds/run
- one genuine model attempt per condition-task
- no model-quality retry after model activity began

### P1 frozen run outputs

- B1: `55EFE1FD3FA35EB4A16E857D302ED4C166D138FE6C13C104D740BDD69B67E7BD`
- A1: `7CFD005F40D578A4B3232A95DA3B55E36C487D3F2FF7BC47DE390E83E32D8661`
- A2: `962A94BD70FF1314E2E070AEBD3C41DD15AE0FC53CC31CDB9592E0EAD8688BDC`
- B2: `7E88A7666D10224DBD831D9CBC8E985FB98FD4AE4AF3DF05A4051F9435778901`
- B3: `78FB304A25F4FC6CE89F35BB14FCDA35D432EC997A00FFB73D5917A0106DA63D`
- A3: `3ACFA6855D82F499EC5356E08B91A89B3B5657D1C33BF59DC6DD7AF76EF7677D`

P1 six-run blinded freeze manifest:

`F426272137C6A39E6D1B60361B1792365853C70DD979036BB92C539768822D3C`

Raw adjudication manifest:

`5B80CB2655B974149C89F086A1135F47C6427009A2525EB5ABA5F9A686710DF5`

Interpretation manifest:

`3952AC8FD23A95BAD54DB67300F701B14D53F27CC4D078FA68D25BACEF869BAF`

### P1 raw result

| Task | Persistent A | Fresh B | Paired difference |
|---|---:|---:|---:|
| WP04 | 8/8 | 8/8 | 0 |
| WP05 | 10/10 | 10/10 | 0 |
| WP06 | 0/12 | 0/12 | 0 |
| **Total** | **18/30** | **18/30** | **0** |

Matched behaviour-vector agreement: **30/30**.

Matched behaviour-vector disagreement: **0/30**.

Observed result: no behavioural correctness difference was observed between persistent-session and fresh-session conditions in these three matched tasks.

This is **not** a proof of equivalence or non-inferiority.

WP06 was classified with high confidence as a **common foundational-capability omission**, affecting both conditions rather than showing a differential session-continuity effect.

P1 bounded interpretation: **supportive with limitations**.

P1 supports bounded evidence that fresh reasoning can reconstruct from authoritative repository state without observed behavioural loss in this small three-task sample. It does not establish universal repository sufficiency, cross-repository generalisation, formal equivalence/non-inferiority or resource-cost superiority.

## P2 — accepted design

Private planning root:

`C:\Kyntic\ras-p2-planning\subject-b-p2-v1`

Accepted design result:

- complete historical candidate pool: 10
- eligible: 5
- excluded: 5
- selection rule: **all eligible candidates in the historical inventory window, ordered by POST date then commit ID**
- outcome-based exclusions: 0
- substitutions: 0
- complexity composition: 3 LOW, 2 MEDIUM, 0 HIGH
- recommended repetitions: 3
- Condition A runs: 15
- Condition B runs: 15
- total planned P2 model runs: 30
- Condition A topology: three independent five-task persistent chains
- Condition B topology: fifteen independent fresh sessions
- primary analysis unit: matched task × repetition outcome
- primary endpoint: task-level qualified hidden behavioural success and paired A-B difference
- formal non-inferiority: **not justified for P2; descriptive replication**
- blindness: freeze all 30 outputs before hidden verdict release
- retry: infrastructure-only before model activity; no model-quality retry after activity
- telemetry: remediated/durable resource telemetry required

Important limitation: the objectively eligible P2 pool contains **no HIGH-complexity task**. P2 must not be used to claim independent replication of the highest-complexity stratum.

## Active work package — item 59

Codex is currently running the accepted prompt:

**P2 TASK-SELECTION FREEZE AND NEUTRAL CONTRACT CURATION**

The worker must:

1. hash/bind the accepted P2 design inputs;
2. mechanically recompute 10 candidates → 5 eligible / 5 excluded;
3. freeze the exact five selected tasks as `P2_T01`..`P2_T05`;
4. bind PRE/POST commits and trees;
5. prove materialisability and future-history isolation feasibility;
6. freeze objective complexity classifications (3 LOW, 2 MEDIUM, 0 HIGH);
7. curate neutral task specifications from legitimate pre-implementation evidence;
8. curate governing behavioural contracts;
9. create task-contract mappings and fairness audits;
10. create deterministic private task-selection and curation freeze packages;
11. produce public-safe local drafts;
12. make **zero** P2 experimental model invocations;
13. leave hidden-verifier implementation for the next work package.

Expected successful next step from Codex:

`COORDINATOR_ACCEPT_P2_TASK_SELECTION_AND_CONTRACT_FREEZE; PUBLISH_PUBLIC_SAFE_FREEZE; IMPLEMENT_AND_QUALIFY_P2_SEMANTIC_HIDDEN_VERIFIERS`

When this worker returns, the coordinator must inspect the exact five task identities and contract counts before publishing anything.

## Next gates after active item 59

60. Implement and qualify P2 semantic hidden verifiers for all five frozen tasks.
61. Freeze P2 final preregistration, model/runtime, prompts, random seed/order, execution lock, output-freeze mechanism and blind-adjudication gate.
62. Execute the 30-run P2 experiment.
63. Blind-adjudicate and scientifically interpret P2.
64. Publish/update the paper with Level-2 same-repository replication evidence.
65. Select Subject C and execute cross-repository replication / Level-3 expansion.
66. Final hostile review, claims audit, limitations/statistical audit and reproducibility review.
67. Final paper/reproducibility package and submission-ready release.

## Coordinator/Codex division of labour

Coordinator/ChatGPT owns:

- public/shared GitHub changes;
- research-method decisions and acceptance;
- public-safe evidence publication;
- claim-boundary enforcement;
- exact next Codex work-package prompts.

Codex primarily owns:

- local/private implementation;
- local/private verifier work;
- deterministic historical materialisation;
- experiment execution;
- evidence generation;
- local/private qualification and audits.

Whenever Codex returns a work package, the coordinator must in the same response:

1. assess validity and what was actually proved;
2. make any safe public/shared GitHub changes directly;
3. provide the exact next Codex prompt.

Do not ask separately whether the user wants the next prompt.