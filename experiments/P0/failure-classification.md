# P0 failure classification

Failure categories are frozen before experimental execution.

## Categories

**AGENT_TASK_FAILURE**  
The valid controlled environment was available, but the agent failed to complete the neutral engineering task within the frozen rules.

**HIDDEN_VERIFIER_FAILURE**  
The submitted state completed the agent workflow but failed frozen hidden behavioural verification.

**TIME_BUDGET_EXHAUSTED**  
The frozen per-task budget was exceeded. Exact budget values remain pending model/runtime freeze.

**TOOL_FAILURE**  
A permitted experimental tool failed independently of the task solution and meets the frozen infrastructure rule.

**MODEL_PROVIDER_FAILURE**  
The chosen model runtime failed independently of agent decision quality.

**HARNESS_FAILURE**  
The research harness itself malfunctioned or could not enforce a mandatory experimental invariant.

**ENVIRONMENT_FAILURE**  
The frozen local environment could not supply a declared dependency/toolchain condition independently of agent action.

**FUTURE_HISTORY_LEAK**  
The fail-closed history gate detected forbidden history/state. The model must not be invoked.

**TASK_SPEC_INVALID**  
The frozen task specification is later shown to be internally invalid or impossible under its declared pre-state. This classification requires auditable evidence and is not a rescue mechanism for poor performance.

**VERIFIER_INVALID**  
The hidden verifier is shown to reject materially equivalent correct behaviour or otherwise violate its frozen contract.

**RUN_CONTAMINATED**  
Forbidden human/context/state transfer occurred or treatment isolation was otherwise compromised.

## Rerun rule

Only objectively classified **HARNESS_FAILURE**, **MODEL_PROVIDER_FAILURE**, or **ENVIRONMENT_FAILURE** may become rerun-eligible under the final frozen runtime rule.

A run is not rerun because:

- the agent made a poor decision;
- the verifier failed;
- the answer looked incomplete;
- Condition B performed worse than Condition A;
- the result is inconvenient for the hypothesis.

All exclusions and reruns remain auditable.
