# Subject B P2 — Item 61 runtime-access falsification v2

## Status

**Item 61 reopened. Item 62 blocked before model execution.**

The first live post-lock Item-62 execution preflight falsified one part of the accepted Item-61 execution-readiness claim: the dedicated restricted identity could authenticate, but Windows denied execution of the frozen Codex executable before any task-model process started.

Worker terminal:

`BLOCKED_PRE_MODEL_RESTRICTED_CODEX_EXECUTABLE_ACCESS_DENIED`

Public repository remained unchanged at:

`69de3dc9577e38058f0b8c084e669e3d15e2e742`

## Observed facts

- restricted credential valid: **true**
- experimental identity: `DESKTOP-BFTREBH\ras-p2-experimental`
- experimental identity Administrator: **false**
- frozen Codex executable launch: **Access denied before model process start**
- scheduled units with genuine model activity: **0/24**
- fresh accepted experimental units: **0**
- hidden verifier runs against fresh candidates: **0**
- correctness adjudications: **0**
- Item 62 executed: **false**
- experimental attempt consumed: **false**

This is therefore a runtime-readiness falsification, not experimental contamination or a candidate/model result.

## Scientific ruling

The previous Item-61 execution lock remains preserved as historical evidence, but its live execution-readiness claim is superseded by this observation.

The authoritative ledger returns to **60/67 complete**:

- Item 61: **ACTIVE — restricted Codex runtime-access repair and fresh execution relock**
- Item 62: **BLOCKED**

The repair must not change the experiment itself. Prompts, model, task selection, PRE states, randomisation, schedule, blind IDs/mapping, timeout, retry discipline and full-block blindness remain frozen.

The repair must make the exact frozen Codex runtime executable by the restricted non-admin identity **without granting that identity access to protected coordinator/private roots**. After live restricted-runtime qualification, a superseding zero-model execution lock must be created and publicly committed before Item 62 may start again.
