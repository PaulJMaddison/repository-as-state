# Subject-B P1 private verifier qualification — partial

The corrected P1 task-contract package remains valid and immutable.

A continuation worker recovered the interrupted private verifier work and re-qualified the historical controls:

- WP04 PRE FAIL / POST PASS
- WP05 PRE FAIL / POST PASS
- WP06 PRE FAIL / POST PASS

All 18 required three-run PRE/POST determinism invocations completed and the behavioural verdicts were stable for all three task verifiers.

The private-access-control audit found inherited access on the P1 curation/verifier trees. The private worker corrected only those private ACLs; the trees are now restricted to owner/system/administrators and the hidden-verifier material is not readable by the experimental identities.

The verifier package is **not ready to freeze yet**. The remaining defects are methodological/verifier-implementation issues rather than SearchForCars corpus failures:

- no per-behaviour negative-control fixtures have yet been created;
- implementation-independence evidence is only partial;
- candidate verifier implementations still rely on exact public test-method names, which are implementation-specific literals rather than direct semantic behavioural observations;
- private oracle self-tests have not yet been completed;
- therefore no final verifier/package SHA has been frozen.

Current measured verifier durations were approximately 13.7–14.5 seconds and are within the current engineering target.

Current state:

- `P1_CURATION_INTEGRITY_VALID=true`
- `P1_PRIVATE_VERIFIERS_READY=false`
- `P1_EXPERIMENTAL_AGENT_RUNS=0`
- `P1_EXECUTED=false`

This does not change the established SearchForCars chain or the frozen P1 task contracts. The next step is to replace implementation-specific test-name selection with direct semantic/public-seam verification, add complete per-behaviour negative controls and oracle self-tests, demonstrate implementation independence, and only then freeze the private P1 verifier package.

Current next step:

`REMEDIATE_PRIVATE_P1_VERIFIER_IMPLEMENTATION`
