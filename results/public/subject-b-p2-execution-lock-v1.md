# Subject-B P2 execution lock v1

Status: **item 61 complete; item 62 active.**

The final zero-model execution lock has been created downstream of the corrected public preregistration commitment and before any P2 task-solving model activity.

## Frozen experiment

- 4 historical tasks
- 13 disclosed governing behaviours
- 3 repetitions
- 2 conditions
- 24 total experimental runs
- 12 matched task×repetition units
- full-block blindness: all 24 candidate outputs must be frozen before hidden correctness adjudication

## Runtime

- exact model target: `gpt-5.6-luna`
- Codex CLI: `0.153.0-alpha.5`
- execution-relevant effective Codex configuration identity: `8249A208C5DED9B173BBC6B22B8EA6E1A11AB8E29BFF4B7B006A396BF8FA0093`
- runtime-manifest SHA-256: `4FC602F42CA6974BFF0AC13AA4D06FF8FA0831790398F05D55EEFBCB66239674`
- timeout: 1800 seconds

The corrected public preregistration commitment is bound at commit `a3da5fb11df577034ef364c4790deb170ef37f77`, with corrected JSON blob `e4f8419238c336833ee5aec306f0734406091ada`.

## Final pre-execution integrity

- Phase-A private preregistration package unchanged
- canonical prompts unchanged
- randomisation not regenerated
- schedule unchanged
- blind mapping unchanged and sealed
- 24/24 PRE workspaces present, clean and future-history safe
- 24/24 PRE workspaces contain neither hidden verifier material nor sealed mapping material
- persistent-session resume mechanism remains available
- fresh workspace on exact-session resume remains supported
- hidden verifier remains private and inaccessible to the experimental agent
- no pre-existing P2 experimental outputs, correctness results or task sessions

## Frozen execution discipline

- repetitions are independent replications, not retries
- no best-of-N selection
- no model-quality retry
- no human rescue
- no mid-run prompt injection
- no verifier feedback during execution
- no partial hidden adjudication

## Execution-lock identities

- public-binding audit: `D02218A1206BF2C7B2CC4730523D48E99EF02E949C608FB9CCA160DD8D747E41`
- Phase-A integrity audit: `816388AC58FE331CC3924F4DE21F051410B22419A6B514FB04DD4658A78284FC`
- final zero-model gate: `8344F950C7AF7820C088C2761194FDAA6F0F4780D9590F397B5B644E3063DFF3`
- execution-lock manifest: `3E3760D3B57C2BBA4D62B45B154C84633A44DB13025E618E66CE061C92924E9E`
- execution-lock freeze: `9FC8D4B6011BF5A7CDD5C956C0E08D105890AD345577A0A06488A1AA1F424890`
- execution-lock package: `CD8E28A9CAECEFF95B666FD19BD7CB64D19D71F93401CCEBA1C5DC60520AA3C6`

All execution-lock SHA-256 values are 64 hexadecimal characters, repeat-hash checks match, and the package's internal bindings validate.

## Final zero-model gate

At execution-lock freeze:

- model completions generated: **0**
- P2 experimental agent runs: **0**
- P2 task-solving model invoked: **false**
- P2 executed: **false**
- hidden-verifier experimental adjudications: **0**
- pre-existing P2 experimental outputs: **0**
- pre-existing P2 correctness results: **0**

The private schedule, randomisation seed, blind-to-condition mapping and hidden-verifier implementation remain sealed. No correctness information is published here.

The next programme gate is **item 62: controlled execution of the frozen 24-run P2 replication**.
