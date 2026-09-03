# Subject-B PR8 boundary recovery

Ancestry was reproduced: B4 is an ancestor of PR8, and PR8 is an ancestor of B5. A fresh PR8 workspace restored successfully and built successfully with zero warnings and errors.

The frozen rediscovery produced 300 fully qualified test names, while the protocol requires exactly 302. This is a discovery reproducibility failure, so partitioned replay did not start and no tests were counted as terminally accounted in this replay. PR8 remains unresolved rather than accepted or rejected on product behavior grounds.

That evidence does **not** establish a passing accepted boundary, but it also does not establish a failing repository boundary. The observed failure is currently a harness/completion failure. PR8 is therefore classified as `UNRESOLVED_HARNESS_STALL`, not accepted and not scientifically rejected.

No replacement candidate contracts are frozen and no new discriminator has run. No test grouping or alternate commit was selected.

This aggregate contains no private paths, source, hidden requirements, or test traces.
