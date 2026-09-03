# Post-P0 remediation v1

This document governs remediation after Subject-B P0. It does not amend or
retroactively repair P0.

## Runtime candidate

The next runtime candidate must materialise each historical PRE as a local
writable branch whose tree and commit identity are independently verified.
The workspace must contain no remote, no future refs, no unreachable future
objects and no private control-plane material.

The runtime must also prove that the repository's deterministic local build and
test prerequisites are available without granting general network access.
Offline dependency/cache provisioning is permitted only as non-source tooling
state and must be identical across conditions.

Synthetic and historical-state infrastructure probes are allowed. Experimental
task-solving model invocations are not.

## Task-contract rule for the next experiment

For each candidate task, freeze a requirement matrix before execution:

`task-spec statement -> governing verifier behaviour -> derivation class`.

Every governing behaviour must be either:

- `EXPLICITLY_REQUIRED_BY_TASK_SPEC`, or
- `REASONABLY_ENTAILED_BY_TASK_SPEC`.

If any governing behaviour is `NOT_REASONABLY_DERIVABLE_FROM_TASK_SPEC`, the
task is ineligible for the next causal experiment.

The verifier may remain hidden and implementation-independent. The behavioural
requirement itself may not be hidden.

## P0 preservation

The six P0 outputs, verdicts and hashes are permanent historical evidence.
No remediation may overwrite or rerun them. A corrected experiment must use a
new version identifier and new preregistration.
