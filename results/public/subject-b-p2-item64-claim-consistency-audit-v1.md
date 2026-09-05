# Item 64 claim-consistency audit

This audit covers the public Level-2 P2 publication and the paper/evidence surfaces aligned to the coordinator-accepted P0, P1 and P2 research state.

## Authoritative empirical status

P0 was executed exactly once and classified `MIXED_METHODOLOGY_AND_MODEL_FAILURE`. Its A/B correctness outcome is not treated as causally interpretable and P0 is not rerun.

P1 observed equal non-zero performance: 18/30 behaviours in each condition, with 30 matched agreements and no disagreements.

P2 observed equal zero performance: 0/39 behaviours in each condition, with 39 matched agreements, no disagreements, and 0/12 candidate-level overall passes per condition. P2 is explicitly floor-limited and is not evidence of successful behavioural preservation, equivalence, non-inferiority, or repository-state sufficiency.

P1 and P2 are not pooled.

## Inventory classification

Files classified `MUST_UPDATE` were changed only where their active publication/status claims were stale or incomplete. Files classified `REVIEWED_NO_CHANGE` were read and retained because their wording was historical protocol, methodology, or already bounded correctly. No experimental/runtime/source file was in scope.

### MUST_UPDATE

- `README.md`
- `aidocs/repository-as-state/README.md`
- `experiments/P1/README.md`
- `paper/README.md`
- `paper/claims-register.md`
- `paper/evidence-roadmap.md`
- `paper/experiment-plan.md`
- `paper/sections/06-repository-sufficiency.tex`
- `paper/sections/10-experimental-method.tex`
- `paper/sections/11-results.tex`
- `paper/sections/12-threats-to-validity.tex`
- `paper/sections/13-discussion.tex`
- `paper/sections/16-conclusion.tex`
- `results/public/subject-b-p2-level2-evidence-v1.json`
- `results/public/subject-b-p2-level2-evidence-v1.md`
- `results/public/subject-b-p2-item64-claim-consistency-audit-v1.json`
- `results/public/subject-b-p2-item64-claim-consistency-audit-v1.md`

### REVIEWED_NO_CHANGE

- `results/public/subject-b-p1-results-v1.json`
- `results/public/subject-b-p1-results-v1.md`
- `results/public/subject-b-p2-item62-output-freeze-v3.json`
- `results/public/subject-b-p2-item62-output-freeze-v3.md`
- `results/public/subject-b-p2-item63-results-v2.json`
- `results/public/subject-b-p2-item63-results-v2.md`
- `results/public/subject-b-p2-item63-blind-adjudication-falsification-v1.json`
- `results/public/subject-b-p2-item63-blind-adjudication-falsification-v1.md`
- `results/public/subject-b-p2-semantic-verifier-qualification-v1.json`
- `experiments/P1/protocol-v1.md`
- `experiments/P1/preregistration-v1.yaml`
- `paper/sections/01-introduction.tex`
- `paper/sections/02-agent-continuity-problem.tex`
- `paper/sections/03-repository-as-state.tex`
- `paper/sections/04-transactional-reasoning.tex`
- `paper/sections/05-tiered-execution.tex`
- `paper/sections/07-cost-model.tex`
- `paper/sections/08-executable-memory.tex`
- `paper/sections/09-security.tex`
- `paper/sections/14-related-work.tex`
- `paper/sections/15-future-work.tex`
- `paper/sections/17-externalising-engineering-continuity.tex`
- `paper/sections/18-durable-documentation.tex`
- `paper/sections/19-repository-resumability.tex`
- `paper/sections/20-repository-agent-state-scalability.tex`
- `paper/sections/21-authoritative-state-principle.tex`
- `paper/validation-audit.md`

### NOT_RELEVANT

Other tracked source, runtime, test, figure, bibliography, and unrelated historical handoff files were not publication surfaces for this Item 64 change.

## Claim changes

The claims register records P2 as a bounded empirical claim with an explicit floor-effect status. The paper distinguishes P1's equal non-zero result from P2's equal-zero result, does not pool them, and states that neither establishes equivalence, non-inferiority, universal repository sufficiency, or cost superiority. The P2 recovery history and denominator repair are retained as methodological evidence.

## Coordinator review correction

The first Item-64 draft worker correctly aligned the P1/P2 result language but missed stale P0 status in active publication surfaces. Coordinator review found four direct contradictions:

- root `README.md` said P0 had not been executed;
- `paper/README.md` said P0 had not been executed and was not ready;
- `paper/experiment-plan.md` presented pre-run P0 state as current state;
- `paper/sections/11-results.tex` said P0 had not been executed.

`paper/sections/10-experimental-method.tex` also used pre-run tense without clearly identifying P0 as historical.

All were repaired on the Item-64 draft before coordinator acceptance. Active publication wording now states that P0 ran exactly once, was classified `MIXED_METHODOLOGY_AND_MODEL_FAILURE`, supplies no causal A/B correctness result, and must not be rerun. Pre-run protocol material retained for provenance is explicitly labelled historical.

This correction is itself part of the Item-64 audit record rather than being hidden.

## Final claim-risk state

- unsupported active overclaims: **0**;
- stale active P0 execution-status claims: **0**;
- stale P1 numeric claims: **0**;
- stale P2 numeric claims: **0**;
- P1/P2 contradictions: **0**;
- public/private protocol exposures introduced by Item 64: **0**.

Remaining scientific limitations are substantive rather than editorial: P0 is methodology/model failure evidence, formal equivalence and non-inferiority remain unestablished, P2 is floor-limited, generalisation beyond Subject-B remains unestablished, and resource/cost superiority remains unestablished.

## Validation requirements

The accepted Item-64 state must preserve valid JSON, clean documentation diffs, correct P0/P1/P2 numeric/status statements, bounded claim language, public/private separation, and documentation-only changes. No experimental execution is part of Item 64.
