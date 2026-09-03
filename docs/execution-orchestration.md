# Execution orchestration for Repository-as-State

## Principle

> **High-capability reasoning should be invoked at decision boundaries, not consumed continuously throughout mechanical execution.**

A frontier reasoner should decide what work needs to happen, interpret ambiguity and diagnose unexpected outcomes. It should not spend expensive reasoning time babysitting a build, verifier, shell process or result file.

The execution layer should be small, deterministic and cheap.

> **Never make the reasoner wait when the orchestrator can watch.**

## Architecture

RaS separates four responsibilities:

1. **Repository** — authoritative durable project state.
2. **Reasoner** — disposable high-capability intelligence.
3. **Orchestrator** — deterministic execution control.
4. **Verifier** — independent acceptance.

The orchestrator owns:

- subprocess launch and termination;
- bounded hard deadlines;
- progress heartbeats;
- stall detection;
- retries where explicitly allowed;
- cancellation;
- completion signalling;
- structured execution evidence.

The reasoner is re-entered only when the deterministic execution layer reaches a genuine decision boundary.

## Fast-verifier rule

A hidden behavioural verifier is an **oracle**, not a full test-suite runner.

Full repository test suites answer:

> Is this historical repository state healthy enough to be an accepted engineering boundary?

Hidden task verifiers answer:

> Does this exact frozen behavioural contract hold?

Those are different jobs.

For private P0 verifiers, prefer direct deterministic scenarios:

- load the relevant assembly/process once;
- instantiate the service under test with deterministic fakes;
- invoke the public behavioural seam;
- assert the frozen invariant directly;
- write structured JSON;
- exit.

Do not use a multi-minute full test host as the implementation of a hidden behavioural verifier unless the frozen requirement genuinely exists only at that boundary.

## Execution budgets

These are engineering targets, not empirical claims:

- individual local behavioural check: normally seconds;
- complete small hidden verifier: preferably tens of seconds;
- a deterministic local verifier taking several minutes should be treated as a harness-performance defect until justified;
- every invocation must have a hard deadline;
- a lack of useful progress should cause the orchestrator to inspect/terminate/recover rather than passively wait.

## Runtime support

`ras.execution.run_supervised` provides a public-safe generic controller with:

- stdout/stderr heartbeat tracking;
- stall timeout;
- hard timeout;
- bounded terminate/kill escalation;
- optional explicit completion-file signalling;
- structured process outcome.

The completion-file path is intentionally generic. A private verifier can atomically write its result and then create a completion marker. The supervisor can then stop waiting even if a child/test-host process leaves an irrelevant tail running.

Requirement-specific verifier code and hidden behavioural requirements remain private and must not be committed to this public repository.

## Scientific boundary

This orchestration design is engineering infrastructure. It must not be reported as empirical evidence that RaS works.

Its purpose is to make the eventual experiment faster, more reproducible and less dependent on expensive high-capability reasoning during mechanical execution.
