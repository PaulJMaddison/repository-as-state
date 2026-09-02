# Threats to validity — hostile-audit revision

## Largest threat: treatment confounding

A session reset can also change:
- tool lifecycle;
- filesystem/worktree state;
- shell/IDE state;
- system prompts;
- provider account/session memory;
- prompt caches;
- model sampling/version;
- executor behaviour;
- dependency/build caches;
- environment variables/network state.

Both A and B therefore require canonical workspace rematerialisation and invariant configuration.

## Catastrophic leakage risks

- future commits/objects reachable from an old checkout;
- remotes, reflogs, tags, packs or Git alternates;
- worktree/source-repository links;
- future commit messages/issues/tests/docs;
- patch/CI artefacts containing the solution;
- hidden verifier or task-generation files visible to the agent.

The future-history gate must fail closed.

## Selection/subject bias

P0's private subject creates:
- author familiarity;
- architecture designed by the same author;
- potentially unusually strong tests/docs;
- historical survivor bias;
- retrospective task-selection bias.

Use a frozen candidate window, inclusion/exclusion rules, task hashes and sampling procedure. P0 is a methodology pilot only.

## Construct validity

- RRI is descriptive, not causal;
- reconstruction-probe scoring may reward verbosity;
- semantic ablation can merely damage the repo;
- visible tests can leak constraints;
- reconstruction-cost classification is manipulable;
- token telemetry omits provider internals.

## External validity

Results may depend on:
- one repository/language/model;
- repository size;
- task locality;
- dependency width;
- documentation/test quality;
- retrieval capability.

Public multi-repository and multi-model replication is required.

## Statistical conclusion validity

Approximately five tasks and one run per condition cannot establish general superiority or non-inferiority.

P0 can validate methodology and reveal obvious failures. Repeated later studies require a declared task population, justified margin, dependence-aware uncertainty, missing-data rules and stopping rules.

## Adverse prior evidence

Handoff Debt shows that repository-only takeover of interrupted tasks can impose substantial rediscovery cost. Post-acceptance RaS must be allowed to show the same problem.
