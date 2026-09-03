# Subject-B P0 preregistration erratum 001

A pre-experiment integrity gate detected a malformed published SHA-256
commitment for the WP04_PR5 neutral task specification.

The originally published value in
`results/public/subject-b-p0-preregistration-v1.json` is 63 hexadecimal
characters and therefore cannot be a SHA-256 digest:

`1f5ed2d31a0609e3aff2b3fb82868ac4c368825366f70537267f25df5b85180`

The actual frozen task-specification file hashes to the following 64-character
SHA-256 value:

`1f5ed2d31a0609e3aff2b3fb82868ac4c368825366f70537267f25df5b85180a`

This erratum is recorded **before any experimental model invocation**. At
discovery, `EXPERIMENTAL_AGENT_RUNS=0` and `P0_EXECUTED=false`.

This is a clerical commitment correction only. It does not change task bytes,
the historical PRE/POST states, the hidden requirements, the frozen verifier,
Protocol v1, the causal design, the model/runtime, execution order, timeout, or
any acceptance criterion.

The original preregistration artefact is preserved unchanged for auditability.
Before P0 execution resumes, the private immutable lock must be inspected to
determine whether its embedded WP04 task-spec commitment contains the correct
64-character value. If it does, no private lock mutation is permitted or
required. If it does not, a versioned non-destructive private erratum must be
created and frozen before the first model invocation.

Current next step:

`VERIFY_PRIVATE_LOCK_WP04_HASH_AND_FREEZE_ERRATUM_IF_REQUIRED`.
