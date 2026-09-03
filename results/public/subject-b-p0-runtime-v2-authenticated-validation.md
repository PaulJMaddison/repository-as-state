# Subject-B runtime v2 — authenticated isolation validation

The dedicated `RAS-P0` runtime has now passed the remaining authenticated
non-experimental isolation checks.

Established controls:

- fresh ChatGPT authentication was completed independently inside isolated Linux
  Codex homes; existing Windows Codex auth/session state was not copied;
- the final provider allow-list is `chatgpt.com:443`;
- authenticated Codex provider transport succeeds through the host-controlled
  relay while direct GitHub, general web, DNS bypass and direct provider access
  remain blocked;
- explicit `gpt-5.6-luna` session resume preserves a synthetic canary;
- a fresh independently authenticated session returns no predecessor marker;
- local Codex homes and session state are mutually unreadable across condition
  identities;
- the frozen condition authentication layout is independent ChatGPT login per
  isolated Linux user;
- the fail-closed network policy now restores automatically across a controlled
  `RAS-P0` restart;
- the metrics probe passes against authenticated Codex JSON output;
- filesystem isolation and network isolation remain ready;
- no Subject-B experimental agent has run and P0 remains unexecuted.

The shared fail-closed readiness evaluator has one remaining unresolved field:
the per-task execution timeout. Runtime isolation itself is ready.

Private authenticated-runtime evidence SHA256:
`5ea8d6fb84ba1a9a4ca64daec777c0a6f296e109ce38b0bcc2cc8a92fbd4e516`.

Current next step:
`HUMAN_FREEZE_P0_TIMEOUT`.
