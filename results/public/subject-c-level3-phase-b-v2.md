# Subject C Level-3 Phase B v2 — accepted public binding

Status: **coordinator accepted**.

Subject C remains publicly identified only as `PRIVATE_SUBJECT_C`. The private repository identity, historical commit identities, hidden verifier implementation, future schedule, seed and blind mapping are intentionally not disclosed here.

## Accepted design state

- Subject selection changed after Phase A: **false**
- Historical chain changed after Phase A: **false**
- Tasks: **3**
- Planned repetitions per condition: **3**
- Planned total future model runs: **18**
- Planned matched task × repetition units: **9**
- Governing behaviours: **10**

## Historical source-state qualification

The v2 repair rematerialised the selected historical PRE and POST states directly from the frozen chain boundaries rather than reusing the rejected v1 qualification copies.

- historical PRE verifier runs: **3**
- historical POST verifier runs: **3**
- all selected PRE states showed the required new-behaviour absence: **true**
- all selected POST states satisfied the frozen disclosed behaviours: **true**

## Semantic-verifier qualification

The accepted v2 verifier is source/state semantic verification only. Project builds, compilers and public test suites are not correctness signals and were not used for qualification.

- governing behaviours: **10**
- semantic negative controls detected: **10/10**
- materially different alternate-valid behaviour witnesses accepted: **10/10**
- adversarial false-positive controls rejected: **10/10**
- implementation-independence qualification: **pass**
- deterministic verifier output: **pass**
- future-history leak gates: **3/3 pass**

Accepted verifier package SHA-256:

`18aa90e28afbf1f36d2aa909417cb436279ddf20fc8c99e516ae25f42f25c0cd`

Accepted Phase-B package SHA-256:

`ee2c288203cf1e36c368624e9efb18ffe0983d29aa89f698eeddef350081fadf`

## Build / test / compiler policy

For accepted Phase B v2:

- project build runs: **0**
- compiler runs: **0**
- public test runs: **0**
- build success used as correctness: **false**
- build failure used as correctness: **false**
- build/test/compiler results used for verifier qualification: **false**

The earlier Phase-B v1 attempt remains historical falsification evidence. Its verifier was rejected by coordinator review because implementation independence was not sufficiently demonstrated. A separate earlier dependency/tool-availability diagnostic was quarantined and contributed no correctness or methodology evidence.

## Experimental state

No Subject-C task-solving experiment has yet run:

- experimental task-model runs: **0**
- model outputs generated: **0**
- correctness adjudications against model output: **0**
- randomisation schedule created: **false**
- blind mapping created: **false**
- execution lock created: **false**

Phase C may now prepare the final preregistration, randomisation, blindness and execution lock. No empirical Subject-C result exists yet.
