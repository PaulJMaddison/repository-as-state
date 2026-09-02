# P0 runbook — preparation state

**DO NOT EXECUTE P0 UNTIL THE READINESS CHECKLIST IS COMPLETE AND THE PREREGISTRATION IS FROZEN.**

This runbook records the intended order only.

## Preparation phase

1. Build private hidden verifiers in a location outside the public repository and outside experimental workspaces.
2. Build isolated historical workspaces from the private lock payload.
3. Run the FUTURE_HISTORY_LEAK_GATE on every workspace with private forbidden future OIDs supplied by the privileged preparation process.
4. Freeze exact visible model/configuration, system instructions, tools/permissions, per-task budget, telemetry, account-memory control, cache policy, network policy, and verifier hashes.
5. Resolve `P0_CAUSAL_RUNTIME_ELIGIBLE`.
6. Complete the readiness checklist.
7. Canonicalise the final preregistration.
8. Create the final preregistration lock and deterministic condition order.
9. Only then may a new, non-curator experimental session execute P0.

## Per-task boundary procedure

For every task in either A or B:

1. start from the same accepted state for that task;
2. create a fresh isolated workspace;
3. apply identical environment/cache policy;
4. verify workspace cleanliness;
5. run FUTURE_HISTORY_LEAK_GATE;
6. stop before model invocation if the gate fails;
7. inject byte-identical stable experiment instructions and task specification across A/B;
8. apply the condition-specific reasoning-history treatment;
9. enforce the same frozen resource budget;
10. allow normal visible repository tests;
11. prevent access to hidden verifier source/failure details;
12. at submission, run the hidden verifier once under its frozen contract;
13. record telemetry and failure classification;
14. if accepted, freeze the next canonical state and destroy the workspace.

## Condition A

Retain predecessor reasoning-session history across tasks. Do not retain filesystem/process residue.

## Condition B

Destroy predecessor reasoning-session state after every accepted task. A fresh session receives no summary, curator notes, prior reconstruction report, resume token, or future solution information.

Before editing, record the structured reconstruction probe outside the workspace.

## Human intervention

No hints, manual fixes, file pointers, cross-condition information, prompt improvements after failure, hidden-verifier details, or selective reruns.

## Reruns

A rerun is potentially eligible only for an objectively frozen harness/provider/environment failure category. Agent/task/verifier failure is not rerun simply because it is undesirable.

## Results discipline

P0 may end only as methodology failure, evidence against RaS, mixed/conditional evidence, or supportive pilot evidence. Never “proven”.
