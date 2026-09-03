# P1 SearchForCars chain rule v1

Status: **SEARCHFORCARS HISTORICAL CHAIN ALREADY ESTABLISHED; P1 TASK-CONTRACT REMEDIATION PENDING.**

P1 is a methodology-corrected follow-up to Subject-B P0.

The SearchForCars historical subject and three-transition chain are **not being
re-proven from scratch**. They were already established extensively before P0
under the accepted work-package methodology and Protocol v1.

The fixed P1 chain remains:

1. `WP04_PR5`
   - PRE `e7f53f17dd7d46050f7836a92a8918c27b6cd01b`
   - POST `b364a51ace47a8c73dc5e2affcb8fbcd156db1bf`
2. `WP05_PR6`
   - PRE `b364a51ace47a8c73dc5e2affcb8fbcd156db1bf`
   - POST `96aa7162faa48e47104916331a9ffcfd66af7171`
3. `WP06_PR7`
   - PRE `96aa7162faa48e47104916331a9ffcfd66af7171`
   - POST `83b5b3c98213c13e2d81b33ade63891effcf204d`

Chain identity:

- WP04 POST == WP05 PRE
- WP05 POST == WP06 PRE

## What P1 is correcting

P1 is not asking whether SearchForCars is a valid research subject or whether
these accepted transitions exist.

Those questions were already answered before P0.

P1 is correcting the **experimental task contract** for those same historical
transitions:

- the neutral task specification must expose every behaviour that can govern
  pass/fail;
- the hidden verifier must remain implementation-independent;
- no hidden acceptance requirement may be introduced;
- the corrected runtime must present each exact historical PRE as a normal
  writable leak-free repository.

The P1 task-contract gate is therefore a **fairness/specification gate**, not a
new corpus-feasibility gate.

## Why the same chain remains fixed

P0 has already been observed, so P1 must not search later SearchForCars history
for a more convenient or favourable chain.

The same WP04/WP05/WP06 transitions remain the P1 chain.

This avoids post-outcome task selection while preserving the extensively proven
SearchForCars historical evidence.

## Allowed P1 remediation inputs

The privileged curator may use:

- exact historical PRE and accepted POST states;
- historical requirement/task records that existed independently of P0;
- original pre-P0 frozen requirement material;
- accepted-boundary evidence;
- original verifier behaviour as a diagnostic source;
- public P1 task-contract rules.

The curator must not use P0-generated patches, model responses or
failure-specific reasoning to invent new requirements.

## If a first draft task contract fails

A failed `ras.task_contract` evaluation does **not** mean SearchForCars has
failed as a subject and does **not** automatically terminate P1.

It means the proposed P1 task contract is not yet fair or complete.

The coordinator/curator must:

1. identify the contract defect;
2. correct the neutral task specification or governing behaviour mapping only
   from legitimate pre-existing historical requirements;
3. rerun the fail-closed contract evaluator;
4. preserve the same historical PRE/POST transition.

Do not weaken the requirements merely to obtain a pass.

Do not use P0 model failures as the source of a correction.

Only if a historical transition is shown to be fundamentally impossible to
express as an implementation-independent behavioural task contract from
legitimate historical requirements should the coordinator stop and review the
P1 design.

That is a **methodology-review condition**, not an automatic instruction to
abandon SearchForCars.

RoomBundle remains a planned later replication subject after SearchForCars P1;
it is not the automatic fallback for a first-draft contract failure.

## P1 status

At this clarification:

- SearchForCars subject validity remains established;
- historical chain remains WP04 -> WP05 -> WP06;
- runtime-v3 remediation is green;
- P1 task-contract specifications/verifiers are not yet frozen;
- P1 task-solving model invocations = 0;
- P1 executed = false.
