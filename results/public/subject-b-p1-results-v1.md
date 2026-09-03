# Subject-B P1 results — bounded public record

Date: 2026-09-03

## Status

P1 execution, blind adjudication and scientific interpretation are complete.

This file is a public-safe summary. Private hidden-verifier implementation details and private oracle diagnostics are intentionally omitted.

## Frozen identities

- preregistration state commit: `d95e2cdc47f8082a805fa2d5b09cdb272cf977ef`
- overall private verifier package: `DD8A85151DED2EE5DD11BF27109A5A0823BA2F815474DDE25DCEB33B873784AB`
- execution-lock JSON: `9222FBC10DE1977A565EA04CC9EEFE3077F18B58944383851051849DCA466328`
- public preregistration binding: `8BC653E42A4B5049F2BBDA6AE0B92D25A8980C03C5E3DE34F3514103612B4A5D`
- six-run blinded freeze manifest: `F426272137C6A39E6D1B60361B1792365853C70DD979036BB92C539768822D3C`
- raw adjudication manifest: `5B80CB2655B974149C89F086A1135F47C6427009A2525EB5ABA5F9A686710DF5`
- interpretation manifest: `3952AC8FD23A95BAD54DB67300F701B14D53F27CC4D078FA68D25BACEF869BAF`

Model: `gpt-5.6-luna`

Frozen run order: `B1 -> A1 -> A2 -> B2 -> B3 -> A3`.

Condition A retained predecessor reasoning-session continuity across tasks while receiving a freshly materialised historical PRE repository for every task. Condition B used a new independent reasoning session for every task. Generated candidate code never carried between tasks.

## Raw behavioural result

| Task | Condition A: persistent session | Condition B: fresh session |
|---|---:|---:|
| WP04_PR5 | 8/8 | 8/8 |
| WP05_PR6 | 10/10 | 10/10 |
| WP06_PR7 | 0/12 | 0/12 |
| **Total** | **18/30** | **18/30** |

The paired behaviour vectors agreed on all 30 governing behaviours: **30 agreements, 0 disagreements**.

Task-level outcomes were also matched: both conditions passed WP04 and WP05 and failed WP06.

No behavioural correctness advantage for predecessor reasoning-session continuity was observed in this three-task sample.

## WP06

WP06 failed all 12 governing behaviours in both conditions. Post-adjudication analysis classified this, with high confidence, as a **common foundational-capability omission** rather than a differential session-continuity effect.

The historical POST remains a qualified passing control for the same frozen verifier. The detailed private oracle evidence is not published here.

## A1 interruption

A1 was interrupted after genuine model activity. Under the preregistered retry rule it was frozen and was not rerun. It later passed all 8 WP04 governing behaviours. The interruption therefore remains part of the experimental record and limits complete resource comparison for that pair because some A1 telemetry is unavailable.

## Resource evidence

Resource/reconstruction evidence is incomplete and mixed. Missing telemetry is recorded as unavailable rather than estimated. P1 therefore does **not** establish that fresh reconstruction is cheaper, more expensive, or resource-equivalent to persistent-session continuation.

## Bounded interpretation

P1 provides supportive but limited evidence for the narrow Repository-as-State proposition tested here: on these three matched SearchForCars tasks, removing predecessor reasoning-session continuity caused **no observed behavioural loss relative to the matched persistent-session condition**.

The result does **not** prove:

- universal equivalence between fresh and persistent reasoners;
- formal non-inferiority;
- that predecessor reasoning context never matters;
- that repository state is sufficient for every task;
- a resource or monetary cost advantage;
- generalisation beyond this repository, model, task sample or protocol.

The observed pattern varies by task, not by condition: both conditions succeeded on WP04/WP05 and both failed on WP06. Replication on more tasks and independent repositories is required.

## Relationship to P0

P0 remains `MIXED_METHODOLOGY_AND_MODEL_FAILURE` and non-causally-interpretable for A/B correctness. P1 is the methodology-corrected controlled study and does not retroactively rehabilitate P0.

## Next evidence step

Freeze a P2 replication protocol before execution, preserving the paired treatment definition while expanding task count and repository diversity. WP06-like tasks should be considered as an explicit higher-complexity stratum rather than being removed post hoc.
