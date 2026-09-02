# Threats to validity

This document is intentionally pessimistic. A strong RaS result is only meaningful if alternative explanations are made difficult.

## External validity

- **Single-repository bias:** success on one codebase may reflect unusual structure or documentation.
- **Single-model bias:** results may depend on one model's repository-navigation strengths.
- **Repository complexity:** small or unusually clean repositories may overstate resumability.
- **Task locality:** local tasks may require little historical state and therefore favour reset conditions.
- **Dependency width:** tasks spanning many modules or services may expose reconstruction limits.
- **Generalisation beyond software engineering:** results should not be extrapolated to general agents without evidence.

## Construct validity

- **Documentation quality:** deliberately maintained state files could dominate the result and turn the experiment into a documentation-quality test.
- **Reconstruction-cost classification:** incorrectly labelling ordinary reasoning as reconstruction, or vice versa, can bias the economic result.
- **Hidden-verifier bias:** the verifier may reward narrow task interpretations or leak implementation assumptions.
- **Repository sufficiency proxy:** RRI and task success do not directly observe the conceptual action distribution used in the epsilon-sufficiency formulation.
- **Token telemetry gaps:** provider interfaces may omit cached tokens, internal retrieval or hidden system context.

## Internal validity

- **Task selection bias:** chosen tasks may favour the architecture.
- **Historical commit survivor bias:** selecting tasks from changes that are known to have succeeded can exclude realistic dead ends.
- **Future-history leakage:** later files, tests, comments or commits can reveal solutions unavailable at the intended task time.
- **Human intervention:** untracked steering can reintroduce external continuity.
- **Experiment-order effects:** agents, operators or infrastructure may benefit from repeated exposure to the same task family.
- **Contamination:** model pretraining, benchmark exposure or accidental cross-condition artefacts may carry solution information.
- **Model nondeterminism:** stochastic outputs can be mistaken for architecture effects.
- **Provider updates:** model or platform changes during the study can confound longitudinal comparisons.
- **Prompt caching:** cache behaviour can distort token-cost comparisons if it differs across conditions.

## Reproducibility and statistics

- **Private subject reproducibility:** proprietary subjects limit external replication and require later public replications.
- **Statistical power:** P0 is a pilot; small samples cannot support strong general claims.
- **Multiple comparisons:** later ablations and depth analyses require a predeclared analysis plan.
- **Missing data:** failed telemetry and aborted runs must not be silently excluded.

## Falsification condition

The strongest direct criticism is that RaS merely moves cost from conversation replay to repository rediscovery. The experiments must therefore measure reconstruction cost. If reconstruction becomes expensive enough to erase outcome-normalised efficiency gains, that finding weighs against a strong RaS claim.
