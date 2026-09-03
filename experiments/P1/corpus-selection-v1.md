# P1 corpus-selection rule v1

Status: **FROZEN BEFORE P1 TASK-CONTRACT CURATION.**

P1 is a methodology-corrected follow-up to Subject-B P0.

To avoid outcome-driven searching after P0, P1 will **not** search for a new
favourable SearchForCars chain.

The only SearchForCars candidates eligible for P1 curation are the same three
historical transitions used by P0:

1. `WP04_PR5`
   - PRE `e7f53f17dd7d46050f7836a92a8918c27b6cd01b`
   - POST `b364a51ace47a8c73dc5e2affcb8fbcd156db1bf`
2. `WP05_PR6`
   - PRE `b364a51ace47a8c73dc5e2affcb8fbcd156db1bf`
   - POST `96aa7162faa48e47104916331a9ffcfd66af7171`
3. `WP06_PR7`
   - PRE `96aa7162faa48e47104916331a9ffcfd66af7171`
   - POST `83b5b3c98213c13e2d81b33ade63891effcf204d`

## Why this is frozen

P0 has already been observed. Searching later SearchForCars history for tasks
that happen to work under the corrected protocol would create an avoidable
post-outcome selection problem.

P1 therefore asks a narrower methodological question:

> Can the original three-transition historical chain be made eligible under the
> corrected runtime and task-contract rules **without using P0 model failures to
> tailor the requirements**?

## Allowed P1 curation inputs

For these three transitions, the privileged curator may use:

- exact historical PRE and accepted POST states;
- historical requirement/task records that existed independently of the P0
  model outputs;
- the original pre-P0 frozen requirement material;
- accepted-boundary evidence;
- original verifier behaviour as a diagnostic source;
- public P1 task-contract rules.

The curator must not use the content of A1/B1/A2/B2/A3/B3 generated patches,
model responses or task-specific failure behaviour to decide what requirements
to add.

## Eligibility rule

Each of the three candidates must independently pass the shared
`ras.task_contract` gate.

If all three pass and preserve the historical chain identity, P1 may proceed to
new task/verifier lock and preregistration.

If any candidate cannot be made eligible from legitimate historical
requirements without implementation-specific or hidden acceptance behaviour:

- reject that candidate for P1;
- do not search replacement SearchForCars commits;
- do not weaken the task contract;
- do not alter P0;
- terminate SearchForCars P1 corpus construction.

The next research step would then be a separately preregistered close
replication subject, with RoomBundle the preferred candidate.

## P1 status

At freeze:

- P1 task-solving model invocations: 0
- P1 executed: false
- P1 task contracts: not yet frozen
- P1 hidden verifier implementations: not yet frozen
