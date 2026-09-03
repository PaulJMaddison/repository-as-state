# Subject-B P1 private verifier qualification — implementation defect found

The first private P1 verifier qualification pass has completed enough work to
establish the following:

- P1 curation integrity remains valid;
- all three historical controls still discriminate correctly:
  - WP04 PRE FAIL / POST PASS
  - WP05 PRE FAIL / POST PASS
  - WP06 PRE FAIL / POST PASS
- all three candidate verifiers are deterministic across three repeated PRE/POST
  runs;
- private P1 curation and verifier trees have been hardened so experimental
  condition users cannot read them;
- no P1 experimental task-solving model has run.

However, the candidate verifiers are **not yet qualified**.

The worker correctly refused to freeze them because:

1. no per-behaviour negative-control fixtures exist yet;
2. implementation-independence is only partial;
3. the current verifier implementations still select exact historical
   test-method names / implementation-specific literals;
4. private oracle self-tests are not yet complete.

Current representative verifier durations are approximately 13.7–14.5 seconds,
which is within the current engineering target and not the blocking issue.

This is a private verifier implementation defect, not a contradiction in the
frozen P1 task contracts.

Current state:

- `P1_PRIVATE_VERIFIERS_READY=false`
- `P1_EXPERIMENTAL_AGENT_RUNS=0`
- `P1_EXECUTED=false`
- `NEXT_STEP=FIX_PRIVATE_P1_VERIFIER_IMPLEMENTATION`

No P1 verifier hashes/package hash have been frozen.
