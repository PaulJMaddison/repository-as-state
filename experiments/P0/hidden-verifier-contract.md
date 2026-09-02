# Hidden verifier contract — P0

Status: **BEHAVIOURAL REQUIREMENTS FROZEN; IMPLEMENTATION NOT YET BUILT.**

The hidden verifier is an adjudicator, not an execution assistant.

For every selected P0 task the verifier must:

- live outside the experimental workspace;
- remain inaccessible to Conditions A, B and any exploratory C run;
- be frozen, versioned and cryptographically committed before model execution;
- be identical across matched conditions for the same task;
- test observable behaviour, contract or invariant rather than historical patch identity;
- accept materially equivalent correct implementations;
- run deterministically and locally/offline where practical;
- isolate tenant/context state where relevant;
- cover important negative/fail-closed behaviour;
- enforce a fixed timeout and deterministic environment;
- return only the final adjudication record to the harness.

The experimental agent must not receive hidden verifier source or iterative hidden-failure detail.

Normal repository tests available at the allowed historical state remain available to the agent. Hidden verification is additional independent adjudication.

Task-specific behavioural requirements are held in the private P0 lock payload and are committed publicly only through PRIVATE_P0_LOCK_SHA256.

No hidden verifier source is stored in this public repository.
