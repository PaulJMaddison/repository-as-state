# Repository-as-State programme matrix

Authoritative normalized ledger established 2026-09-03.

Current status: **60 complete / 67 total**. Item **61 active — restricted Codex runtime-access repair and superseding execution relock**. Item **62 blocked until that repair is accepted**.

Legend: ✅ complete · 🟡 active · ⬜ pending/blocked

| # | Item | Status |
|---:|---|:---:|
| 1 | Define Repository-as-State research question | ✅ |
| 2 | Define authoritative repository state | ✅ |
| 3 | Define accepted/validated work-package boundary | ✅ |
| 4 | Distinguish repository-as-state from repository-as-prompt | ✅ |
| 5 | Define persistent-session vs fresh-session causal treatment | ✅ |
| 6 | Define central disposability hypothesis | ✅ |
| 7 | Define bounded claim language | ✅ |
| 8 | Establish falsification-first research framing | ✅ |
| 9 | Establish reconstruction-cost as separate claim family | ✅ |
| 10 | Establish resource/correctness separation | ✅ |
| 11 | Literature review: repository/Git memory prior art | ✅ |
| 12 | Literature review: sequential software-evolution benchmarks | ✅ |
| 13 | Literature review: handoff/context-debt evidence | ✅ |
| 14 | Literature review: context/AGENTS file evidence | ✅ |
| 15 | Literature review: durable workflow/checkpoint prior art | ✅ |
| 16 | Literature review: model-serving/KV-cache implications | ✅ |
| 17 | Novelty audit and removal of over-broad novelty claims | ✅ |
| 18 | Hostile reviewer attack inventory | ✅ |
| 19 | Claims register established | ✅ |
| 20 | Evidence roadmap established | ✅ |
| 21 | Experimental matching requirements defined | ✅ |
| 22 | FUTURE_HISTORY_LEAK_GATE defined | ✅ |
| 23 | No-human-rescue / retry discipline defined | ✅ |
| 24 | Blind hidden-verifier methodology defined | ✅ |
| 25 | Principle: verifier may be hidden, requirement may not | ✅ |
| 26 | Implementation-independence standard defined | ✅ |
| 27 | Negative-control and alternate-implementation qualification standard defined | ✅ |
| 28 | SearchForCars selected as Subject B | ✅ |
| 29 | SearchForCars historical corpus recovered | ✅ |
| 30 | WP04 historical PRE/POST boundary proved | ✅ |
| 31 | WP05 historical PRE/POST boundary proved | ✅ |
| 32 | WP06 historical PRE/POST boundary proved | ✅ |
| 33 | Exact WP04→WP05→WP06 historical chain proved | ✅ |
| 34 | P0 corpus/preregistration frozen | ✅ |
| 35 | P0 isolated runtime prepared | ✅ |
| 36 | P0 executed exactly once | ✅ |
| 37 | P0 failure forensics completed | ✅ |
| 38 | P0 classified MIXED_METHODOLOGY_AND_MODEL_FAILURE | ✅ |
| 39 | P0 causal A/B correctness claims rejected | ✅ |
| 40 | runtime-v3 remediation designed | ✅ |
| 41 | runtime-v3 network/provider separation proved | ✅ |
| 42 | runtime-v3 offline materialisation/runtime readiness proved | ✅ |
| 43 | runtime-v3 model positive-control proved | ✅ |
| 44 | runtime-v3 A/B environment parity proved | ✅ |
| 45 | P1 neutral task contracts curated | ✅ |
| 46 | P1 semantic hidden verifiers implemented | ✅ |
| 47 | P1 negative controls qualified | ✅ |
| 48 | P1 alternate-implementation/independence qualification passed | ✅ |
| 49 | P1 private verifier package frozen | ✅ |
| 50 | P1 preregistration/model/prompts/order/retry rules frozen | ✅ |
| 51 | P1 execution lock/public binding/final zero-model gate frozen | ✅ |
| 52 | P1 six-run controlled execution completed | ✅ |
| 53 | P1 six-run blinded freeze completed | ✅ |
| 54 | P1 blind adjudication completed | ✅ |
| 55 | P1 scientific interpretation completed | ✅ |
| 56 | P1 public-safe results, README, evidence roadmap and claims register published | ✅ |
| 57 | P2 candidate inventory / anti-cherry-picking / complexity / telemetry design completed | ✅ |
| 58 | Repair and freeze P2 Level-2 design from corrected four-task corpus: 4 × 3 × 2 = 24 runs | ✅ |
| 59 | Freeze corrected four-task P2 selection and neutral disclosed contracts | ✅ |
| 60 | Implement/qualify P2 semantic hidden verifiers and prove hard hidden-material isolation against actual restricted experimental identity | ✅ |
| 61 | Freeze fresh post-repair P2 preregistration/runtime/prompts/randomisation/public binding/execution lock | 🟡 |
| 62 | Execute fresh accepted 24-run P2 same-repository replication | ⬜ |
| 63 | Blind-adjudicate and scientifically interpret P2 | ⬜ |
| 64 | Publish Level-2 P2 evidence and update paper claims/evidence | ⬜ |
| 65 | Select Subject C and perform cross-repository / Level-3 replication | ⬜ |
| 66 | Final hostile review, statistical/claims/limitations and reproducibility audit | ⬜ |
| 67 | Final paper + reproducibility package + submission-ready release | ⬜ |

## Current count

- Complete: **60**
- Active: **1** (`#61`, runtime-access repair and superseding relock)
- Blocked/pending after active item: **6**
- Total: **67**

## Why Item 61 reopened

The first live Item-62 preflight proved that the restricted non-admin identity could authenticate but could not execute the frozen Codex runtime: Windows returned `Access is denied` before any model process started.

This did not consume an experimental attempt and did not contaminate Item 62:

- fresh scheduled units with model activity: **0/24**
- fresh accepted units: **0**
- hidden verifier runs: **0**
- correctness adjudications: **0**
- Item 62 executed: **false**

However, it empirically falsified the Item-61 execution-readiness claim. The previous execution lock is preserved as historical evidence but superseded for runtime readiness.

Public evidence:

- `results/public/subject-b-p2-item61-runtime-access-falsification-v2.json`
- `results/public/subject-b-p2-item61-runtime-access-falsification-v2.md`

## Repair rule

Repair only runtime accessibility. Do not change task selection, prompts, PRE states, model, randomisation, schedule, blind IDs/mapping, timeout, retry discipline or blindness.

The preferred repair is an isolated experimental-readable Codex runtime under an experimental runtime root, not weakening ACLs on coordinator/private roots. The repaired runtime must be live-tested under `DESKTOP-BFTREBH\ras-p2-experimental` with zero scheduled task-model executions, while the private-material deny boundary is re-proved.

After a fresh zero-model execution lock is accepted, Item 61 returns to ✅ and Item 62 resumes.

## Count rule

An item becomes ✅ only after coordinator acceptance of its complete evidence package. Later empirical falsification can reopen an earlier item and invalidate downstream locks; once the falsified gate is genuinely repaired and accepted, the ledger can advance again without hiding the falsification history.
