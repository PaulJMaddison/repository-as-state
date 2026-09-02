# Claims register — Paper v0.1

This register is normative for claim discipline. No positive Repository-as-State claim is currently classified as EMPIRICAL.

| ID | Wording | Category | Manuscript location | Support | Current status | Evidence required to upgrade |
|---|---|---|---|---|---|---|
| C01 | Under naive full-history replay with fixed base context and positive average history growth, cumulative supplied context is quadratic in sequential steps. | THEORETICAL | Context Growth | Algebraic derivation from stated model. | Established only under assumptions. | No empirical upgrade required; measure how well assumptions describe real agents. |
| C02 | If task reconstruction remains bounded, cumulative RaS supplied context is linear in sequential steps. | THEORETICAL | Context Growth | Bound on sum of reconstructed contexts. | Conditional on bounded reconstruction. | Measure reconstruction growth across depth/repository size. |
| C03 | Real reconstruction size depends on repository scale, locality, dependency width, documentation/test/architecture quality and retrieval quality. | HYPOTHESIS | Context Growth | Systems model and identified variables. | Untested as quantitative model. | Multi-repository scaling experiment. |
| C04 | RaS was motivated by repeated practical workflows combining high-capability reasoning, bounded execution, deterministic evidence and repository persistence. | OBSERVED | Introduction; Discussion | Author observation. | Motivation only. | Cannot become controlled evidence without prospective protocol. |
| C05 | Repository state can preserve sufficient continuity for complex sequential software-engineering work after complete reasoning-state reset. | HYPOTHESIS | Agent Continuity; Repository Sufficiency | Central research hypothesis. | Untested. | Forced-reset A/B experiments with hidden verification. |
| C06 | Full historical conversation has limited marginal value when decision-relevant engineering state has been durably externalised. | HYPOTHESIS | Externalising Continuity; Sufficiency | Consequence of C05. | Untested. | Controlled comparison with/without history. |
| C07 | Repository-as-State is distinct from repository-as-prompt: durable state may be large while active reasoning context remains selective. | THEORETICAL | Repository-as-State | Architectural definition. | Definition/architecture. | Empirically test reconstruction selectivity and cost. |
| C08 | Tests can carry executable decision-relevant semantic state across reasoning resets. | HYPOTHESIS | Tests and Durable Semantic State | Mechanism argument. | Untested causal contribution. | Semantic-state ablation and hidden verification. |
| C09 | Architecture records and other durable documentation can preserve rationale not recoverable from code/tests alone. | HYPOTHESIS | Durable Documentation | Mechanism argument. | Untested causal contribution. | Documentation ablation and reconstruction probe. |
| C10 | Selective semantic retention is preferable to preserving every reasoning transcript. | HYPOTHESIS | Durable Documentation | Retention-cost argument. | Design hypothesis. | Compare reconstruction quality/cost under retention policies. |
| C11 | Reconstruction cost is a central falsification route for the RaS state-economics thesis. | THEORETICAL | Reconstruction Cost | Follows from cost decomposition. | Established as research design principle. | Measure actual reconstruction costs. |
| C12 | The proposed Reconstruction Token Fraction measures reconstruction tokens as a share of total RaS input tokens. | THEORETICAL | Reconstruction Cost | Metric definition. | Proposed metric. | Validate usefulness/reliability across experiments. |
| C13 | For sufficiently long programmes, RaS may use fewer measured high-capability state/context resources than a persistent agent while preserving quality. | HYPOTHESIS | State Economics | Provider-neutral model. | Untested. | Outcome-normalised A/B telemetry. |
| C14 | Provider GPU allocation, exact KV-cache cost, infrastructure amortisation and provider margin are not directly observable from ordinary experiment telemetry. | EXTERNAL | State Economics | Limits of exposed interfaces; no provider-internal access assumed. | Methodological constraint. | Only provider-internal instrumentation could change this. |
| C15 | Tiered execution is cheaper in the simplified model when N_E(c_R-c_E) exceeds orchestration overhead. | THEORETICAL | Tiered Execution | Algebraic derivation. | Established only under model assumptions. | Measure all terms and quality effects. |
| C16 | Tiered execution can reduce high-capability model utilisation without materially reducing engineering quality. | HYPOTHESIS | Tiered Execution | Planned condition D. | Untested. | Controlled tiered-execution study. |
| C17 | High-capability reasoning and operational privilege can be scoped independently. | THEORETICAL | Security | Architectural separation. | Architecturally feasible. | Security experiments needed for benefit claims. |
| C18 | Separating reasoner and executor may reduce blast radius or trusted-computing-base exposure. | IMPLICATION | Security | Conditional least-privilege argument. | Not empirically demonstrated. | Adversarial security evaluation. |
| C19 | Forced-State-Reset Evaluation directly intervenes on conversational continuity while preserving allowed repository state. | THEORETICAL | Experimental Method | Protocol definition. | Proposed methodology. | Demonstrate intervention integrity in P0. |
| C20 | Future-history availability would invalidate a historical forced-reset experiment. | THEORETICAL | Experimental Method | Causal leakage argument. | Methodological requirement. | Harness proof that future SHAs/remotes are inaccessible. |
| C21 | RRI estimates correct continuation frequency after eligible complete reasoning-state resets under a specified protocol. | THEORETICAL | Repository Resumability | Metric definition. | Proposed research metric. | Repeated experiments; reliability/uncertainty analysis. |
| C22 | A structured state-reconstruction probe can separate state understanding from downstream engineering success without requesting chain-of-thought. | HYPOTHESIS | Repository Resumability | Measurement design. | Untested. | Validate rubric agreement and predictive value. |
| C23 | SWE-bench, SWE-agent and OpenHands establish repository-level software-agent evaluation/execution foundations but do not test the RaS continuity intervention. | EXTERNAL | Related Work | Cited primary papers/platform sources. | Supported literature positioning. | Revise if prior work directly tests equivalent reset conditions. |
| C24 | Agent-memory and context-engineering work studies persistent/selected context, while RaS asks how much historical interaction can disappear after authoritative state externalisation. | EXTERNAL | Related Work | MemGPT, memory surveys, context-engineering source. | Supported distinction, subject to literature audit. | Independent literature review. |
| C25 | Durable Functions provides precedent for volatile compute over durable external execution state, but not evidence for RaS semantic reconstruction. | EXTERNAL | Transactional Reasoning; Related Work | OOPSLA 2021. | Supported precedent only. | No upgrade to RaS evidence without direct agent experiments. |
| C26 | Cursor Continuity provides precedent for durable repository state with replaceable repository-serving compute. | EXTERNAL | Related Work; Scalability | Cursor first-party research article, 18 Aug 2026. | Supported precedent only. | Does not upgrade without RaS-specific experiments. |
| C27 | Repository-state scalability and agent-state scalability are distinct systems problems. | THEORETICAL | Scalability | Layer separation argument. | Architectural distinction. | Empirical interaction can be studied later. |
| C28 | Lower persistent high-capability state requirements may permit greater useful concurrency on fixed inference infrastructure. | IMPLICATION | Scalability; Discussion | Conditional systems implication; KV-cache literature motivates relevance. | Unmeasured. | Serving experiments with controlled workloads. |
| C29 | A broader Authoritative-State Externalisation Principle may apply beyond software engineering. | HYPOTHESIS | Broader Principle | Conceptual generalisation. | Speculative future work. | Domain-specific controlled experiments. |
| C30 | Controlled RaS forced-reset evaluation demonstrates repository sufficiency. | EMPIRICAL | Results | None. | **NOT ESTABLISHED.** | Valid completed P0/replication evidence. |
| C31 | RaS reduces measured cost relative to persistent agents. | EMPIRICAL | Results | None. | **NOT ESTABLISHED.** | Outcome-normalised controlled telemetry. |
| C32 | Tiered RaS execution preserves quality while reducing high-capability utilisation. | EMPIRICAL | Results | None. | **NOT ESTABLISHED.** | Controlled condition-D evidence. |
| C33 | RaS improves security in practice. | EMPIRICAL | Results/Security | None. | **NOT ESTABLISHED.** | Adversarial security experiments. |

## Rules

- THEORETICAL claims remain conditional on their stated assumptions.
- OBSERVED motivation must never be cited as controlled validation.
- EXTERNAL claims support only what the cited source actually establishes.
- HYPOTHESIS and IMPLICATION claims must not be rewritten as findings.
- Positive EMPIRICAL RaS claims require a versioned protocol, exact repository revision, publication-safe evidence, analysis code and documented exclusion rules.
- Provider subscription pricing is not evidence of provider-internal inference cost.
- Conceptual figures and equations are not empirical data.
