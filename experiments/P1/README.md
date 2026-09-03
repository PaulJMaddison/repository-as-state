# P1 — corrected Repository-as-State causal study

Status: **PUBLICLY PREREGISTERED; PRIVATE EXECUTION LOCK FROZEN; ZERO EXPERIMENTAL RUNS.**

P1 is the methodology-corrected follow-up to the immutable Subject-B P0 pilot.

The SearchForCars WP04/WP05/WP06 historical chain, neutral task contracts, semantic hidden verifiers, runtime-v3 evidence, prompt bytes, execution order, model/runtime configuration, timeout/retry policy, session-continuity design, metrics contract, output-freeze mechanism and blind-adjudication gate are now frozen.

## Core freeze commitments

Overall private verifier package:

`DD8A85151DED2EE5DD11BF27109A5A0823BA2F815474DDE25DCEB33B873784AB`

Private execution-lock JSON:

`9222FBC10DE1977A565EA04CC9EEFE3077F18B58944383851051849DCA466328`

Private execution-lock package:

`951D900DD580CE53F4FA3081E0DFE1707CD6140DF565A3242E11DBCFF8BAD347`

Model:

`gpt-5.6-luna`

Execution order:

`B1 -> A1 -> A2 -> B2 -> B3 -> A3`

Timeout:

`1800 seconds per run`

Attempts:

`1 per condition-task`

No model-quality retry is allowed once model inference/tool activity has begun.

## Prompt and session controls

Each matched A/B pair receives byte-identical frozen prompts.

Condition A carries only the exact reasoning-session identity from A1 into A2 and A3. Each task still receives its own exact historical PRE repository.

B1, B2 and B3 use independent new sessions and independent session stores.

Generated experimental code never carries between tasks.

## Blindness

All six experimental outputs must be frozen before any hidden behavioural verdict is inspected.

No correctness feedback from an earlier run may be provided to a later run.

## Current counters

- `P1_EXPERIMENTAL_AGENT_RUNS=0`
- `P1_EXECUTED=false`
- `P0_RERUN=false`

Final preregistration: `experiments/P1/preregistration-v1.yaml`.

Current next step:

`BIND_PUBLIC_PREREGISTRATION_COMMIT_AND_FINAL_ZERO_MODEL_PREFLIGHT`

P1 must not begin until the private pre-model gate is bound to this preregistration commit and the final zero-model preflight passes.
