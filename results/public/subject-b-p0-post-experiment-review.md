# Subject-B P0 post-experiment coordinator review

The locked Subject-B P0 result remains immutable. This review does not rerun,
replace, or reinterpret any of the six experimental outputs.

## What the forensic analysis established

The original Protocol-v1 verifiers still discriminate their historical
boundaries correctly:

- WP04 historical PRE FAIL / POST PASS;
- WP05 historical PRE FAIL / POST PASS;
- WP06 historical PRE FAIL / POST PASS.

The all-fail experimental result therefore cannot be dismissed as a broken
verifier harness.

However, the P0 correctness comparison is not causally interpretable:

- WP05's governing verifier includes exact copy/content markers that the neutral
  task specification did not expose;
- WP04 and WP06 were assessed as only partially specified relative to the
  governing verifier behaviour;
- fresh-condition B1 and B2 were stopped by repository-safety behaviour before
  implementation in a detached-HEAD workspace;
- several other runs could not establish ordinary build/test health inside the
  frozen runtime.

The coordinator therefore records the P0 result as a **mixed methodology and
model failure**, not evidence for or against Repository-as-State.

## Claim boundary

From P0 we may still report descriptive resource-use, reconstruction and
persistent-history observations. We may not compare A/B correctness, claim
equivalence/non-inferiority, claim RaS support, or claim evidence against RaS.

## Required remediation before P1 or replication

Two independent defects must be fixed before another causal correctness study:

1. **Runtime/workspace validity**
   - agents must receive an exact historical PRE on a normal writable local
     branch rather than a detached HEAD;
   - no future refs, unreachable future objects, remotes or private verifier
     material may be present;
   - deterministic offline build/restore prerequisites must be available without
     widening network access.

2. **Task-spec/verifier alignment**
   - every governing behavioural verifier check must be explicit in, or
     reasonably entailed by, the task specification shown to both conditions;
   - hidden verification may remain hidden, but hidden *requirements* may not;
   - implementation-specific copy markers or exact historical-patch details
     cannot govern acceptance unless they are themselves a legitimate explicit
     requirement;
   - every verifier check must have a frozen task-spec-to-behaviour mapping
     before model invocation.

P0 will not be rerun. Any corrected study is a new protocol/experiment version.

Private post-P0 forensic package SHA256:

`c784c805ea05a8242b57b0d18b764ee0d1ff04ebbe6ff36e3530aac6352f0ed6`

Current next step:

`POST_P0_REMEDIATION_V1`.
