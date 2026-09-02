# Research questions — hostile-audit revision

## RQ1 — Post-acceptance continuity

For genuinely dependent software-engineering tasks, what is the effect of removing predecessor high-capability reasoning-session history **after a validated accepted project transition**, when accepted repository state, current task, model/configuration, tools and environment are otherwise matched?

P0 tests whether this treatment can be isolated. Later repeated studies may test a preregistered non-inferiority/equivalence claim.

## RQ2 — Reconstruction burden

How much repository rediscovery is required after forced reset?

Measure:
- reconstruction input tokens;
- repository bytes/files read;
- searches/navigation operations;
- model/tool calls;
- reconstruction and total elapsed time;
- retries;
- observable cache usage.

A valid result may be: **reset succeeds but reconstruction is more expensive than retaining predecessor history**.

## RQ3 — Durable semantic carriers

Which allowed project artefacts have marginal continuity value at accepted boundaries?

Candidate classes include source, tests, Git history, architecture records, concise state documentation, schemas and reproducible build information.

Condition C must use small preregistered ablations rather than arbitrary repository degradation.

## RQ4 — Scaling and portability

How do reset effects vary with:
- sequential depth;
- repository size;
- task locality;
- dependency width;
- documentation/test quality;
- retrieval method;
- model family?

Cross-model continuity and tiered execution are later research questions, not P0's primary treatment.
