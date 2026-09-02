# Experimental method

## Conditions

**A — Persistent monolithic control.** A continuing high-capability session retains history and may reason, edit and test.

**B — RaS forced reset.** The same high-capability model is used, complete repository state is retained, and the reasoning session is destroyed after every bounded task. A fresh session receives only repository state and the next task.

**C — RaS semantic-state ablation.** As B, except pre-registered semantic repository artefacts are removed according to a manifest while source, tests and build rules remain.

**D — RaS tiered execution.** High-capability reasoning is transactional and a separate lower-cost or stateful execution worker performs constrained implementation and verification.

## Forced reset

For each sequential stage:

    A_1 + R_0 + U_1 -> R_1
    destroy A_1
    A_2(fresh) + R_1 + U_2 -> R_2
    destroy A_2

and repeat.

In reset conditions there is no previous conversation, resume facility, external summary, copied hidden memory or manual transfer of state. Only the repository and current task survive.

## Outcomes

Primary and secondary outcomes should include:

- correct task continuation under hidden behavioural verification;
- RRI by depth;
- regression rate;
- reconstruction accuracy;
- input and output tokens where available;
- reconstruction tokens and RTF;
- files read;
- tool and model calls;
- wall-clock time;
- retries and intervention count;
- execution cost proxies.

P0 is a pilot. Confirmatory analyses, exclusion rules and power calculations belong in later preregistrations.
