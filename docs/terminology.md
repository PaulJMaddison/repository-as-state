# Terminology

**Repository-as-State (RaS):** the hypothesis and architecture in which durable software-engineering continuity is externalised into authoritative repository artefacts and reconstructed for fresh reasoning transactions.

**Authoritative state:** durable, reviewable state whose contents govern the next engineering action. In RaS this is primarily repository state.

**Reasoning transaction:** a bounded invocation of high-capability reasoning over current task plus reconstructed state, ending in a proposed and validated state transition.

**Reconstruction:** the process of selecting and supplying repository information needed for a reasoning transaction.

**Persistent monolithic agent:** a control condition in which a continuing high-capability session retains history and may reason, edit and test.

**Tiered execution:** separation of high-capability reasoning from a lower-cost, stateful or constrained execution worker.

**Repository sufficiency:** the degree to which repository state preserves information needed for future correct engineering action after historical conversational state is removed.

**RRI:** Repository Resumability Index, a proposed empirical metric for successful correct continuation after forced state reset.

**RTF:** Reconstruction Token Fraction, reconstruction tokens divided by total RaS input tokens.

**Decision-relevant semantic state:** durable information required to choose or validate future correct actions, distinguished from lossless replay of historical reasoning.
