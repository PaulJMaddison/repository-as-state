# Subject C Level-3 — 65G runtime-path diagnosis v1

Status: **COORDINATOR-ACCEPTED PRE-MODEL METHODOLOGY DIAGNOSIS**

This is not a Subject-C correctness result and does not contain experimental model output.

## Classification

`STANDALONE_CODEX_SANDBOX_WRAPPER_NOT_EQUIVALENT_TO_ACCEPTED_P2_EXECUTION_RUNTIME`

The fresh 65G state remains pre-model and uncontaminated: 18 fresh scheduled units, 18 fresh blind IDs and 18 fresh PRE workspaces were prepared; no fresh execution lock was created; no Subject-C task model or model completion ran; no project build/compiler/test/lint or correctness adjudication occurred; the failed first block was not resumed and no consumed unit was rerun.

The zero-model readiness investigation established that the standalone `codex sandbox` wrapper is not the execution path used by the accepted Subject-B P2 run. A workspace-only managed permission profile is accepted syntactically by the standalone Windows wrapper but requires the elevated Windows sandbox backend. Elevation is outside the accepted experimental boundary and is not permitted.

Accepted P2 instead used normal `codex exec` under the restricted non-admin identity with `[windows] sandbox = "unelevated"`. Therefore failure of the standalone debug/wrapper path cannot be converted into a Subject-C task failure or correctness outcome.

## Methodology repair before lock

The previous requirement that the standalone `codex sandbox` wrapper itself perform the exact-runtime zero-model read/write gate is retired because that wrapper is not equivalent to the accepted execution runtime.

Before any fresh Subject-C execution lock may be accepted, 65G must instead pass a decomposed pre-model readiness proof:

1. bind the fresh Subject-C launcher/runtime/configuration to the accepted successful P2 non-elevated `codex exec` path;
2. prove zero-model read/create/modify/delete access to representative fresh Subject-C workspaces under the same restricted identity;
3. independently prove protected/private roots remain denied under that identity through the filesystem security boundary;
4. prove the fresh schedule, blind mapping, PRE source bytes and execution state remain unchanged and uncontaminated.

No Subject-C task-solving model may run to perform this readiness proof. 65H remains prohibited until the replacement gate passes and a fresh execution lock is accepted.

## Scientific consequence

This diagnosis does not require regeneration of the fresh 65G state if its integrity can be revalidated. It produces no correctness result, no blind adjudication and no A/B comparison.
