# Core thesis

Repository-as-State (RaS) investigates a narrow systems claim for software engineering:

> Durable engineering continuity does not necessarily need to live inside the expensive high-capability reasoning process.

The intended architecture makes high-capability reasoning **disposable**. A reasoning process consumes durable repository state R_t and a current task U_t, proposes a bounded state transition, and relies on execution plus deterministic evidence to produce R_(t+1). The reasoning process may then be destroyed. A later fresh process reconstructs the decision-relevant engineering state from the repository.

This is not the claim that Git stores “memory”, nor the observation that coding agents can read repositories. The research question is whether repository state can carry enough decision-relevant semantic continuity that complete conversational-state reset does not materially reduce long-horizon engineering success.

RaS therefore separates three things that are often conflated:

1. **Durable authoritative state** — source, tests, schemas, history, design records, build information, evidence.
2. **Active inference context** — the bounded subset reconstructed for one reasoning transaction.
3. **Ephemeral computation** — high-capability reasoning and execution processes that can be replaced.

The project begins from repeated practical observation of such a workflow. That observation motivates controlled experiments; it is not itself proof.
