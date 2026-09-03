# PR8 partitioned accepted-boundary replay protocol v2

Status: **frozen curation protocol amendment; no P0 execution**.

## Amendment reason

Protocol v1 required 302 discovered tests. That requirement is superseded because the 302 figure was produced by an invalid discovery-count parser.

The earlier diagnostic code used this fallback when no `Total Tests` summary was matched:

`count = number of all indented output lines`

That parser was not restricted to test identifiers and therefore could count non-test output as tests.

Before any partitioned replay batch was executed, a stricter discovery pass extracted only fully-qualified `SearchForCars.Tests.*` names, deduplicated them and sorted them ordinally. It produced:

- authoritative discovered test count: **300**
- ordered discovered-test-list SHA256: `02c78ff3b90665fb183a63eb1280b2b92c405a934c36bb67e7448d95f1d28eaa`

This corrected count is independently corroborated by the contemporaneous PR #8 merge record, which states that 300 tests passed, 0 failed and 0 skipped during the historical review.

No replay batch had started when the mismatch was discovered. Therefore v2 corrects a measurement error before outcome-producing replay execution; it does not change the candidate, source, test set or acceptance rule in response to replay outcomes.

Protocol v1 remains preserved as historical evidence and must not be rewritten.

## Hindsight disclosure

One test that the monolithic hang diagnostics marked incomplete was already executed in isolation and passed before v1/v2 replay. That diagnostic observation remains disclosed. It cannot be used by itself to accept PR8.

All 300 authoritative discovered tests, including that already-observed test, must be replayed under the same frozen v2 rules.

## Frozen authoritative inventory

Candidate commit:
`575dc1e531c2a5e6bf39579869720fb8c6deff76`

Candidate tree:
`4d777a99f1f5b43d8123d221616a1f9688da8b2e`

Expected fully-qualified test count:
`300`

Expected ordered test-list SHA256:
`02c78ff3b90665fb183a63eb1280b2b92c405a934c36bb67e7448d95f1d28eaa`

The private `discovered-tests.txt` used for replay must hash to this exact value before any batch executes.

If the count or hash differs, stop as an inventory-integrity failure. Do not rediscover and silently replace the frozen list.

## Frozen replay rule

1. Do not modify product or test source.
2. Verify exact PR8 commit and tree.
3. Verify the private ordered discovered-test list has count 300 and the exact frozen SHA256 above.
4. Partition that frozen list mechanically into consecutive batches of at most 25 tests.
5. Freeze and hash the partition manifest before executing any batch.
6. Execute each batch in a fresh `dotnet test` process with no build/restore and a machine-readable result artefact.
7. Use bounded stall/hard deadlines.
8. If a batch stalls, bisect only that frozen batch mechanically until the exact non-terminating test or minimum interacting subset is identified.
9. Every one of the 300 frozen tests must receive exactly one terminal replay outcome in final accounting.

## Boundary adjudication

PR8 may be classified `ACCEPTED_WITH_HARNESS_CAVEAT` only if:

- contemporaneous historical review evidence records the PR8 work package as validated;
- current restore passes;
- current build passes;
- frozen inventory count = 300;
- frozen inventory hash matches exactly;
- all 300 tests are terminally accounted for in the partitioned replay;
- failed tests = 0;
- no product/test source was changed.

The original monolithic runner stall remains permanently disclosed. The corrected inventory means the monolithic run accounted for 292/300 tests, leaving 8 unaccounted there.

PR8 is `REJECTED` if a frozen replay test deterministically fails or a required test itself cannot complete when isolated under the frozen replay.

PR8 remains `UNRESOLVED_HARNESS_STALL` if exhaustive frozen replay still cannot account for all 300 tests without proving a product/test failure.

## Experimental boundary

This is corpus curation only. It runs no A/B agent, creates no final P0 lock, and is not positive empirical evidence for Repository-as-State.
