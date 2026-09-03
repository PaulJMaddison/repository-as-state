# Final SearchForCars Subject-B recovery audit

Status: corpus curation only. No P0 execution.

## Trigger

The preferred natural PR8-base split is closed. Exact PR8 base `b818d5e50c588113529c5545843446618dba4e4e` restores but fails the deterministic build gate with two CA1512 analyzer errors, so it is not an accepted engineering boundary.

This does **not** make intermediate redness itself an acceptance criterion. It only means that particular SHA cannot be used as the state separating two P0 tasks.

## Final allowed SearchForCars recovery search space

No further SHA search is allowed.

The only remaining accepted historical endpoints that may be reviewed for a three-task chain are:

- B4: `96aa7162faa48e47104916331a9ffcfd66af7171`
- accepted PR8 merge: `575dc1e531c2a5e6bf39579869720fb8c6deff76`
- B5 / PR7 merge: `83b5b3c98213c13e2d81b33ade63891effcf204d`

Together with existing WP05, the only remaining prospective chain is:

1. WP05_PR6
2. `RC03_B4_TO_PR8_COMPOSITE`: B4 -> PR8
3. `RC04_PR8_TO_B5_REMAINDER`: PR8 -> B5

## Critical scientific rule

The existence of accepted endpoints is not enough.

Each interval must independently pass a **coherent-work-package audit** based on historical intent and actual engineering scope before any new task contract is frozen.

A candidate is coherent only if its changes can be represented honestly as one defensible engineering objective/work package rather than a convenient bundle assembled to obtain chain length.

Evidence may include:

- historical PR/branch intent;
- commit chronology;
- committed product/architecture/session documentation;
- relationship between sub-programmes;
- whether the accepted endpoint represents a meaningful completion/checkpoint for that objective.

Do not use hidden PRE/POST discriminator outcomes when deciding coherence.

## Stop rule

If either B4 -> PR8 or PR8 -> B5 is not defensibly coherent:

- do not search another internal commit;
- do not broaden or rename the task to hide unrelated work;
- do not weaken the minimum task count;
- stop SearchForCars as the primary three-task P0 corpus and return to corpus/protocol design.

If both are coherent, freeze neutral task specifications and hidden behavioural requirements for both **before** any discriminator run.

No experimental A/B agent may run during this audit.
