# Repository-as-State — CURRENT

Updated: 2026-09-06 00:10 Europe/London

## Programme status

- Authoritative progress ledger: **64/67 complete**.
- Items **1–64 are COMPLETE**.
- **Item 65 is ACTIVE.**
- Items 66–67 remain pending.
- P0 rerun: **FALSE**.
- P1 rerun: **FALSE**.
- P2 task rerun: **FALSE**.

Current Item-65 substage: **65F — zero-model Subject-C workspace-access/materialisation root-cause qualification**.

## Core framing

- Persist authoritative state; reconstruct computation.
- Do not allow ephemeral state to become authoritative state.
- Unit of progress = validated repository state, not accumulated agent conversation.
- Repository-as-State != repository-as-prompt.
- The hypothesis is not that conversation has no effect. The question is whether persistent conversation state is necessary for behavioural software correctness when sufficient authoritative state can be reconstructed externally.
- Do not claim equivalence or non-inferiority unless explicitly designed for it.

## Historical experimental state

### P0

Executed exactly once and classified:

`MIXED_METHODOLOGY_AND_MODEL_FAILURE`

- causal A/B correctness claims: **REJECTED**
- rerun: **PROHIBITED**
- retained as methodology/falsification evidence

### P1

Accepted Subject-B P1 result:

- Condition A persistent: **18/30 behaviours**
- Condition B fresh: **18/30 behaviours**
- matched agreements: **30**
- disagreements: **0**

Safe wording: no behavioural correctness difference was observed between persistent-session and fresh-session conditions in these three matched tasks.

### P2

Accepted Subject-B P2 result:

- Condition A satisfied: **0/39 behaviours**
- Condition B satisfied: **0/39 behaviours**
- matched agreements: **39**
- disagreements: **0**
- overall candidate passes: **0/12 per condition**

This is a floor-effect result. It does not positively demonstrate successful behavioural preservation, equivalence or repository-state sufficiency. P1 and P2 are not pooled.

## Critical build/test rule

Semantic correctness is **not** determined by project build/compiler/public test execution.

For Subject C, unless a different methodology is preregistered before experimentation:

- project build for correctness: **PROHIBITED**
- project compiler/typechecker for correctness: **PROHIBITED**
- project/public tests for correctness: **PROHIBITED**
- lint for correctness: **PROHIBITED**

Correctness is determined by the accepted implementation-independent source/state semantic verifier.

## Item 65 — Subject C / Level-3 replication

### Accepted 65A — selection/design

Subject C was independently selected under a frozen anti-cherry-picking protocol.

Accepted Phase-A package:

`6b54c793b07c706362f82efa7a64dd59276b059dd12aa583b43e99f78aa26373`

Design:

- tasks: **3** (`SC_T01`, `SC_T02`, `SC_T03`)
- repetitions per condition: **3**
- conditions: **2**
- planned runs: **18**
- matched task × repetition units: **9**
- governing behaviours: **10**
- Condition A: three persistent-session chains `T01 -> T02 -> T03`, with fresh PRE source state per task and reasoning/session continuity only
- Condition B: nine fresh independent sessions
- generated-code carry between tasks: **FALSE**

### Accepted 65B — task contracts and semantic verifier

Phase-B v1 is rejected methodology history because its verifier was too coupled to historical implementation shape and the original phase also contained quarantined tooling/build ambiguity.

Accepted Phase-B v2 package:

`ee2c288203cf1e36c368624e9efb18ffe0983d29aa89f698eeddef350081fadf`

Accepted semantic-verifier v2 package:

`18aa90e28afbf1f36d2aa909417cb436279ddf20fc8c99e516ae25f42f25c0cd`

Accepted verifier qualification:

- governing behaviours: **10**
- historical PRE expected failures: **PASS**
- historical POST expected passes: **PASS**
- negative controls: **10/10 detected**
- alternate-valid witnesses: **10/10 accepted**
- false-positive controls: **10/10 rejected**
- exact historical private helper/substring requirements: **0**
- implementation-independence: **PASS**
- project build/test/compiler used for qualification: **FALSE**

### Accepted 65C — preregistration/execution lock

Execution-lock package:

`9538cc1b9af91b732127d08085a7f2211f37f15fd5bd091d8b03a2493f770afe`

Frozen execution source HEAD:

`84e68b18c8c58d5576d6f726a51524d3e676758f`

Runtime binding:

- model: `gpt-5.6-luna`
- CLI: `codex-cli 0.153.0-alpha.5`
- restricted identity: `DESKTOP-BFTREBH\ras-p2-experimental`
- administrator: **FALSE**
- elevated: **FALSE**
- 18 blind IDs/workspaces/scheduled units frozen
- output freeze required before correctness adjudication

### Accepted 65D/65E — first execution blocked and evidence frozen

The first locked Subject-C execution block is permanently closed and **cannot produce a correctness result**.

Sequence:

1. Slot 1 became model-active and was consumed by `401_UNAUTHORIZED_MISSING_AUTHENTICATION` before a completion.
2. Authentication under the restricted account was repaired successfully using normal ChatGPT login.
3. Slot 2 became model-active but source-state access failed with `EXPERIMENTAL_WORKSPACE_ACCESS_DENIED`; source state remained unchanged.
4. Coordinator authorised one zero-model compatibility repair using the previously successful runtime mode `sandbox = "unelevated"`, because Phase C had not frozen a contradictory sandbox setting.
5. Isolation/private-root denial remained intact.
6. Slot 3 became model-active but source reads still failed with `EXPERIMENTAL_WORKSPACE_ACCESS_DENIED`.
7. Slots 1–3 were never rerun.
8. Slots 4–18 were never started.

Accepted classification:

`EXECUTION_ENVIRONMENT_BLOCKED_AFTER_MODEL_ACTIVITY`

Accepted blocker package:

`a5d534f4599454c5504ea7b8d20d7dc7982bc5b25e5e8d2f441a613eae9cae0c`

Public evidence:

- `results/public/subject-c-level3-execution-blocker-v1.json`
- `results/public/subject-c-level3-execution-blocker-v1.md`

Accepted blocker facts:

- preregistered units: **18**
- consumed units: **3**
- not started: **15**
- authentication repair succeeded: **TRUE**
- `unelevated` repair applied: **TRUE**
- `unelevated` repair resolved workspace access: **FALSE**
- project builds: **0**
- compiler/typechecker runs: **0**
- project/public tests: **0**
- lint: **0**
- hidden verifier runs against model output: **0**
- correctness adjudications: **0**
- correctness inspected: **FALSE**
- Subject-C correctness result available: **FALSE**
- blind adjudication allowed on failed block: **FALSE**
- A/B comparison allowed on failed block: **FALSE**

Do not resume or repair this failed execution block into a result.

## ACTIVE NOW — 65F workspace-access/materialisation qualification

The next scientific task is zero-model diagnosis and qualification of the future Subject-C workspace materialisation/ACL path.

Current working hypothesis from the blocked evidence: the failure is likely in workspace ACL/materialisation rather than the model or semantic verifier. Directory metadata can be enumerated while actual source-file reads remain denied even after `unelevated` sandbox configuration.

Required 65F work:

- compare failed Subject-C workspace parent/file ACLs with the accepted successful Subject-B P2 execution path;
- identify whether the cause is copied ACLs, inheritance, owner, deny ACEs, missing sandbox principal/group access, integrity level, or another filesystem/security property;
- reproduce the problem only in a disposable fixture root;
- define the minimum future materialisation repair;
- prove restricted read/create/modify/delete access on a disposable source-like tree;
- preserve non-admin/non-elevated execution and all protected private-root denials;
- invoke **no task-solving model**;
- run **no project build/compiler/tests/lint**;
- do not modify the failed execution workspaces.

Only if 65F passes may the programme create a **new** Subject-C execution preregistration/lock. The old block remains historical falsification evidence.

## Remaining Item-65 path

- **65F ACTIVE:** zero-model workspace access/root-cause qualification
- **65G PENDING:** fresh Subject-C preregistration, schedule, blind mapping, workspaces and execution lock
- **65H PENDING:** fresh execution and complete output freeze
- **65I PENDING:** blind semantic adjudication and bounded interpretation
- **65J PENDING:** Level-3 publication/claim alignment

Item 65 becomes complete only after the valid Level-3 replication has been executed, adjudicated and published/claim-aligned.

## Programme after Item 65

- Item 66: final hostile review, statistical/claims/limitations and reproducibility audit
- Item 67: final paper + reproducibility package + submission-ready release

## Separate follow-up

`aidocs/repository-as-state/FOLLOWUP-CHATGPT-DIRECT-TO-REPO.md`

After the current experiment/tooling blocker work, fix and verify ChatGPT direct-to-repo end-to-end. This is separate from the experiment and must not be mixed into Subject-C evidence.
