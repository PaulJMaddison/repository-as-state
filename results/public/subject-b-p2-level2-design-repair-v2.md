# Subject-B P2 Level-2 design repair v2

Status: **ACCEPTED**.

The corrected P2 eligibility corpus contains exactly four tasks: `C07`, `C08`, `C09`, `C10`, with 13 genuine governing behaviours and complexity distribution 3 LOW / 1 MEDIUM / 0 HIGH.

The superseding Level-2 design is:

**4 tasks × 3 independent repetitions × 2 conditions = 24 experimental runs.**

Condition A contains three mutually independent persistent-session chains, each traversing the four tasks in chronological order. Each task still starts from a fresh exact PRE repository state; generated implementation state never carries between tasks or repetitions. Condition B contains 12 fresh mutually independent sessions. The primary matched unit remains task × repetition, giving 12 matched units.

The repaired design retains full-block blindness: all 24 outputs must be frozen before hidden correctness adjudication. Resource telemetry remains separate from correctness. Repetitions remain independent replications rather than retries. No post-activity model-quality retry or human rescue is allowed. Pre-execution randomisation remains required and is deferred to the final preregistration/execution-lock gate.

The task/run reduction is forced solely by the corrected objective eligibility corpus. No replacement task was selected, no repetition count was changed to recover 30 runs, and no model outcomes, verifier difficulty, desired sample size or complexity balance were used to alter the design.

Interpretation remains **descriptive replication**. The experiment does not justify formal equivalence or formal non-inferiority. Same-repository scope and the absence of HIGH-complexity tasks remain explicit limitations.

Private deterministic identities:

- eligibility re-audit v2: `D55B610B6E2FFB1B032137F30C348FEFE9EF3542321720090C6690885D749E41`
- design repair v2: `D4CCB92E84CC8112EF304E1A674F5E6D98185CD0B212390514B49563632311A4`
- invariant audit v2: `E7D6D969B24F7158DEADE121DEB91352DDFFCB32AF06E7C5752BA81B74FF6BD1`
- design freeze v2: `782ADD46591FCCDCABB796D25DC3BE71B03627FCC082372B1FD018875DE1248A`
- design package v2: `C5124105BD1701A2336211776AF1E3D7E1ED98270665ABAA39910385B81C41F3`

The earlier truncated invariant-audit hash appeared only in the worker terminal response. Direct verification confirmed the private artifact already contained the correct 64-character SHA-256, the package bindings are valid, and no private artifact regeneration was required.

P2 experimental agent runs remain **0**. P2 has not been executed or preregistered.
