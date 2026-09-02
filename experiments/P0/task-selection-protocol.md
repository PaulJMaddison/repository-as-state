# P0 task-selection protocol

Status: **CORPUS SELECTED — MODEL/RUNTIME FREEZE PENDING**

This document records the task-selection rule that was fixed before individual historical transitions were evaluated for P0.

## Candidate-window rule

Use one **bounded contiguous local engineering programme**, selected before inspecting individual task solutions. The programme must be internally coherent, local/deterministic in character, and must exclude cloud/model-dependent proof work by the window rule rather than by observed experimental outcome.

Publicly, the private subject is identified only as `PRIVATE_SUBJECT_A`. Exact dates, repository identifiers, commits, paths, solution transitions, and task text are held only in the private P0 lock payload.

The selected window contains:

- candidate transitions considered: **38**;
- transitions grouped into selected task units: **17**;
- transitions excluded after the five qualifying pilot units were reached: **21**;
- selected task units: **5**.

Selection-rule commitment:

`c5d2c4d4346152b58ae85513997a404eea08896e6a1af02ce33ab8f9315b49be`

## Selection algorithm

1. Freeze the bounded contiguous programme before task inspection.
2. Enumerate every transition oldest-to-newest.
3. Apply the inclusion/exclusion rules below.
4. Group adjacent transitions into the smallest coherent historical requirement that reaches a credible accepted boundary.
5. Select the first five qualifying sequential task units under the P0 pilot budget.
6. Exclude later transitions solely because the pilot budget has been reached; do not substitute later tasks because they appear easier or more favourable to RaS.
7. Preserve every private candidate decision and reason inside the private lock payload.

## Inclusion criteria

A task must satisfy all applicable criteria:

1. real historical engineering requirement;
2. observable behaviour, contract, architecture, or important invariant changes;
3. non-trivial engineering work;
4. neutral specification possible without historical implementation disclosure;
5. credible pre-task repository state;
6. credible accepted post-task boundary;
7. behaviourally adjudicable without patch identity;
8. deterministic/local verification possible;
9. no paid cloud requirement;
10. no unavailable secret or private external service;
11. no dependence on live-model nondeterminism;
12. not primarily formatting/generated/mechanical churn;
13. focused enough that unrelated changes do not dominate;
14. plausible within a future P0 per-task budget;
15. later selected tasks can naturally depend on accumulated accepted state;
16. requirement wording does not disclose the solution;
17. no required information exists only in an unavailable private human conversation;
18. materially equivalent correct implementations can pass the eventual hidden verifier.

## Exclusion criteria

Exclude:

- cloud-only proof work;
- credential-dependent work;
- external-service incidents;
- pure documentation edits;
- trivial typo/formatting changes;
- mass dependency bumps;
- generated artefact updates;
- tasks without deterministic behavioural adjudication;
- transitions dominated by unrelated changes;
- tasks whose pre-state discloses the future solution;
- tasks where future-history isolation cannot be made fail-closed;
- tasks without a credible accepted boundary;
- time/network-dependent tasks;
- tasks that cannot run locally/deterministically;
- tasks requiring subjective human pass/fail judgement;
- transitions after the first five qualifying clusters under the preregistered P0 pilot budget.

## Sequentiality rule

Five unrelated bugs are not sufficient. A later selected task must naturally depend on earlier accepted programme state through code, interface, test, schema, architecture, governance, or state-transition contracts.

The selected public dependency shape is:

`P0-T1 -> P0-T2 -> P0-T3/P0-T4 -> P0-T5`

The graph is connected. T5 depends on accumulated accepted state from both the identity/lifecycle and governed-state branches.

## Patch independence

Historical solutions are curator ground truth only. Experimental success is never defined by textual similarity to a historical patch.
