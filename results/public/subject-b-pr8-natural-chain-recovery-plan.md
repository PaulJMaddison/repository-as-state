# Subject-B PR8 natural chain-recovery plan

Status: corpus curation only. No P0 execution.

## Accepted evidence

PR8 merge `575dc1e531c2a5e6bf39579869720fb8c6deff76` is accepted with a disclosed harness caveat. Its exact first parent is the pre-existing PR #8 base:

`b818d5e50c588113529c5545843446618dba4e4e`

Its second parent is the reviewed PR #8 implementation head:

`5658fa1ae922afa56ba76f1d8dffd9bd95d60209`

The PR8 merge record identifies the work package as agentic market-acquisition hardening and records 300 passing tests, 0 failures, 0 skips, server build 0 errors/warnings and iOS MAUI green at historical review.

## Preferred sequential decomposition

Do **not** immediately use the broad B4 -> PR8 interval as one task. That interval contains both the product/moat work already present on the PR8 base branch and the PR8 acquisition merge.

The preferred natural sequence is:

1. existing WP05_PR6: `b364a51a... -> 96aa7162...`
2. candidate A: `96aa7162faa48e47104916331a9ffcfd66af7171 -> b818d5e50c588113529c5545843446618dba4e4e`
3. candidate B: `b818d5e50c588113529c5545843446618dba4e4e -> 575dc1e531c2a5e6bf39579869720fb8c6deff76`

This gives three sequential transitions if and only if the PR8-base state is itself a defensible accepted engineering boundary.

The PR8-base SHA is not an arbitrary post-hoc commit: it is the exact historical first parent/base of the already-existing PR #8 merge.

## Mandatory next gate

Before any task contract is frozen or any hidden discriminator runs:

- materialise exact PR8 base `b818d5e5...`;
- verify ancestry and tree identity;
- reproduce restore/build/test health using the same accepted-boundary methodology already used for PR8;
- if a monolithic runner hangs, use the already-frozen deterministic inventory/partition approach rather than changing product/test source;
- preserve any harness caveat explicitly.

If PR8 base is accepted, freeze two neutral task contracts from the actual historical work-package intent **before** running any PRE/POST discriminator.

If PR8 base is not accepted, do not automatically collapse B4 -> PR8 into one broad composite task merely to preserve chain length. Return to corpus review.

## Contract-construction rule

For each accepted candidate transition, task specification and hidden behavioural requirements must be derived from pre-existing historical intent, PR/branch context and externally meaningful behaviour.

Do not choose requirements because they are known to fail PRE or pass POST. Do not run exploratory hidden probes before the contract hashes are frozen.

No experimental A/B agent may run during this curation step.
