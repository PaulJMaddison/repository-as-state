# Item 64 claim-consistency audit

This audit covers the public Level-2 P2 publication and the paper/evidence surfaces aligned to the coordinator-accepted P1 and P2 results.

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

The claims register now records P2 as a bounded empirical claim with an explicit floor-effect status. The paper now distinguishes P1's equal non-zero result from P2's equal-zero result, does not pool them, and states that neither establishes equivalence, non-inferiority, universal repository sufficiency, or cost superiority. The P2 recovery history and denominator repair are retained as methodological evidence.

## Validation requirements

The final worker validation must report JSON parsing, Markdown/link sanity, stale-number scans, overclaim scans, P1/P2 contradiction scans, public/private protocol exposure scans, `git diff --check`, and a manual diff review. Only public documentation/evidence files may be changed.
