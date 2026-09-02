# Terminology — hostile-audit revision

**Repository-as-State (RaS):** the hypothesis/architecture in which accepted software-project state is treated as the primary durable continuity substrate and predecessor high-capability reasoning-session history may be removed between accepted transitions.

**Authoritative project state:** the allowed durable project artefacts at an experimental cutoff: source, tests, schemas, build/configuration, documentation, architecture records and Git history as defined by protocol.

**Reasoning transaction:** a bounded reasoning episode over externally persisted project state that can end after a validated transition. Lifecycle analogy only; does not imply ACID semantics.

**Disposable reasoning:** a reasoning process is disposable with respect to programme continuity when replacing it after an accepted transition does not materially impair the next correct continuation under matched durable state, task, model/configuration, tools and environment. Disposal may require recomputation.

**Persistent-history control (A):** condition retaining predecessor reasoning-session history while rematerialising canonical workspace/environment state.

**Forced-reset condition (B):** fresh reasoning session with predecessor reasoning history absent while other declared causal inputs are matched.

**Reconstruction:** selection and inspection of project information needed to understand the current task after reset.

**Tiered execution:** a secondary architecture separating high-capability reasoning from a lower-cost/stateful/constrained execution worker. Not necessary for RaS and not primary P0.

**Repository sufficiency:** conditional behavioural adequacy of allowed project state for a declared task/model/environment/depth; not an intrinsic repository property.

**RRI:** Repository Resumability Index, a descriptive proportion of eligible reset continuations that pass the behavioural verifier.

**RTF:** Reconstruction Token Fraction, reconstruction-attributed input tokens divided by total forced-reset input tokens.

**Decision-relevant semantic state:** durable information required for future correct action. The phrase describes a mechanism; persisting engineering decisions is not claimed as novel.

**Agent-state scalability:** the architectural objective of increasing concurrent/long-horizon programmes without proportionally increasing persistent high-capability reasoning-session state requirements.
