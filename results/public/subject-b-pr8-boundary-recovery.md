# Subject-B PR8 boundary recovery

Ancestry was reproduced: B4 is an ancestor of PR8, and PR8 is an ancestor of B5. A fresh PR8 workspace restored successfully and built successfully with zero warnings and errors.

The earlier reported discovery count of 302 is now classified as a **measurement/parser error**, not a repository-state change. That count was produced by a fallback that counted arbitrary indented `dotnet test --list-tests` output lines when no `Total Tests` summary matched. A later strict parser that accepts only fully-qualified `SearchForCars.Tests.*` test names produced exactly 300 unique tests with ordered-list SHA256 `02c78ff3b90665fb183a63eb1280b2b92c405a934c36bb67e7448d95f1d28eaa`.

This corrected count is independently consistent with the contemporaneous PR #8 validation record, which recorded 300 tests passed, 0 failed and 0 skipped before merge.

The monolithic project run remains disclosed as a harness caveat: it produced 292 terminal passing results and no failures or skips before stalling, leaving 8 of the corrected 300-test inventory unaccounted for in that monolithic run. It is not rewritten as a pass.

The frozen v2 partitioned replay completed all 12 consecutive batches. One top-level batch stalled and was resolved by the required midpoint bisect; its two child runs accounted for all members. Leaf TRX outcomes account for exactly 300/300 tests: 300 passed, 0 failed and 0 skipped. PR8 is therefore **ACCEPTED_WITH_HARNESS_CAVEAT**. The next step is to freeze PR8 split task contracts. No replacement candidate contracts are frozen and no new discriminator has run.

This aggregate contains no private paths, source, hidden requirements, or proprietary test traces.
## Natural next split

Before freezing replacement contracts, the recovery plan now prefers the exact historical PR #8 base/first-parent boundary `b818d5e50c588113529c5545843446618dba4e4e`. This avoids treating the entire B4 -> PR8 interval as one broad composite task. If the PR8-base state validates as an accepted boundary, the natural three-task chain becomes existing WP05 followed by B4 -> PR8-base and PR8-base -> PR8 merge. If that base state is not accepted, the broad interval will not be collapsed merely to preserve chain length.

