# Public/private boundary

This repository is public.

The experiment architecture therefore treats publication as an explicit data-flow boundary:

    private subject / raw evidence
              ->
         sanitisation
              ->
      public aggregate evidence

The public repository must never contain proprietary KynticAI source, proprietary diffs, hidden proprietary verifier source, private source snapshots, credentials, secrets, private model traces containing proprietary source, Very Group material, customer data or unnecessary personal filesystem paths.

A public evidence record may include task identifiers, condition labels, protocol versions, aggregate outcome metrics, reconstruction telemetry, model or runtime metadata that does not disclose secrets, hashes of publication-safe artefacts, and sanitised verifier outcomes.

Sanitisation itself should be auditable. Where a private subject prevents independent reproduction, the limitation must be stated rather than hidden.
