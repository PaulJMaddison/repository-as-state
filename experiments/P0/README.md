# P0 — Forced-State-Reset Pilot

**Status: NOT EXECUTED.**

P0 is the initial pilot for evaluating whether sequential software-engineering work can continue correctly after complete conversational-state reset.

The likely P0 subject is a private proprietary software system, but this public repository contains no proprietary source, private diff, hidden verifier implementation or private model trace. P0 must be prepared so that private subject or evidence remains private and only sanitised aggregate evidence crosses the publication boundary.

## Pilot objectives

1. Exercise the forced-reset protocol end to end.
2. Validate task packaging and state-reset enforcement.
3. Validate hidden-verifier independence.
4. Measure reconstruction telemetry, including RTF.
5. Estimate variance and failure modes for later power analysis.
6. Test whether the public or private evidence pipeline is adequate.

## Reset rule

Between eligible sequential tasks in reset conditions:

- terminate the reasoning session;
- do not use resume;
- do not provide prior conversation;
- do not provide an external session summary;
- do not copy hidden memory;
- provide only the allowed repository snapshot plus the current task.

## Evidence

Raw private evidence stays outside this repository. Public P0 outputs, if approved for release, should contain protocol version, task IDs, condition labels, depth, aggregate success or failure, sanitised verifier outcome, reconstruction telemetry, timing, model or runtime metadata, intervention flags and hashes of publication-safe artefacts.

Use protocol-template.yaml and preregistration-template.yaml as starting points. They intentionally contain no results.
