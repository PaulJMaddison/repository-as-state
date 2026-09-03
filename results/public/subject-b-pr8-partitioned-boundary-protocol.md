# PR8 partitioned accepted-boundary replay protocol v1

Status: **frozen curation protocol amendment; no P0 execution**.

## Why this amendment exists

The exact historical PR8 tree restores and builds successfully. The monolithic test-project run discovers 302 tests but stalls after 292 terminal passing results, with zero reported failures or skips. The first incomplete test identified by hang diagnostics passes when run alone. This establishes a harness/fixture interaction ambiguity, not an accepted boundary and not a proven product failure.

The original monolithic-run evidence remains preserved and must not be rewritten as a pass.

## Hindsight disclosure

Before this protocol was frozen, one test identified as incomplete in the monolithic run was executed in isolation and passed. That diagnostic observation is preserved as hindsight exposure. It cannot be used by itself to accept PR8.

The protocol therefore requires **all 302 discovered tests, including that already-observed test, to be replayed again under the same frozen rules**.

## Frozen replay rule

1. Use exact PR8 commit `575dc1e531c2a5e6bf39579869720fb8c6deff76` and tree `4d777a99f1f5b43d8123d221616a1f9688da8b2e`.
2. Do not modify product or test source.
3. Perform test discovery once and persist the complete fully-qualified test list privately.
4. Sort the discovered test names ordinally and SHA256-hash the exact ordered list before executing the replay.
5. Require the frozen discovery count to equal 302. If it does not, stop as a discovery-reproducibility failure.
6. Partition the frozen ordered list mechanically into consecutive batches of at most 25 tests. The partition algorithm is fixed by list order and batch size, not by test outcome.
7. Execute each batch in a fresh `dotnet test` process with no build/restore, a machine-readable result artefact, bounded stall/hard deadlines, and no source changes.
8. If a batch stalls, bisect only that frozen batch mechanically until the exact non-terminating test or interaction is identified. Do not change the test list or acceptance rule.
9. Every one of the 302 frozen discovered tests must receive one terminal outcome in the replay accounting.

## Boundary adjudication

PR8 may be classified `ACCEPTED_WITH_HARNESS_CAVEAT` only if all of the following hold:

- contemporaneous historical review evidence records the PR8 work package as validated;
- current restore passes;
- current build passes;
- frozen discovery count is 302;
- all 302 tests are terminally accounted for under the frozen partitioned replay;
- failed tests = 0;
- no product/test source was changed to obtain the result.

The original monolithic runner stall remains a disclosed reproducibility caveat and is not erased.

PR8 is `REJECTED` if a frozen replay test deterministically fails or a required test itself cannot complete when isolated under the frozen replay.

PR8 remains `UNRESOLVED_HARNESS_STALL` if exhaustive frozen replay still cannot account for all 302 tests without establishing a product/test failure.

## Experimental boundary

This protocol is corpus curation only. It does not run A/B agents, does not create the final P0 lock, and is not positive empirical evidence for Repository-as-State.
