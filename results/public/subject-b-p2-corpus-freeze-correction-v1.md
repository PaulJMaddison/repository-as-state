# Subject B P2 corpus-freeze correction v1

Status: **P2 task-selection freeze superseded pending methodology repair**.

No P2 experimental model run has occurred.

## Reason

During genuine candidate-workspace verifier qualification, the exact previously frozen P2_T03 / C08 POST commit:

`a740ce1965ba26ab5e06ed5c466430f1e28c5ac5`

failed compilation before behavioural execution.

The failure is a compile-time interface-contract error (`CS0535`): the historical candidate declares a new `IMarketInventoryRepository` member while the corresponding in-memory and PostgreSQL repository implementations do not implement that member.

A non-buildable POST cannot be treated as a validated accepted boundary under the existing P2 eligibility methodology.

## Consequence

The earlier public P2 task-selection/contract-freeze artifacts remain preserved as historical records but are **not eligible for final P2 preregistration unchanged**.

The P2 corpus selection stage has been reopened before any experimental run.

The repair will be append-only and auditable. It will determine whether:

1. a different contemporaneous historical commit is the legitimate accepted POST for C08; or
2. C08 must be reclassified ineligible under the already-existing accepted-boundary criteria.

No excluded task will be substituted merely to preserve a target task count.

Every task remaining eligible after repair must have its exact historical POST mechanically build/execution-validated before the corrected corpus is frozen.

## Preserved identities

Initial P2 design-input manifest:

`D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`

Initial task-selection freeze:

`829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`

Initial curation package:

`5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

These hashes remain useful to identify the superseded initial freeze; they are not the final P2 preregistration identities.

P2 experimental runs at correction: **0**.