# Theoretical model

## Context-scaling model

Assume:

- B is stable base context supplied to a persistent reasoner;
- g is average historical interaction growth added per sequential step;
- n is the number of sequential reasoning steps;
- naive full-history replay supplies all preceding historical growth at every step.

Then cumulative supplied context is:

    T_persistent(n)
      = sum(i=1..n) [B + g(i-1)]
      = nB + g*n(n-1)/2.

For fixed positive g, this model yields Theta(n^2) cumulative supplied information.

For RaS, let K_i be the reconstructed task-relevant input at step i. If reconstruction remains bounded such that K_i <= K for all i, then:

    T_RaS(n) <= nK,

and the cumulative supplied information is Theta(n) under the stated bound.

These are theoretical information-supply models, not measurements of commercial agents. Prompt caching, compaction, retrieval, provider-specific state management, long-context optimisations and changing task complexity can alter observed cost. The model does not assert that all persistent agents literally replay full history or that all RaS reconstructions remain bounded.

## Falsification pressure

The bounded-reconstruction assumption is itself empirical. Repository growth may increase search and rediscovery cost. RaS must therefore measure reconstruction tokens, files read, tool calls, model calls, elapsed time, and cached or uncached context where telemetry permits.

If reconstruction cost grows until it eliminates the expected state-economics advantage, that is evidence against the strong version of the RaS hypothesis.
