# Subject B P2 corpus correction v2

Status: **CORRECTION TO v1 — INITIAL P2 TASK FREEZE REMAINS VALID**.

No P2 experimental model run has occurred.

## Correction

`subject-b-p2-corpus-freeze-correction-v1` incorrectly concluded that P2_T03/C08's frozen historical POST should be treated as an invalid accepted boundary because a full `dotnet build SearchForCars.sln` invocation failed.

That conclusion was caused by an over-strict coordinator verifier prompt and is withdrawn.

The established experimental unit is a validated accepted work-package boundary judged by its frozen disclosed behavioural contract. Whole-repository/commit greenness is not itself the acceptance model.

A hidden verifier must evaluate the relevant behaviour through implementation-independent semantic observation. It may use targeted/minimal compilation, reflection, dynamic loading, process/API execution or deterministic adapters/fakes as appropriate. A failure of the entire historical solution to compile in isolation is not, by itself, a reason to invalidate a frozen task identity.

## P2 state

The initial P2 task-selection and curation freezes remain the authoritative current corpus identities:

- design-input manifest: `D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`
- task-selection freeze: `829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`
- curation package: `5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

Programme state:

- item 59: complete
- item 60: active
- P2 experimental runs: 0

## What remains invalid

The earlier fixture-only P2 verifier attempt remains invalid because it derived verdicts from hand-authored semantic-state JSON rather than candidate execution.

The next verifier implementation must exercise actual candidate behaviour through legitimate semantic seams and must not use full-solution build/test success as an extra methodology gate.