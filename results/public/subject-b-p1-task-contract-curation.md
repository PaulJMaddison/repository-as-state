# Subject-B P1 SearchForCars task-contract curation

The corrected P1 task-contract curation has completed for the already-established
SearchForCars historical chain.

No P1 experimental task-solving model invocation has occurred.

The curation worker explicitly excluded P0-generated outputs from task-contract
construction and used historical/pre-P0 requirement evidence.

## Historical chain

The established chain remains:

- WP04_PR5
- WP05_PR6
- WP06_PR7

Chain identity remains valid.

## P1 task-contract result

All three corrected task contracts pass the shared fail-closed
`ras.task_contract` evaluator and the independent-engineer fairness review.

| Task | Requirements | Governing behaviours | Eligible | Fairness |
| --- | ---: | ---: | --- | --- |
| WP04_PR5 | 8 | 8 | true | PASS |
| WP05_PR6 | 10 | 10 | true | PASS |
| WP06_PR7 | 12 | 12 | true | PASS |

All governing behaviours are mapped, every derivation class is allowed, exact
copy/string acceptance is justified/removed as required, and contract authority
flows from historical requirement -> task specification -> governing behaviour.

The WP05 contract uses semantic journey/content requirements rather than
arbitrary historical literal strings.

## Frozen private commitments

WP04 task specification SHA256:

`e5edbed6c5fe2c4a0d8d0cd4bf497e4056a7140bd4cf888e93d53d9bee552201`

WP04 task-contract SHA256:

`60bbb850a26f4173dedf591f3acd64aa2da07b47cd8d7777828a743edac2560a`

WP05 task specification SHA256:

`b85af46eaa5e3673703dd139b5e27fd88c087a132f661a6fbdb02fa972f39555`

WP05 task-contract SHA256:

`5027b39a373632c4c4db8b24d8a1472d121ae8f917e47950e64bc68b4debee2f`

WP06 task specification SHA256:

`a32a2e1e244d846aef535a66ef5aaadad997bb72de231647c8e185c0f50133dd`

WP06 task-contract SHA256:

`b2f6dfd4dda8484acd9fd01a96d8f0c6433e9c8d2de4065db61a73d484a56e40`

Whole private curation package SHA256:

`11a883bc0f5346e9dd87ddb9fbc30bb072e5bcf35edb6239e8e0d4c73bc0b041`

## Current gate

The SearchForCars chain is established and the corrected P1 task contracts are
now eligible.

The next step is to implement **private hidden P1 behavioural verifiers** from
these already-frozen contracts, prove PRE FAIL / accepted POST PASS and
behavioural negative controls, then freeze the verifier implementations before
any P1 experimental agent run.

At this point:

- `P1_SEARCHFORCARS_CORPUS_ELIGIBLE=true`
- `P1_EXPERIMENTAL_AGENT_RUNS=0`
- `P1_EXECUTED=false`

Current next step:

`BUILD_AND_FREEZE_PRIVATE_P1_VERIFIERS`
