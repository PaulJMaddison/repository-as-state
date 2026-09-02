# Theoretical model — hostile-audit revision

## Disposable reasoning

A reasoning process is **disposable with respect to engineering programme continuity** when replacing it after an accepted engineering transition does not materially impair the next correct continuation under a prespecified behavioural comparison, given matched authoritative project state, current task, model capability/configuration, tool interface and execution environment.

Disposable does not mean computation-free. A fresh process may recompute context. Reconstruction cost is therefore a first-class outcome.

## Full-history replay stress model

Let:
- B be fixed base context;
- g be average new historical tokens added per sequential step;
- n be sequential reasoning steps.

Under naive full-history replay:

    T_full(n)
      = sum(i=1..n) [B + g(i-1)]
      = nB + g*n(n-1)/2
      in Theta(n^2).

This is a conditional stress model, **not** a general model of persistent agents.

Let h_i* be effective retained history after compaction, retrieval, summarisation, windows or other context management:

    T_persistent(n)
      = sum(i=1..n) [B + h_i*].

If h_i* is bounded, persistent cumulative input is also linear. Therefore the paper makes no general asymptotic claim that RaS beats persistent agents.

## Reconstruction model

For RaS:

    T_RaS(n) = sum(i=1..n) K_i

with a realistic dependency:

    K_i = f(
      |R_i|,
      task locality,
      dependency width,
      documentation quality,
      test quality,
      architecture quality,
      retrieval quality
    ).

Bounded K is not assumed empirically.

## Behavioural target

For later repeated studies, let Y be hidden-verifier success and c be persistent-history control A or forced-reset B:

    p_c(d) = P(Y=1 | c, depth=d, matched model/environment/task population).

A confirmatory study may preregister a justified non-inferiority or equivalence margin. P0 is too small to establish that inference.

## Falsification pressure

The strong RaS claim is weakened if:
- B loses verified success relative to A;
- complete-sequence success collapses with depth;
- reconstruction dominates resource use;
- success depends on unusually tailored semantic documentation;
- effects disappear with larger/non-local repositories.
