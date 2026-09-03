# Subject-B PR8-base boundary recovery

The exact PR8 first-parent base was materialised from the SearchForCars source repository and verified:

- base commit: `b818d5e50c588113529c5545843446618dba4e4e`
- base tree: `f05ef04b8f2443f92ef642e25b3940140084ce13`
- PR8 first-parent and second-parent identities match the recorded values
- B4 is an ancestor of the PR8 base
- restore passes

The historical base build fails deterministically with two analyzer errors (CA1512) and zero warnings. Per the recovery protocol, test discovery and execution did not proceed, candidate contracts remain unfrozen, and no discriminator, experimental agent, or P0 run occurred. The base is rejected as an accepted boundary on build health grounds.

No alternative SHA was searched and the broad B4-to-PR8 interval was not forced. This aggregate contains no private paths, source, hidden requirements, test names, traces, or proprietary material.

Next step: `SUBJECT_B_CORPUS_REVIEW`.
