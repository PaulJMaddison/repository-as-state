# Tiered execution — hostile-audit revision

Tiered execution is a **secondary architecture**, not a logical requirement of Repository-as-State and not part of P0's primary causal comparison.

A high-capability reasoner may handle architecture, decomposition, difficult debugging, review and evidence interpretation. A separate worker may handle edits, compilers, tests, formatting, Git and constrained environment interaction.

The elementary accounting identity:

    C_M = (N_R + N_E)c_R
    C_T = N_R*c_R + N_E*c_E + C_O

implies tiering is cheaper only when:

    N_E(c_R-c_E) > C_O.

This is not a novel theorem. It simply makes orchestration/retry overhead explicit.

Recent repository-exploration and model-routing work already studies cheaper models for modular suboperations. A later RaS experiment may test whether accepted-state continuity makes such tiering easier, but P0 must not change executor quality while testing history persistence.
