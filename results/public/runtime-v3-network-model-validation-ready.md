# Runtime-v3 network/model validation — ready

The post-P0 runtime-v3 remediation is now complete for the controls required
before a future corrected experiment.

## Established runtime-v3 controls

- the canonical shared historical-PRE materialiser creates a normal writable
  `ras-experiment` branch at the exact requested historical PRE;
- real WP04/WP05/WP06 PRE workspaces have no remotes, no future/unreachable
  objects and pass the fail-closed leak gate;
- a frozen offline dependency store allows all three real historical PREs to
  restore and build without model-side internet access;
- provider transport is restricted to `chatgpt.com:443` through the
  privileged host relay;
- provider proxy configuration is scoped to the Codex client process rather
  than exported as general shell network access;
- ordinary agent-tool network activity remains denied;
- the full negative network matrix passes;
- the synthetic provider positive control succeeds with `gpt-5.6-luna`;
- the canonical synthetic writable repository probe succeeds: Codex edits the
  repository and `git status` observes the change without repository-safety
  refusal;
- the root-owned IPv4/IPv6 default-deny network policy automatically restores
  across a controlled `RAS-P0` restart;
- provider access and the negative network controls still pass after restart;
- offline restore/build still pass after restart;
- the final runtime configuration can be applied identically to future A and B
  conditions.

The root cause of the previously unproven runtime-v3 network/model gate was:

`HOST_RELAY_CONFIGURATION_MISSING_AND_PROXY_CONFIGURATION_MISSING`

This was a private runtime/control-plane omission, not a failure of the public
writable-PRE materialiser.

## Validation counts

The independently validated P1 task-contract branch also passed:

- targeted task-contract tests: 9 passed, 0 failed;
- full public suite: 105 passed, 0 failed, 1 known environment-only skip.

## Private evidence commitment

Runtime-v3 network/model probe SHA256:

`b9d06be03ee03e49f697c295f530aad665abf22c4ed6dc078a7f0d97fae537f6`

Prior real-PRE/offline-build remediation SHA256:

`3c4ca79b22cc7fc9f8d77a8621e94b1c750ee15b9017926b03c28385b30d091b`

At this point:

- `RUNTIME_REMEDIATION_READY=true`
- `P1_EXPERIMENTAL_AGENT_RUNS=0`
- `P0_EXPERIMENTAL_AGENT_RUNS_ADDED=0`

P0 remains immutable.

Current next step:

`P1_CORPUS_AND_TASK_CONTRACT_CURATION`.
