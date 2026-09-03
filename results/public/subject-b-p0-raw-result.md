# Subject-B P0 raw experimental result

Subject-B P0 has executed under the frozen Protocol v1 runtime and session
contracts.

All six experimental model invocations completed in the preregistered order:

`A1,B1,B2,A2,A3,B3`.

The persistent condition used one exact resumed Codex session across A1/A2/A3.
The reset condition used three distinct fresh Codex sessions for B1/B2/B3.
A/B prompt bytes were identical within each task pair. No run timed out.

After all six raw outputs were frozen, the original Protocol-v1 behavioural
verifiers were run. All six verifier harnesses completed, but all six
experimental outputs failed their frozen behavioural verifier:

- WP04: A1 FAIL, B1 FAIL
- WP05: A2 FAIL, B2 FAIL
- WP06: A3 FAIL, B3 FAIL

This raw result is **non-discriminating for the primary A/B correctness
question** because the persistent-history control failed every task as well as
the fresh-session condition. It must not be presented as evidence that reset
history is worse, equivalent, or better.

A post-experiment failure-forensics pass is required to determine whether the
all-fail outcome reflects task difficulty, task-specification insufficiency,
execution/runtime effects, a shared implementation failure mode, or another
methodological issue. The frozen experimental outputs and verdicts must not be
changed or rerun during that analysis.

Raw experimental-output integrity SHA256:

`fcce7545f5997d78e50319a4cdd7952b97299ad8b14b784c5664d8e44a99c642`

Final private P0 experiment-lock SHA256:

`bd6cdbd0e6ffba07f6f72d33e13ad9262e2807dddb42ba9d29435aa4281365ad`

Current state:

- `EXPERIMENTAL_AGENT_RUNS=6`
- `P0_EXECUTED=true`
- `PRIMARY_CORRECTNESS_RESULT=NON_DISCRIMINATING_ALL_FAIL`
- `NEXT_STEP=POST_P0_FAILURE_FORENSICS`
