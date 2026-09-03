# Subject-B runtime v2 — credential and session-validation gate

Dedicated runtime-v2 provisioning has now mechanically established the core
local isolation boundary:

- dedicated `RAS-P0` WSL2 distro provisioned from Ubuntu 24.04;
- Windows-drive automount disabled;
- Windows interoperability disabled;
- condition-specific unprivileged users with isolated mode-0700 homes;
- exact Codex CLI version installed;
- filesystem isolation controls pass;
- default-deny IPv4/IPv6 egress is enforced;
- a host-controlled allow-list relay is operational;
- direct GitHub, general web, DNS bypass, direct provider bypass, relay
  allow-list bypass and network-policy modification controls all fail as
  required;
- private/preparation filesystem and privilege-escalation controls fail as
  required;
- historical PRE identities and leak gates remain valid.

No experimental Subject-B agent has run and P0 remains unexecuted.

## Remaining non-experimental gates

The runtime is not yet P0-ready because the clean Linux Codex identity is not
authenticated. Without an approved authentication source the preparation worker
correctly did not:

- run the synthetic Codex provider probe;
- freeze the minimum provider destination set;
- prove Condition-A session resume semantics under the authenticated Linux CLI;
- complete the provider/account-memory audit;
- validate the metrics parser against an authenticated synthetic probe.

The next authorised action should use a **fresh ChatGPT login inside the
dedicated Linux runtime**, not copy an existing Windows `.codex/auth.json`
or existing conversation/session state.

Authentication is a runtime prerequisite, not an experimental agent run, as
long as only synthetic non-Subject-B probes are used.

The task timeout remains a separate human freeze after these authentication and
session controls pass.

Current next step:
`HUMAN_APPROVE_FRESH_LINUX_CODEX_LOGIN_FOR_RUNTIME_V2`.
