# P0 corpus boundary amendment 001

Status: accepted for corpus review; the P0 experiment remains unexecuted.

## Reason

Independent Rust reproduction of the selected identity-lifecycle post-state did
not satisfy two already-frozen behavioural requirements: changing an alias must
retire the old alias from active matching while preserving the canonical entity,
and a tombstoned alias must not be inherited by a later unrelated record.

The failure was reproduced directly from a fresh isolated historical workspace,
not inferred from the public harness or from a verifier-only result. A
chronological walk through the remaining states in the bounded local history
did not establish an accepted identity-lifecycle boundary. The public harness
therefore must not treat the original boundary as valid merely because the
historical state is reproducible or committed.

## Amendment

The original frozen task requirements, task wording, ordering rule, and five-unit
pilot budget are unchanged. The corpus boundary is rejected for the affected
identity-lifecycle unit. Before any preregistration freeze, task selection must
be rerun oldest-to-newest using this clarification:

> A proposed accepted boundary must pass the complete frozen behavioural
> acceptance contract in an independent direct implementation check. A
> compile-only state, a state passing only newly introduced tests, or a state
> whose active identity indexes retain retired aliases is not an accepted
> boundary.

The replacement selection must preserve the same public/private separation,
future-history exclusion, and negative-control requirements. If no replacement
boundary satisfies the contract inside the predeclared corpus window, the P0
corpus remains unready and the experiment must not start.

The reselection pass did not produce a defensible amended five-task chain. The
original T3 unit is recorded as
`EXCLUDED_INVALID_ACCEPTED_BOUNDARY_DISCOVERED_DURING_PREPARATION`; downstream
selection was not promoted to a final chain because the required replacement
eligibility and dependency checks were not all satisfied. The corpus therefore
stops at `P0_CORPUS_INSUFFICIENT_AFTER_BOUNDARY_VALIDATION=true`.

## Current disposition

- `FROZEN_T3_REQUIREMENTS_CHANGED=false`
- `P0_EXECUTED=false`
- `EXPERIMENTAL_AGENT_RUNS=0`
- `NETWORK_ISOLATION_READY=false`
- No private commit identifiers, lock material, implementation details, or
  result-judge information are disclosed here.
