# From stateful agents to transactional reasoning

RaS treats a reasoning session as a transaction rather than a durable process:

    R_t + U_t
      -> high-capability reasoning transaction
      -> validated state transition
      -> R_(t+1)

After the transition, reasoning state may be destroyed.

This framing changes the scalable unit from a persistent long-lived agent process to an **independent reasoning transaction**. It also creates explicit commit semantics: proposed work is not durable continuity until it has been encoded into repository artefacts and validated.

The analogy to stateless application compute is deliberately limited. A reasoning transaction may still be expensive, nondeterministic and dependent on a large model. RaS does not make the computation stateless within the transaction; it asks whether the programme can be resumable between transactions without durable conversational state.
