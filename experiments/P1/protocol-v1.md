# P1 protocol v1 — corrected causal-study framework

Status: **FROZEN FRAMEWORK; TASK-SPECIFIC PREREGISTRATION PENDING.**

This protocol is a new experiment version after P0. It does not amend P0.

## 1. Research question

After a validated accepted engineering transition, can a fresh
high-capability reasoner reconstruct sufficient task-relevant state from the
authoritative repository with acceptable correctness and rediscovery cost,
relative to a matched reasoner that retains predecessor reasoning-session
history?

## 2. Conditions

### Condition A — persistent reasoning session

The first selected task starts a new Codex session.

Every later selected task resumes the exact same session identifier.

The repository itself is rematerialised to the exact frozen historical PRE for
each task. Generated experimental code from an earlier task is never carried
into the next task.

### Condition B — fresh reasoning session

Every selected task starts a new independent Codex session.

No predecessor session identifier, conversation or local session database may
be provided.

The same exact frozen historical PRE is rematerialised for the matched task.

## 3. Intended causal difference

The intended treatment variable is predecessor reasoning-session continuity.

The following must be identical or mechanically matched between A and B:

- model identifier/configuration;
- exact task prompt bytes;
- historical PRE commit/tree;
- writable branch state;
- toolchain;
- offline dependencies;
- provider transport;
- agent-tool network denial;
- filesystem isolation;
- timeout;
- attempt/retry policy;
- available public repository tests/tools;
- metrics collection.

## 4. Runtime requirement

P1 must use runtime-v3 or a later explicitly versioned runtime that preserves
all runtime-v3 guarantees.

Required runtime-v3 public/private evidence includes:

- writable exact-PRE `ras-experiment` materialisation;
- no remotes/future/unreachable objects;
- fail-closed future-history leak gate;
- deterministic offline restore/build capability;
- provider transport restricted to the approved destination set;
- provider transport separated from ordinary agent-tool network access;
- negative network controls;
- restart-persistent default-deny network policy;
- successful synthetic repository edit/status probe;
- A/B runtime parity.

## 5. Task eligibility

A candidate task is eligible only if:

1. it is a real historical engineering requirement;
2. it has a credible accepted PRE and accepted POST boundary;
3. its PRE can be materialised leak-free;
4. it is non-trivial but feasible within the frozen task budget;
5. it is locally/deterministically adjudicable;
6. materially equivalent correct implementations can pass;
7. no live external service or secret is required;
8. the governing verifier is implementation-independent;
9. every governing verifier behaviour has exactly one valid task-contract
   mapping;
10. every mapping is either:
    - `EXPLICITLY_REQUIRED_BY_TASK_SPEC`, or
    - `REASONABLY_ENTAILED_BY_TASK_SPEC`;
11. no governing behaviour is
    `NOT_REASONABLY_DERIVABLE_FROM_TASK_SPEC`;
12. no acceptance rule is merely historical-patch identity.

The shared `ras.task_contract` evaluator must return:

`ELIGIBLE_FOR_PREREGISTRATION`

before the task may enter the final P1 corpus.

## 6. Curator contamination rule

P0 experimental outputs and their model-specific implementation mistakes must
not be used to tailor a P1 task specification.

P1 curation may use:

- historical repository state;
- real historical requirements;
- accepted-boundary evidence;
- task-contract requirements;
- verifier behaviour requirements;
- public software-health evidence.

If a historical P0 transition is considered for P1, its task specification
must be reconstructed from historical requirements and the corrected task
contract, not from observing what A1/B1/A2/B2/A3/B3 happened to miss.

This limitation must be disclosed in the paper because the overall coordinator
has knowledge of P0 outcomes.

## 7. Hidden verifier rule

The verifier source stays inaccessible to experimental agents.

The behavioural requirement does not.

Agents receive sufficient neutral task text to derive every behaviour that can
govern pass/fail.

The verifier may test negative/fail-closed behaviour not verbatim in prose only
when that behaviour is reasonably entailed by the stated task contract.

## 8. Prompt freeze

For each selected task:

`A_PROMPT_BYTES == B_PROMPT_BYTES`

Prompt bytes and SHA256 are frozen before the first experimental invocation.

A common repository-authority prefix may be used, but must be byte-identical
across matched conditions.

## 9. Anti-carryover

Experimental output from task i is frozen and archived.

The next task begins from its own exact historical accepted PRE.

Condition A carries only the reasoning session.

Condition B carries neither reasoning session nor generated code.

## 10. Attempts, timeouts and outcome handling

The exact attempt and timeout values must be frozen in the task-specific
preregistration before P1 begins.

No model-quality retry is allowed after inference or model tool activity has
started.

A timeout is an observed task outcome, not a reason to extend the protocol.

## 11. Blindness / adjudication

All experimental model outputs must be frozen before hidden behavioural
verdicts are inspected.

No correctness feedback from an earlier matched task may be provided to a
later experimental run.

## 12. Measurements

Where directly observable:

- behavioural pass/fail;
- wall-clock duration;
- input/output/cached/reasoning tokens;
- model calls;
- tool calls;
- failed tool calls;
- commands;
- files read/modified;
- reconstruction/repository exploration;
- timeouts;
- ordinary restore/build/public-test health.

Unavailable metrics remain `UNAVAILABLE`.

Do not estimate.

## 13. Interpretation

P1 remains a small causal study.

Do not claim formal equivalence or statistical non-inferiority from a small
task chain.

Any positive P1 result requires independent replication before broad
generalisation.

RoomBundle remains the preferred close replication candidate after a valid P1.

## 14. P0 preservation

P0 outputs, verdicts, locks and hashes are immutable.

P1 must receive a new:

- protocol identifier;
- task/corpus lock;
- runtime reference;
- preregistration;
- experiment root;
- experiment lock.

## 15. Current gate

The framework is ready, but task-specific execution is prohibited until:

`P1_CORPUS_AND_TASK_CONTRACTS_FROZEN=true`

and a public-safe P1 preregistration commitment exists.
