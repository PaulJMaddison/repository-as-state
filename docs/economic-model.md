# Provider-neutral economic model

For a conventional persistent coding agent, define:

    C_persistent =
        C_reasoning
      + C_context/history
      + C_agent-state
      + C_execution
      + C_tools
      + C_orchestration.

For RaS, define:

    C_RaS =
        C_reconstruction
      + C_reasoning
      + C_shallow-execution
      + C_repository-state.

The empirical economic question is whether:

    C_RaS < C_persistent

for sufficiently long engineering programmes while maintaining comparable engineering quality.

## Cost categories

RaS explicitly separates:

1. **Measured cost proxy** — observable tokens, model calls, tool calls, files read, elapsed time, execution time, retry count and provider-billed usage where available.
2. **Theoretical infrastructure implication** — consequences derived from an explicit resource model.
3. **Unobservable provider-internal cost** — internal inference, cache, scheduling, hardware and margin information not available to the experimenter.

Subscription pricing must not be used to infer provider margins or internal inference cost. Chat interfaces must not be treated as “free inference”.

## Reconstruction Token Fraction

    RTF = Reconstruction Tokens / Total RaS Input Tokens.

RTF should be reported with repository size and task depth. Increasing RTF as a repository grows is a direct warning signal for the strong RaS claim.
