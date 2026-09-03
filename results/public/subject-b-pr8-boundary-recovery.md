# Subject-B PR8 boundary recovery

Ancestry was reproduced: B4 is an ancestor of PR8, and PR8 is an ancestor of B5. A fresh PR8 workspace restored successfully and built successfully with zero warnings and errors.

Independent discovery found 302 tests. The isolated project run did not complete before the prescribed 45-second stall timeout; it produced 292 terminal passing results and no failures or skips, leaving 10 tests unaccounted for. Hang diagnostics marked `ProductActivityAcceptsWhitelistedNonPiiEvents` incomplete, but that test passed in isolation, so the exact project-level runner/fixture interaction remains unresolved. PR8 is neither accepted nor rejected on product behavior grounds.

That evidence does **not** establish a passing accepted boundary, but it also does not establish a failing repository boundary. The observed failure is currently a harness/completion failure. PR8 is therefore classified as `UNRESOLVED_HARNESS_STALL`, not accepted and not scientifically rejected.

No replacement candidate contracts are frozen and no new discriminator has run. The next step is a narrow diagnostic of the test-run completion path: establish the expected discovered test count, isolate any non-terminating test/project or post-test teardown process, and then rerun the accepted-boundary gate without changing PR8.

This aggregate contains no private paths, source, hidden requirements, or test traces.
