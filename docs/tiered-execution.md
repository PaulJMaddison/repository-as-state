# Tiered execution

RaS distinguishes reasoning capability from operational privilege.

A high-capability reasoner may be most valuable for architecture, decomposition, causal reasoning, difficult debugging, review, interpretation and planning. An execution worker may handle repository edits, compilation, tests, formatters, Git and constrained environment interaction.

A simple theoretical utilisation model is:

    C_monolithic = (N_R + N_E) c_R

versus:

    C_tiered = N_R c_R + N_E c_E + C_orchestration,

where N_R and N_E are reasoning and execution units, c_R and c_E their respective unit costs, and C_orchestration the coordination overhead.

Under this model, tiering saves cost when:

    N_E (c_R - c_E) > C_orchestration.

This is a theoretical condition only. Real model pricing, execution quality, retry rates, coordination failures and latency must be measured.

## Least privilege

High intelligence does not imply high privilege. A reasoner may need read, reason and propose access. An executor may need workspace write, compiler, test runner and restricted Git. Production credentials may belong to neither. This separation can reduce blast radius and narrow the trusted computing base if enforcement is outside the model.
