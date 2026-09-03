# Subject-B isolated runtime v2 — candidate execution boundary

Status: **pre-experiment runtime design for local validation**.

This document does not execute P0, alter the frozen Subject-B corpus, or
supersede the immutable Protocol v1 lock. It defines the next runtime candidate
after the unrestricted Windows host correctly failed the enforceable-isolation
gate.

## Why v2 is required

Runtime freeze v1 established that the local Codex configuration, model
selection, session semantics, workspace materialisation, leak gate, execution
order, retry policy and metrics collection could be frozen. It also established
three blockers on the unrestricted host:

- filesystem access could not be denied outside the experimental workspace;
- model-provider transport could not be separated from agent-tool network access;
- cross-session/global state could not be made auditable.

P0 must remain stopped until all three are enforced rather than requested by
prompt.

## Candidate architecture

The preferred local candidate is a **dedicated WSL2 execution boundary** with
no Windows-drive automount and no Windows interoperability.

The privileged Windows host remains the curator. The experimental Codex process
runs inside the dedicated Linux boundary as an unprivileged user.

Required controls:

1. `/etc/wsl.conf` disables Windows-drive automount and Windows process
   interoperability.
2. Experimental users have no sudo/root capability and their home directories
   are mode 0700.
3. No curator/private directories are mounted into the execution boundary.
4. Historical PRE workspaces enter the boundary only through a host-controlled
   one-way materialisation step. The live SearchForCars repository is never
   mounted.
5. The execution boundary has default-deny outbound networking.
6. Provider traffic is permitted only through a host/privileged relay whose
   destination allow-list contains only the empirically required Codex provider
   endpoints. GitHub, arbitrary web access, package registries and external APIs
   remain unreachable to agent tools during P0.
7. The experimental user cannot alter the firewall or provider relay policy.
8. MCP/plugin integrations are disabled unless explicitly frozen as part of the
   protocol. The default P0 target is none.
9. Hidden verifiers execute outside the experimental boundary and their output
   is never returned to the continuing A session.

If local validation shows WSL2 cannot enforce these controls on this machine,
this candidate is rejected rather than weakened.

## Session-state separation

Use distinct OS user homes as part of the state boundary:

- `p0a`: Condition A, one Codex session resumed across A1 -> A2 -> A3.
- `p0b1`: fresh B1 session only.
- `p0b2`: fresh B2 session only.
- `p0b3`: fresh B3 session only.
- `p0probe`: disposable non-experimental runtime probes only.

Homes must not be mutually readable.

Condition A keeps only the reasoning/session state in `p0a`. Its generated
workspace is destroyed after each task and replaced with the next frozen
historical PRE.

Condition B never reuses a Codex session or user home.

## Provider-relay validation

The exact provider destination set must be observed and frozen before P0.

A disposable `p0probe` user may make a minimal **non-experimental synthetic
runtime probe** against an empty synthetic repository solely to establish that
Codex provider transport works through the allow-listed relay. It must not
receive any SearchForCars task bytes, historical PRE state, hidden verifier
material or private curation evidence.

Record these probes separately from experimental-agent runs.

## Network negative controls

Before P0, prove from inside the experimental boundary that:

- the required Codex provider transport succeeds;
- direct GitHub access fails;
- direct arbitrary HTTPS access fails;
- DNS/direct egress that bypasses the relay fails;
- the unprivileged experimental user cannot change the network policy.

A prompt saying "do not browse" is not evidence of network isolation.

## Filesystem negative controls

Before P0, prove from the unprivileged experimental identity that:

- only the assigned workspace and its own private home are readable;
- Windows `C:\` is not mounted or reachable;
- curator/private Subject-B evidence is not reachable;
- other condition homes are not readable;
- no historical POST/future workspace is reachable;
- the experimental identity cannot enable automount, interoperability or sudo.

## Cross-session-memory audit

The only permitted persistent session state is the explicit Condition-A Codex
session in `p0a`.

Record and hash the configuration/home surfaces that Codex can use. Disable or
exclude global MCP memory, plugin state and any other external agent memory.
Fresh B users provide an OS-level negative control against accidental reuse of
local Codex session files.

If provider/account memory cannot be disabled or bounded well enough to state
what persists, P0 remains blocked.

## Existing frozen values retained

- model: `gpt-5.6-luna`;
- execution order: `A1,B1,B2,A2,A3,B3`;
- one model-task attempt per condition/task;
- verifier feedback returned to agent: false;
- experimental generated output carried forward: false;
- historical accepted PRE rematerialised per task: true.

## Timeout

Protocol v1 contains no binding task timeout. Runtime v2 must not invent one
silently. A timeout value must be approved and frozen before P0.

A proposed operational ceiling may be validated locally, but
`timeout_policy_frozen` remains false until explicit human approval is
recorded.

## Public readiness gate

The shared implementation in `ras.runtime_readiness` is deliberately
fail-closed. P0 is eligible only when every declared isolation and freeze field
is true and zero experimental agent runs have occurred.

The local privileged worker must provide the evidence. The shared evaluator
does not create or assume OS isolation.

## Valid next outcomes

- `READY_TO_EXECUTE_P0`: every control is mechanically demonstrated and the
  timeout has been approved/frozen.
- `HUMAN_FREEZE_P0_TIMEOUT`: isolation is ready but timeout remains the only
  unresolved binding field.
- `HUMAN_SELECT_ISOLATED_RUNTIME`: WSL2 candidate cannot enforce the required
  boundary.
- `HUMAN_RUNTIME_INTEGRITY_REVIEW`: previously frozen identities do not match.

No P0 model receives SearchForCars task material during runtime-v2 validation.

## Validation-stage interpretation

A read-only inventory of an existing general-purpose WSL distro is not a test of
this candidate architecture. The candidate specifically requires a newly
provisioned dedicated P0 distro with automount/interoperability disabled,
unprivileged condition identities, provider-only egress and mechanically tested
negative controls.

Accordingly, runtime v2 is rejected only after a dedicated candidate has been
provisioned and one or more required controls are shown to be unenforceable.

