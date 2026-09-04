# Subject-B P2 preregistration binding v1

Status: **public preregistration commitment corrected and republished; item 61 is not yet complete.**

This record commits the corrected Subject-B P2 experiment before any P2 task-solving model activity.

## Frozen experiment

- 4 historical tasks: `P2V2_T01`–`P2V2_T04`
- 13 disclosed governing behaviours
- 3 repetitions
- 2 conditions
- 24 total experimental runs
- 12 matched task×repetition units
- Condition A: three mutually independent persistent-session chains, each in chronological task order `T01 → T02 → T03 → T04`
- Condition B: twelve fresh mutually independent sessions
- fresh exact PRE state for every experimental unit
- generated implementation never carries between runs or tasks
- full-block blindness: all 24 outputs must be frozen before hidden correctness adjudication

## Model and runtime commitment

- exact model target: `gpt-5.6-luna`
- Codex CLI: `0.153.0-alpha.5`
- execution-relevant effective Codex configuration SHA-256: `8249A208C5DED9B173BBC6B22B8EA6E1A11AB8E29BFF4B7B006A396BF8FA0093`
- Phase-A runtime-manifest SHA-256: `4FC602F42CA6974BFF0AC13AA4D06FF8FA0831790398F05D55EEFBCB66239674`
- run timeout: 1800 seconds

The effective configuration identity above is the canonical execution-relevant configuration frozen inside `P2V2-RUNTIME-MANIFEST-v1.json`; it is deliberately distinguished from the raw `config.toml` file hash.

Phase A established exact-model availability using local runtime/provider metadata without generating a model completion.

## Public commitments to private frozen state

- prompt manifest: `36EE1B1FC458D37821F1805B6E0FEC9AAC12C0BB4A0E1754CFDA22E11E7A2879`
- randomisation manifest: `CEC19FC3891F516F5AB57C47DC28BC427BB8B366A5D80C2FC7B359C975FA1428`
- experimental-unit manifest: `FD47BCF1A81066CF3DD80C240B5C5A1B62D177A1A831B66848FC86D068CE9681`
- blind-ID mapping: `A100F2AA35CBFDB59CC6D5FBD6AB0B7CDFFF83577AB81952F25812DAEA8F09FE`
- PRE-workspace manifest: `C059081C3228C72644E546A14833F339CF9E9211C12037C0196D8C819CF670E3`
- execution-command templates: `38435B615C38264DF1E888159FB7F830CEE0B0956CD5125DA469AC6DB1B9B8F4`
- pre-model readiness audit: `DF99C3B064C7FD3D6E857BA1C15F92A959BAAA23A886819EB3B239B70E24259B`
- preregistration manifest: `221E19675EFAFB37E96FA4950D178BE729C27D16D3B4C955D4DBCBABA2DFCF48`
- preregistration package: `86EAF3411A89D45F3563D7CD64411C0F9927FC5CE5815DB4ECFBA7B0C6DC5F59`

The randomisation seed, private execution order, blind-to-condition mapping and hidden-verifier implementation remain sealed. This public record binds their frozen private manifests without revealing them before adjudication.

## Correction history

The original Phase-A publication commit was:

`7ebb0705d78a52b4144107a323ea240fe31567e6`

with JSON blob:

`8b7355db2db8f519f2cd4096b1801ee14e325f74`.

A Phase-B integrity check proved that the original public `codex_config_sha256` field incorrectly contained:

`4FC602F42CA6974BFF0AC13AA4D06FF8FA0831790398F05D55EEFBCB66239674`

which is the SHA-256 of `P2V2-RUNTIME-MANIFEST-v1.json`, not the effective Codex configuration identity embedded in that manifest.

The correct frozen execution-relevant effective configuration identity is:

`8249A208C5DED9B173BBC6B22B8EA6E1A11AB8E29BFF4B7B006A396BF8FA0093`.

For audit completeness, Phase B also observed the then-current raw `C:\Users\pm\.codex\config.toml` file hash as:

`B321C224F46DCE5C01F500AD813D626D34513738F446644450D0A4D1DF16DF1E`.

No substantive experimental choice changed during this correction. The private Phase-A preregistration manifest/package, prompts, randomisation, schedule, blind mapping, model and timeout remain unchanged. P2 experimental runs remained zero.

## Frozen execution discipline

- repetitions are independent replications, not retries
- no best-of-N selection
- no model-quality retry
- no human rescue
- no mid-run prompt injection
- no verifier feedback during execution
- resource telemetry remains separate from correctness
- no partial hidden adjudication before all 24 output freezes exist
- hidden verifier remains private and inaccessible to the experimental agent

## Zero-model gate at correction publication

- P2 experimental agent runs: **0**
- P2 task-solving model invoked: **false**
- model completions generated: **0**
- P2 executed: **false**
- hidden verifier experimental adjudications: **0**

The next step is item-61 Phase B: validate this corrected public binding against the unchanged private Phase-A package and create the final zero-model execution lock. Only after coordinator acceptance of that lock may item 62 begin.
