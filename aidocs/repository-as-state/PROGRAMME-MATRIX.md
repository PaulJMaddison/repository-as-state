# Repository-as-State programme matrix

Authoritative normalized ledger established 2026-09-03.

Current status: **58 complete / 67 total**. Item **59 active**.

Legend: ✅ complete · 🟡 active · ⬜ pending

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
| 59 | Freeze corrected four-task P2 selection and neutral disclosed contracts | 🟡 |
| 60 | Implement and qualify P2 semantic hidden verifiers for final selected tasks | ⬜ |
| 61 | Freeze P2 final preregistration/runtime/prompts/randomisation/execution lock | ⬜ |
| 62 | Execute accepted 24-run P2 same-repository replication | ⬜ |
| 63 | Blind-adjudicate and scientifically interpret P2 | ⬜ |
| 64 | Publish Level-2 P2 evidence and update paper claims/evidence | ⬜ |
| 65 | Select Subject C and perform cross-repository / Level-3 replication | ⬜ |
| 66 | Final hostile review, statistical/claims/limitations and reproducibility audit | ⬜ |
| 67 | Final paper + reproducibility package + submission-ready release | ⬜ |

## Current count

- Complete: **58**
- Active: **1** (`#59`)
- Pending after active item: **8**
- Total: **67**

## Accepted corrected P2 corpus

Corrected eligible set: `C07,C08,C09,C10`.

- tasks: **4**
- governing behaviours: **13**
- complexity: **3 LOW / 1 MEDIUM / 0 HIGH**
- eligibility re-audit: `D55B610B6E2FFB1B032137F30C348FEFE9EF3542321720090C6690885D749E41`

C06 is ineligible. C07 retains two genuine behaviours; its historical B02 is removed as an over-curated non-delta.

## Accepted item-58 Level-2 design v2

Design: **4 tasks × 3 repetitions × 2 conditions = 24 runs**.

- A: 3 independent persistent chains × 4 chronological tasks = 12 runs
- B: 12 fresh independent sessions
- matched task×repetition units: 12
- full-block blindness: 24 outputs before hidden adjudication
- fresh exact PRE every run
- generated code does not carry
- repetitions are independent replications, not retries
- telemetry remains separate from correctness
- no-human-rescue and no post-activity model-quality retry retained
- descriptive replication only
- formal equivalence/non-inferiority unsupported

Deterministic identities:

- design repair: `D4CCB92E84CC8112EF304E1A674F5E6D98185CD0B212390514B49563632311A4`
- invariant audit: `E7D6D969B24F7158DEADE121DEB91352DDFFCB32AF06E7C5752BA81B74FF6BD1`
- design freeze: `782ADD46591FCCDCABB796D25DC3BE71B03627FCC082372B1FD018875DE1248A`
- design package: `C5124105BD1701A2336211776AF1E3D7E1ED98270665ABAA39910385B81C41F3`

All identities are verified 64-character SHA-256 values and the package's internal bindings validate. The earlier short invariant-audit value was a terminal-response transcription defect only.

Public-safe evidence:

- `results/public/subject-b-p2-level2-design-repair-v2.md`
- `results/public/subject-b-p2-level2-design-repair-v2.json`

## Item 59 gate

Item 59 must create an execution-authoritative corrected four-task selection and neutral contract freeze from `C07,C08,C09,C10` only, with 13 genuine governing behaviours, no C06, and no invented replacement for removed C07 B02.

## Absolute P2 contract/verifier rule

No `dotnet build`, `dotnet test`, `dotnet restore`, compiler, project/solution build/test or probe compilation may be used as contract or verifier qualification evidence at this stage.

No P2 experimental model run may occur before items 59, 60 and 61 are accepted.

## Count rule

An item becomes ✅ only after the coordinator accepts all evidence for that gate. Later falsification may reopen a completed gate before execution; that is expected scientific bookkeeping rather than count drift.
