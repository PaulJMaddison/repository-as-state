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
