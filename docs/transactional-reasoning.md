# From stateful agents to bounded reasoning episodes

RaS uses "reasoning transaction" only as a lifecycle analogy:

    R_t + U_t
      -> bounded reasoning episode
      -> validated state transition
      -> R_(t+1)

After acceptance, the reasoning process may be replaced.

This does **not** imply ACID, serialisability, transactional memory, deterministic replay or database atomicity.

Checkpoint/restart and durable workflow systems are prior architectural precedents. The RaS question is whether a fresh nondeterministic software-engineering reasoner can reconstruct enough semantic state from accepted project artefacts to continue a dependent task programme without predecessor reasoning-session history.

A valid experiment must keep workspace, tools, model/configuration, task and environment matched across persistent-history and forced-reset conditions.
