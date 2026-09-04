# Subject-B P2 item-62 hidden-material isolation blocker

Item 62 began under the accepted item-61 execution lock. Before any accepted experimental unit completed, the first unit with genuine model activity demonstrated that the experimental identity could read private item-60 hidden-verifier/qualification material. This falsifies the previously accepted hidden-material access boundary.

The active run was terminated immediately after the breach was confirmed. No hidden verifier was executed and no partial correctness adjudication was performed, but correctness-related private information had been exposed to the experimental session. The contaminated attempt is therefore excluded from scientific evidence and is not retryable under the existing preregistration.

Execution state at stop:

- accepted experimental units completed: 0
- units with genuine model activity: 1
- units not executed: 23
- hidden verifier runs: 0
- partial correctness adjudications: 0
- P2 execution accepted: false

Methodology consequence:

- item 60 is reopened only for the hidden-material isolation/access-control gate; the already-qualified 13 semantic verifier behaviours are not re-curated or changed without new evidence;
- item 61 is no longer execution-authoritative because its lock depended on an isolation claim now falsified by live execution;
- item 62 is blocked and may not continue from the next schedule slot;
- the current execution instance is abandoned rather than selectively retried;
- after isolation is repaired and proven against the real experimental identity, a fresh preregistration/public commitment/execution lock is required before any new model activity.

Private preserved evidence identities:

- contaminated event log SHA-256: `CB8CB6A38424A4D8BFADDAFCCB943BF600775F727A00B9FD7EC51DB03026CBCA`
- partial candidate manifest SHA-256: `7E72A6004BA07C43A61765E84CC6A3A43CAB445B0945516587DDCF03B0DA31D3`

No private verifier implementation, sealed mapping, schedule or correctness result is disclosed here.
