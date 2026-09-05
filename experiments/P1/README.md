# P1 — corrected Repository-as-State causal study

Status: **EXECUTED; BLIND-ADJUDICATED; INTERPRETED; PUBLIC-SAFE RESULTS PUBLISHED.**

P1 is the methodology-corrected follow-up to the immutable Subject-B P0 pilot.

The SearchForCars WP04/WP05/WP06 historical chain, neutral task contracts, semantic hidden verifiers, runtime-v3 evidence, prompt bytes, execution order, model/runtime configuration, timeout/retry policy, session-continuity design, metrics contract, output-freeze mechanism and blind-adjudication gate were frozen before execution.

The final preregistration state remains historically bound to commit:

`d95e2cdc47f8082a805fa2d5b09cdb272cf977ef`

Post-experiment publication commits do not alter that preregistered state.

## Core freeze commitments

Overall private verifier package:

`DD8A85151DED2EE5DD11BF27109A5A0823BA2F815474DDE25DCEB33B873784AB`

Private execution-lock JSON:

`9222FBC10DE1977A565EA04CC9EEFE3077F18B58944383851051849DCA466328`

Private execution-lock package:

`951D900DD580CE53F4FA3081E0DFE1707CD6140DF565A3242E11DBCFF8BAD347`

Six-run blinded freeze manifest:

`F426272137C6A39E6D1B60361B1792365853C70DD979036BB92C539768822D3C`

Raw adjudication manifest:

`5B80CB2655B974149C89F086A1135F47C6427009A2525EB5ABA5F9A686710DF5`

Interpretation manifest:

`3952AC8FD23A95BAD54DB67300F701B14D53F27CC4D078FA68D25BACEF869BAF`

Model:

`gpt-5.6-luna`

Execution order:

`B1 -> A1 -> A2 -> B2 -> B3 -> A3`

Timeout:

`1800 seconds per run`

Attempts:

`1 per condition-task`

No model-quality retry was allowed once model inference/tool activity had begun.

## Prompt and session controls

Each matched A/B pair received byte-identical frozen prompts.

Condition A carried only the exact reasoning-session identity from A1 into A2 and A3. Each task still received its own exact historical PRE repository.

B1, B2 and B3 used independent new sessions and independent session stores.

Generated experimental code never carried between tasks.

## Blindness

All six experimental outputs were frozen before any hidden behavioural verdict was inspected.

No correctness feedback from an earlier run was provided to a later run.

## Result

| Task | Condition A | Condition B |
|---|---:|---:|
| WP04_PR5 | 8/8 | 8/8 |
| WP05_PR6 | 10/10 | 10/10 |
| WP06_PR7 | 0/12 | 0/12 |
| **Total** | **18/30** | **18/30** |

The matched behaviour vectors agreed **30/30**, with zero disagreements.

No behavioural correctness advantage for predecessor reasoning-session continuity was observed in this three-task sample. WP06 was classified post-adjudication as a high-confidence common foundational-capability omission affecting both conditions.

Resource evidence is incomplete and mixed, so P1 makes no cost-superiority or cost-equivalence claim.

The bounded public result is recorded in:

- `results/public/subject-b-p1-results-v1.md`
- `results/public/subject-b-p1-results-v1.json`

## Final counters

- `P1_EXPERIMENTAL_AGENT_RUNS=6`
- `P1_EXECUTED=true`
- `P1_ADJUDICATED=true`
- `P1_RESULTS_INTERPRETED=true`
- `P1_PUBLIC_RESULTS_PUBLISHED=true`
- `P0_RERUN=false`

## Interpretation boundary

P1 is supportive with limitations for the narrow proposition tested: fresh reconstruction from the authoritative repository state produced no observed behavioural loss relative to the matched persistent-session condition across these three tasks.

P1 does not establish universal equivalence, formal non-inferiority, universal repository sufficiency, or a resource-cost advantage. Replication on more tasks and independent repositories is required.

Current evidence status:

Subject-B P2 has now completed as a preregistered Level-2 same-repository replication. It observed 0/39 satisfied behaviours in both conditions, 39 matched agreements and no disagreements. This floor effect does not provide positive evidence of successful behavioural preservation; the public Level-2 synthesis is recorded in `results/public/subject-b-p2-level2-evidence-v1.md`.

The next external-validity step is independent cross-repository replication, particularly Subject C.
