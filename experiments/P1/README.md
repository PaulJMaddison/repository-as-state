# P1 — corrected Repository-as-State causal study

Status: **WP04 AND WP05 PRIVATE VERIFIERS QUALIFIED AND FROZEN; WP06 SEMANTIC VERIFIER COMPLETE BUT IMPLEMENTATION-INDEPENDENCE QUALIFICATION PENDING.**

P1 does not overwrite, repair or rerun P0. P0 remains immutable historical evidence.

## Central P1 task-contract rule

> **A verifier may be hidden. A requirement may not be hidden.**

The established SearchForCars WP04/WP05/WP06 chain and frozen P1 task contracts remain authoritative.

## Current status

Runtime-v3 remediation is green.

WP04_PR5 is qualified and frozen at:

`F61BEFEE8262FEE42D26DB3AC833E1BE8DB29E5555073CDCA30ABBE6DD996057`

WP05_PR6 is qualified and frozen at:

`5BBE8A480B2453B4EAE6B8AB7769753062E994602CE18F349ABB5B70E8329E4D`

WP06_PR7 now has direct semantic coverage for all 12 frozen behaviours. Its 12 targeted negative controls are detected, PRE fails and POST passes deterministically across three runs, semantic selector/source/diff/commit dependence is absent, and oracle self-tests pass.

WP06 is nevertheless **not qualified for freeze** because no semantics-preserving alternate implementations have yet been executed. The implementation-independence gate therefore remains open.

A provisional WP06 archive hash exists, but it is not a frozen verifier-package commitment and must be replaced after independence qualification.

No P1 task-solving model has run. P0 has not been rerun.

Current next step:

`COMPLETE_WP06_IMPLEMENTATION_INDEPENDENCE_QUALIFICATION_BEFORE_FREEZE`

After WP06 implementation independence passes, rerun the final controls/self-tests, re-freeze WP06, publish the accepted aggregate state, and only then prepare the overall private P1 verifier package freeze and corrected P1 preregistration.
