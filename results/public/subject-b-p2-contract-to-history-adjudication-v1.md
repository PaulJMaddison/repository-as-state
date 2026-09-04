# Subject-B P2 contract-to-history adjudication v1

Status: **VALID_TERMINAL_B — frozen contract repair required before verifier qualification can continue.**

This public-safe record documents the outcome of the private no-build/no-test/no-compile contract-to-history adjudication for the frozen five-task P2 corpus.

## Result

- governing behaviours audited: **18**
- valid behavioural deltas: **9**
- oracle-mapping defects: **4**
- frozen contract defects: **5**
- unresolved: **0**
- P2 experimental model runs during adjudication: **0**

Private adjudication artifact SHA256:

`4A57493EC8B70732C5AFABC71F055153DA423867F32564233FBD1EF59A17D5F5`

Repeat-hash verification: **PASS**.

## Methodological consequence

The previous five-task selection itself is not being silently replaced. Instead, programme item 59 is reopened because five exact frozen governing behaviours were shown by the private audit not to satisfy the required historical PRE→POST behavioural-delta condition.

The remaining 13 behaviours are not invalidated by this result: nine were confirmed valid behavioural deltas and four were confirmed as verifier/oracle seam-mapping defects rather than contract defects.

The next repair step must read the immutable private audit package, identify the exact five defective behaviour IDs, and repair only those disclosed contract mappings/behaviours under the original anti-cherry-picking and no-substitution rules. No experimental P2 model run may occur until item 59 is re-frozen and item 60 is subsequently completed.

This record does not claim that P2 failed. P2 has not executed.
