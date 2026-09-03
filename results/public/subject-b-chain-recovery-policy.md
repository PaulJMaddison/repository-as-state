# Subject-B chain recovery policy after WP04 rejection

Status: privileged corpus preparation only. No P0 execution.

## Trigger

WP04_PR5 was rejected after direct probes showed all eight frozen requirements were already satisfied by PRE.

## Recovery rule

Do not rewrite WP04 and do not search arbitrary commits for a convenient discriminator.

The allowed recovery search space is restricted to **pre-existing reviewed/merged work-package boundaries already present in the historical development graph** between surviving accepted chain states.

For the current B4 -> B5 interval, GitHub history exposes one such boundary:

- PR #8: Merge agentic market acquisition hardening
- merge commit: `575dc1e531c2a5e6bf39579869720fb8c6deff76`
- historically reviewed with recorded build/test evidence
- descendant of B4 / PR #6 merge
- ancestor of B5 / PR #7 merge

## Next gate

1. validate PR #8 merge commit as an accepted engineering boundary using reproducible local boundary evidence;
2. if accepted, freeze two neutral candidate transitions:
   - B4 -> PR8 merge
   - PR8 merge -> B5
3. freeze task specs and hidden behavioural requirements before any new discriminator run;
4. require implementation-independent PRE/POST discrimination and behavioural negative controls;
5. reject the split if either transition cannot satisfy the frozen protocol.

No arbitrary commit search, post-hoc requirement strengthening, or reuse of experimental-agent output is permitted.
