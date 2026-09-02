# P0 protocol amendment 002: validated sequential subchain size

Status: frozen for corpus review; the P0 experiment remains unexecuted.

## Reason

Executable pre-experiment validation invalidated one selected historical
boundary. The original exact-five-task pilot shape is therefore no longer
viable without changing the corpus window or weakening acceptance. Neither is
permitted.

## Amended selection rule

Within the original frozen candidate programme, P0 uses the longest valid,
dependency-preserving sequential subchain, subject to:

- maximum task count: 5;
- minimum task count: 3;
- every selected task must independently satisfy frozen PRE FAIL / POST PASS;
- chronological order, genuine dependency, neutral wording, equivalent
  implementation tolerance, deterministic local verification, and future-history
  isolation remain mandatory;
- no later history is added and no task is selected for anticipated RaS
  performance.

If equal-length valid chains remain, select deterministically by lexicographically
earliest candidate transitions, then by earliest ending transition.

This reduces corpus size after an objective boundary rejection. It does not
inspect or use any experimental outcome, and it does not change the frozen
behavioural requirements, original candidate window, inclusion/exclusion rules,
or dependency standard.

If no valid chain of at least three tasks exists, the corpus is insufficient and
P0 must not proceed.

## Current disposition

- `CORPUS_AMENDMENT_REQUIRED=true`
- `ORIGINAL_T3_BOUNDARY_VALID=false`
- `FROZEN_BEHAVIOURAL_REQUIREMENTS_CHANGED=false`
- `EXPERIMENTAL_AGENT_RUNS=0`
- `P0_EXECUTED=false`
- `NETWORK_ISOLATION_READY=false`
