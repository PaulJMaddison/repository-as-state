# Subject-B PR8 boundary recovery

Ancestry was reproduced: B4 is an ancestor of PR8, and PR8 is an ancestor of B5. A fresh PR8 workspace restored successfully and built successfully with zero warnings and errors.

Independent discovery found 302 tests. The isolated project run did not complete before the prescribed 45-second stall timeout; it produced 292 terminal passing results and no failures or skips, leaving 10 tests unaccounted for. Hang diagnostics marked `ProductActivityAcceptsWhitelistedNonPiiEvents` incomplete, but that test passed in isolation, so the exact project-level runner/fixture interaction remains unresolved. PR8 is neither accepted nor rejected on product behavior grounds.

No replacement candidate contracts were frozen, no new discriminator was run, and no arbitrary SHA was searched. This aggregate contains no private paths, source, hidden requirements, or test traces.
