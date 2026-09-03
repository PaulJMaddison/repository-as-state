# Subject-B v2 final verification record

Status: corpus preparation / review only. No P0 execution or experimental-agent run occurred.

## Frozen history

- Frozen remote main: `83b5b3c98213c13e2d81b33ade63891effcf204d`
- Frozen tree: `96aafb77cc02008413115013d3411b6c83103965`
- First-parent history digest: `ffbb95eeedb3304f1156c6c84a926fda030bacc500dde746c788108b080b0f85`
- History window version: 2

## Candidate outcomes

| Candidate | PRE | POST | Negative control | Result |
|---|---|---|---|---|
| WP02_PR2 | FAIL | PASS | DETECTED | valid narrow verifier candidate |
| WP03_PR4 | PASS | PASS | not applicable | rejected: PRE already satisfies discriminator |
| WP04_PR5 | FAIL | PASS | DETECTED | valid narrow verifier candidate |
| WP05_PR6 | FAIL | PASS | DETECTED | valid narrow verifier candidate |
| WP06_PR7 | FAIL | PASS | DETECTED | valid narrow verifier candidate |

The narrow verifier chain proposed for review is `WP04_PR5 -> WP05_PR6 -> WP06_PR7`, length 3. Boundary identity checks are true: WP04 POST equals WP05 PRE, and WP05 POST equals WP06 PRE.

## Completeness gate

The narrow verifiers do not cover every frozen behavioural requirement. Requirement counts are WP04=8, WP05=9, and WP06=12; the comprehensive verifier implementation gate is therefore not passed. This record must not be interpreted as final-lock approval or as an empirical P0 result.

The final private-lock gate remains closed pending comprehensive, independently reproducible offline verifiers and their negative controls.

## Safety and provenance

- Experimental agent runs: 0
- P0 executed: false
- Final lock created: false
- SearchForCars product repository: unchanged
- Public research record: this sanitized aggregate only
- Hidden verifier implementations, private source snapshots, raw logs, private workspace paths, and credentials: intentionally excluded

## Latest WP04 comprehensive-verifier attempt

A later privileged WP04-only implementation run did not create the comprehensive verifier. It evaluated 0 of 8 frozen requirements, produced no valid PRE/POST comprehensive observations, ran no comprehensive negative controls, and left the final-lock gate closed.

This is recorded as an **incomplete preparation execution**, not a scientific rejection of WP04. The prior narrow WP04 discrimination result remains preserved. The next worker must implement the WP04 comprehensive verifier rather than repeat the coverage audit.

See:

- `results/public/subject-b-wp04-comprehensive-status.md`
- `results/public/subject-b-wp04-comprehensive-status.json`
## Chain status after WP04 direct discriminator probes

WP04_PR5 is now comprehensively rejected for P0 task discrimination: all eight already-frozen requirements produced PRE=PASS and POST=PASS under direct supervised micro-probes. No v3 was created. The previous three-task review chain is therefore no longer valid; the surviving contiguous main-boundary chain is WP05_PR6 -> WP06_PR7 (length 2).

A transparent recovery candidate exists in the already-recorded historical development graph: merged PR #8 (`575dc1e531c2a5e6bf39579869720fb8c6deff76`) is a pre-existing reviewed work-package boundary that is a descendant of B4/PR6 merge (`96aa7162...`) and an ancestor of B5/PR7 merge (`83b5b3c...`). It may allow the broad B4->B5 interval to be split into two natural accepted transitions.

This is **not yet a valid task**. The next corpus-preparation step is to validate PR #8 as an accepted engineering boundary and, only if accepted, freeze neutral task contracts for the two natural intervals before running any new behavioural verifier. Arbitrary internal commits must not be searched for merely to manufacture a third task.

