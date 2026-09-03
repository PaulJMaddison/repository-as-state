# Subject-B P0 final runtime lock

The final private runtime lock has been created after successful authenticated
runtime validation.

Frozen execution controls:

- model: `gpt-5.6-luna`;
- execution order: `A1,B1,B2,A2,A3,B3`;
- one model-task attempt per condition/task;
- hard wall-clock timeout: 3600 seconds;
- Condition A: create a new session at A1, then resume that exact session for
  A2 and A3;
- Condition B: B1, B2 and B3 each start a fresh independent session;
- condition users: `p0a`, `p0b1`, `p0b2`, `p0b3`;
- authentication state is independent per isolated Linux user;
- provider destination set remains `chatgpt.com:443`;
- filesystem isolation, network isolation and cross-session-memory controls are
  ready;
- metrics collection is frozen.

Final private runtime lock SHA256:

`32a5f8912bd5750872b4f5e6e75370810adc3f3129906f4ccf0f35b8d49de302`.

The shared fail-closed readiness evaluator returned ready with no failures.
No Subject-B experimental agent run had occurred at the point the lock was
created.

Current next step:

`EXECUTE_SUBJECT_B_P0`.
