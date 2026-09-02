# Claims register

This register is normative for claim discipline. A substantive statement must remain in its current category until evidence justifies a change.

| ID | Category | Claim | Current support / status |
|---|---|---|---|
| C01 | THEORETICAL | Under naive full-history replay with stable base context B and positive average history growth g, cumulative supplied context is nB + g n(n-1)/2 and therefore Theta(n^2). | Derived in paper Section 7 under explicit assumptions. |
| C02 | THEORETICAL | If reconstructed task-relevant context K_i remains bounded by K, cumulative RaS supplied context is at most nK and therefore linear in n under a non-degenerate lower bound. | Derived in paper Section 7; bounded reconstruction is not yet empirically established. |
| C03 | THEORETICAL | Tiered execution is cheaper in the simplified model when N_E(c_R-c_E) exceeds orchestration cost. | Algebraic consequence of the stated model; not a provider claim. |
| C04 | OBSERVED | RaS was motivated by repeated practical workflows using high-capability reasoning, bounded execution, deterministic evidence and repository persistence. | Author observation; not controlled evidence. |
| C05 | HYPOTHESIS | Repository state can preserve sufficient engineering continuity for fresh reasoning sessions after complete conversational-state reset. | Primary P0/P1 hypothesis; untested. |
| C06 | HYPOTHESIS | Externalising continuity can reduce high-capability state/context burden per successful engineering outcome. | Requires reconstruction and outcome-normalised cost measurement. |
| C07 | HYPOTHESIS | Tiered execution can reduce high-capability model utilisation without materially reducing engineering success. | Planned condition D; untested. |
| C08 | HYPOTHESIS | Tests and other executable artefacts carry decision-relevant semantic state that improves resumability. | Mechanism proposed; requires ablation evidence. |
| C09 | HYPOTHESIS | Reconstruction cost can remain bounded enough for RaS to retain a scaling advantage on useful classes of repository tasks. | Central falsifiable assumption; untested. |
| C10 | IMPLICATION | Lower persistent reasoning-state burden may permit greater useful concurrency on fixed inference infrastructure. | Conditional systems implication only. |
| C11 | IMPLICATION | Separating reasoner and executor can permit narrower operational privileges and blast radius. | Architectural implication; no security benchmark yet. |
| C12 | EXTERNAL | SWE-bench evaluates real-world repository-level software-engineering issues. | Jimenez et al., arXiv:2310.06770. |
| C13 | EXTERNAL | SWE-agent uses an agent-computer interface to let language models act on software repositories and environments. | Yang et al., NeurIPS 2024 / arXiv:2405.15793. |
| C14 | EXTERNAL | OpenHands provides an open software-agent platform and later SDK with sandboxed and composable execution capabilities. | Wang et al. 2024 and 2025. |
| C15 | EXTERNAL | Cursor Continuity persists repository pushes through a WAL in S3-compatible object storage and can materialise local repository state, providing repository-infrastructure precedent. | Cursor first-party article, 18 Aug 2026. It does not prove RaS. |
| C16 | EXTERNAL | Repository-local Cursor rule files have been empirically observed to encode project context and engineering guidance. | Sun et al., arXiv:2608.10622. |
| C17 | EMPIRICAL | Controlled RaS forced-reset experiments demonstrate repository sufficiency. | **NOT ESTABLISHED. No controlled results yet.** |
| C18 | EMPIRICAL | RaS reduces measured cost relative to persistent agents. | **NOT ESTABLISHED. No controlled results yet.** |
| C19 | EMPIRICAL | Tiered RaS execution preserves quality while reducing utilisation. | **NOT ESTABLISHED. No controlled results yet.** |

## Rules

- Never upgrade HYPOTHESIS to EMPIRICAL because a practical workflow “worked”.
- External system results support only the external statement actually made by the source.
- Provider subscription prices are not evidence of provider-internal inference cost.
- Illustrative mathematics must be labelled theoretical or “ILLUSTRATIVE EXAMPLE — NOT EMPIRICAL DATA”.
- Any future EMPIRICAL claim must link to a versioned protocol, public-safe evidence, analysis code and exact repository revision.
