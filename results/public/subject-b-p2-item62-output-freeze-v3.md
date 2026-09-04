# Subject B P2 Item 62 — accepted output freeze v3

Item 62 completed the fresh locked 24-run same-repository P2 execution and is accepted for blind adjudication.

## Execution integrity

- Scheduled units: **24**
- Final frozen unit records: **24**
- Workspace gates passed: **24/24**
- Schedule order changed: **false**
- Unscheduled executions: **0**
- Model-active units: **24**
- Exact model: `gpt-5.6-luna`
- Exact CLI: `codex-cli 0.153.0-alpha.5`
- Model substitutions: **0**

## Session integrity

Condition A used exactly three independent persistent-session chains. T01 created one new session per repetition and the remaining tasks resumed only that repetition's session:

- A chains: **3**
- A new T01 sessions: **3**
- expected resumes: **9**
- successful resumes: **9**
- cross-repetition session reuse: **0**

Condition B remained fully fresh:

- fresh B sessions: **12**
- B resumes: **0**

Generated code did not carry between task workspaces.

## Retry and blindness integrity

- pre-model infrastructure retries: **3**
- post-model quality retries: **0**
- best-of-N: **false**
- human rescue: **false**
- repetitions treated as retries: **false**
- full-block blindness: **true**
- hidden verifier runs during Item 62: **0**
- correctness adjudications during Item 62: **0**
- condition mapping remained sealed: **true**

The earlier runtime/UAC issue was handled under the frozen recovery rule: already model-active units were preserved and were not repeated; only pre-model failures were retried.

## Frozen evidence identities

- Item-62 execution manifest: `334EFF9B6F85AE92766DEC6EF3AEF562F62E97C2DCC8E09C80E6BE5743F1FDBC`
- Item-62 output-freeze manifest: `2A27C6110E99D712D99D1680B58F568512301B866A78E802C5D79D933414BC4E`
- Item-62 execution package: `31898756356B676CB76F7D67596DE206B902659B5E8D58E5A4620250F55607C1`

All SHA-256 values are 64 characters, repeated hashes match and internal package bindings validate.

## Sealed material

This public record does **not** expose the randomisation seed, private schedule, blind-to-condition mapping, hidden verifier, credentials or correctness results.

Item 62 is complete. Item 63 may now perform blind adjudication and scientific interpretation.
