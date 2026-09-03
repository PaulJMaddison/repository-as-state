# Runtime-v3 private validation — partial success

The merged public writable-PRE materialiser has now been validated against all
three real historical SearchForCars PRE states inside the isolated `RAS-P0`
runtime.

Validated:

- WP04, WP05 and WP06 PRE materialisation all pass;
- all three workspaces are on the writable `ras-experiment` branch;
- all three have no remotes, no future/unreachable objects and pass the leak gate;
- repository-safety edit/status probes pass for all three;
- the previous P0 build limitation is classified as missing toolchain/dependency
  support rather than a repository-state defect;
- a frozen offline dependency store containing 55 public NuGet packages was
  created;
- offline restore and build pass for all three historical PRE states;
- A/B workspace materialisation, offline toolchain, network policy and
  repository-safety state are matched.

The runtime is not yet ready for a future causal experiment because the
provider-relay/network-control matrix and the synthetic Codex editing probe were
not completed safely in this validation run. No synthetic model invocation was
made and no additional experimental agent run occurred.

Private remediation package SHA256:

`3c4ca79b22cc7fc9f8d77a8621e94b1c750ee15b9017926b03c28385b30d091b`

Current next step:

`COORDINATOR_RUNTIME_V3_NETWORK_AND_MODEL_PROBE_REVIEW`.
