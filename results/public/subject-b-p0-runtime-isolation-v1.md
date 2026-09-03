# Subject-B P0 runtime/isolation freeze v1

The Protocol v1 corpus and runtime preparation package are frozen without running P0 or invoking an experimental agent. The configured model is explicitly `gpt-5.6-luna`; session semantics, workspace materialisation, execution order, retry policy and metrics collection are recorded.

Preparation checks passed for exact PRE materialisation and identity, clean leak-gate controls, and synthetic contamination rejection. The package is not ready to execute because the current host exposes unrestricted filesystem access, cannot enforce separation between model-provider transport and agent-tool network access, and does not provide an auditable cross-session-memory boundary. The original protocol also specifies no binding task timeout, so timeout approval remains pending.

The runtime freeze hash and corpus-lock hash are cryptographic commitments. Sensitive task, checking, credential and local-environment material is excluded from this public summary.

Next step: `HUMAN_SELECT_ISOLATED_RUNTIME`.
