# P0 readiness checklist

**Current status: NOT READY TO EXECUTE.**

This checklist is a hard gate, not a planning suggestion. Every mandatory item must be frozen and auditable before P0 begins.

## Corpus

- [ ] Candidate historical window/frame defined.
- [ ] Inclusion criteria frozen.
- [ ] Exclusion criteria frozen.
- [ ] Candidate set frozen before outcomes.
- [ ] Sequential-dependence criterion satisfied and documented.
- [ ] Task hashes frozen.
- [ ] Sampling/randomisation rule and seed frozen where used.
- [ ] Subjective complexity labels frozen before outcomes.
- [ ] Historical survivor bias documented.

## Causal treatment

- [ ] Canonical workspace materialiser implemented.
- [ ] A and B rematerialise identical accepted project state per task.
- [ ] Untracked/shell/IDE/scratch/worktree residue removed.
- [ ] Stable experiment instructions hashed.
- [ ] Current task text identical across A/B.
- [ ] Model/configuration/sampling manifest frozen.
- [ ] Tool schema/executor manifest frozen.
- [ ] Base image/toolchain/dependency manifest frozen.
- [ ] Cache policy frozen.
- [ ] Network policy frozen.
- [ ] Provider account/session memory disabled or auditable.
- [ ] If hidden cross-session memory cannot be controlled, runtime rejected.

## FUTURE_HISTORY_LEAK_GATE

- [ ] No remotes.
- [ ] Known future solution SHAs cannot resolve.
- [ ] No future refs/tags/reflogs.
- [ ] No packed future objects.
- [ ] No Git alternates.
- [ ] No source-repository worktree/filesystem links.
- [ ] No future patch/generated/CI artefacts.
- [ ] Network cannot retrieve private future source.
- [ ] Gate fails closed before model invocation.
- [ ] Gate version/evidence format frozen.

## Task leakage

- [ ] Post-cutoff commit messages audited.
- [ ] Issue edits audited.
- [ ] Branch/tag names audited.
- [ ] Changelog/TODO/comment/generated-doc channels audited.
- [ ] Future tests unavailable.
- [ ] Task-generation files unavailable.
- [ ] Historical solution patches unavailable.

## Hidden verifier

- [ ] Stored outside experimental workspace.
- [ ] Inaccessible to agent.
- [ ] Behaviour-oriented.
- [ ] Same across conditions.
- [ ] Equivalent correct solutions accepted.
- [ ] Historical future patch not used as textual oracle.
- [ ] Verifier version/hash frozen.

## Reconstruction probe

- [ ] Reportable-state schema frozen.
- [ ] No chain-of-thought requested.
- [ ] Objective hidden-ground-truth rubric frozen.
- [ ] Scoring blinding plan defined where feasible.
- [ ] Probe stored outside subject workspace.
- [ ] Probe never supplied to later agents.

## Run control

- [ ] Timeout/stopping rule frozen.
- [ ] Retry rule frozen.
- [ ] Cancellation rule frozen.
- [ ] AGENT_FAILURE defined.
- [ ] INFRASTRUCTURE_FAILURE defined.
- [ ] Rerun rule frozen.
- [ ] Selective reruns prohibited.
- [ ] Human hints/manual edits/prompt changes prohibited.

## Telemetry

- [ ] Total input/output tokens captured where exposed.
- [ ] Reconstruction input classification frozen.
- [ ] File/byte read measurement available.
- [ ] Search/tool/model calls measured.
- [ ] Reconstruction/total elapsed time measured.
- [ ] Retry/escalation measured.
- [ ] Cache counters captured where exposed.
- [ ] Provider-billed usage captured only if exposed.

## Preregistration

- [ ] Allowed P0 interpretation categories frozen.
- [ ] P0 explicitly labelled methodology pilot/initial case study.
- [ ] No inferential non-inferiority claim planned for ~5 tasks.
- [ ] Preregistration committed before any outcome is observed.

If any mandatory treatment/leakage/verifier item is unresolved: **DO NOT RUN P0.**
