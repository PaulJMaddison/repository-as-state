# Experimental method — hostile-audit revision

## Primary P0 causal comparison

**A — Persistent-history control**
- predecessor high-capability reasoning-session history available;
- canonical accepted project state;
- current task.

**B — RaS forced reset**
- no predecessor conversation, summary, resume state or copied reconstruction;
- same canonical accepted project state;
- same current task.

The intended treatment is **predecessor reasoning-session history availability**.

## State that must be matched across A/B

Before every task in both conditions:
- materialise the same accepted repository state into a canonical clean workspace;
- remove untracked files, shell history, IDE state, scratch files and previous tool residue;
- use identical system/developer experiment instructions and task text;
- use the same model build/configuration/sampling;
- use the same tool schema/executor/privileges;
- use the same base image, dependency versions, environment policy and network policy;
- use the same hidden verifier.

Caches must be reset or identically prewarmed under a preregistered policy.

If provider/account/session memory cannot be disabled or audited, the runtime is ineligible for the causal A/B experiment.

## FUTURE_HISTORY_LEAK_GATE

Before model invocation:
- no remotes;
- known future solution SHAs cannot resolve;
- no future refs/tags/reflogs/packed objects;
- no Git alternate object store;
- no source-repository worktree/filesystem link;
- no future patch/CI/generated artefact;
- network cannot retrieve private future source state.

If any check fails:

    RUN INVALID — STOP BEFORE MODEL INVOCATION.

## Task leakage

Audit post-cutoff:
- commit messages;
- issue edits;
- branch names;
- changelogs/TODOs;
- future tests;
- generated docs;
- patch files/task-generation outputs.

Information legitimately present at cutoff remains allowed.

## Hidden verifier

Must be:
- outside the workspace;
- unavailable to the agent;
- behaviour-oriented;
- identical across conditions;
- versioned and hashed before runs;
- capable of accepting equivalent correct solutions.

## Human intervention and reruns

After run start prohibit:
- hints/file pointers;
- copied information;
- prompt changes;
- manual edits;
- cross-condition conclusions;
- selective reruns.

Preregister timeouts, retries and the distinction between AGENT_FAILURE and INFRASTRUCTURE_FAILURE.

## P0 scope

Primary: A/B.

Exploratory: one small preregistered semantic-state ablation C if it does not weaken causal clarity.

Deferred: tiered execution D.

P0 is a methodology pilot/initial case study. Allowed interpretations:
- METHODOLOGY FAILURE;
- EVIDENCE AGAINST RaS;
- MIXED / CONDITIONAL PILOT EVIDENCE;
- SUPPORTIVE PILOT EVIDENCE.

Never PROVEN.

## Corpus-preparation state

The P0 corpus has now been selected privately under the preregistered historical-window and task-selection rules.

The public experiment uses five pseudonymous dependent task units, `P0-T1` through `P0-T5`, with byte-canonical neutral task specifications committed by SHA-256. Exact subject/commit/path/solution information remains behind the private-lock commitment.

Both A and B will use the same generic independent-workspace materialiser and fail-closed future-history gate. The public gate rejects remotes, Git alternates, linked worktrees, unexpected refs, reflog leakage, resolvable forbidden future commits, unreachable extra Git objects, future-state sidecars, symlink escapes, dirty workspaces, and absent network-isolation assertion.

Condition C is not enabled because no clean semantic-only ablation was identified for this pilot. Condition D remains deferred.

The corpus is selected but the experiment is not run-ready until the exact model/runtime, stable system instructions, tools/permissions, resource budget, telemetry, cache/network policy, account-memory controls, and private verifier implementation are frozen.

No P0 result exists.
## Fixed cross-condition state progression

To preserve causal identifiability, P0 does **not** let A and B produce different repository states for the next task. For each task, both conditions receive independently materialised copies of the same frozen historical accepted pre-state. Experimental outputs are adjudicated and recorded, but the next task advances to the next frozen historical accepted boundary.

This preserves byte-identical repository state across A/B. It also creates a declared limitation: Condition A may retain reasoning about a materially equivalent prior implementation that differs from the next frozen historical boundary. Stable runtime instructions must state that the rematerialised repository is authoritative.

