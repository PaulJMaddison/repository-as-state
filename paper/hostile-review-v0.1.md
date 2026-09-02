# Hostile pre-experiment review — Repository-as-State paper v0.1

## SUMMARY

The paper asks whether predecessor high-capability reasoning-session state can be discarded after accepted software-engineering transitions because decision-relevant continuity has already been externalised into repository/project artefacts. The original v0.1 framing was intellectually interesting but too generous about novelty, too loose about the causal treatment, over-formalised repository sufficiency with an unobservable KL-divergence expression, and used an additive economic decomposition that could double-count costs.

A current literature audit finds material prior art in Git-bound agent memory, commit-history repository memory, sequential software-evolution evaluation, interrupted-task handoff, repository context files, modular low-cost exploration, durable execution, and AI workflow checkpointing. The closest adverse prior is **Handoff Debt** (KC & Budathoki, arXiv:2606.02875), which finds that repository-only successors on interrupted tasks consume substantially more events and prompt tokens than context-bearing handoffs. **Why Git Is the Memory Solution for the Agentic Development Lifecycle** (Guo, arXiv:2607.14390) also removes any credible claim that Git-bound agent memory is itself new.

After correction, a narrower research gap remains: controlled disposal of predecessor reasoning-session history **after validated accepted transitions** in a genuinely dependent engineering sequence, with matched project state/model/tools/environment and explicit measurement of rediscovery. That is sufficient to justify a methodology pilot if the required isolation gates are implemented before execution.

## OVERALL ASSESSMENT

**Before fixes: 4/10.**

The central idea was plausible, but reviewers could reject it without seeing data because:
- the novelty boundary omitted the closest 2026 work;
- the persistent-agent context model risked a straw-man asymptotic comparison;
- the KL formalism was not operational;
- A/B changed more than one plausible source of state unless the workspace/runtime was canonicalised;
- the economic decomposition mixed conceptual and potentially overlapping quantities;
- RRI risked looking like renamed task success;
- P0 scope was too permissive about C/D.

**After hostile-audit fixes: 6/10.**

The revised theory is narrower and more defensible. It is not yet a strong empirical paper because there are no results and the private subject creates serious external-validity concerns. It is, however, a legitimate pilotable research question rather than a novelty-by-terminology argument.

## MAIN CLAIM AS UNDERSTOOD BY REVIEWER

The defensible claim is not “repositories are memory”.

It is:

> For a declared class of dependent software-engineering tasks, after each task reaches a validated accepted project state, predecessor high-capability reasoning-session history may have sufficiently small marginal value that a fresh matched reasoner can continue without material behavioural loss; whether this is worthwhile depends on the measured rediscovery cost.

“Disposable reasoning” is technically meaningful only in that behavioural/lifecycle sense. The computation is not destroyed without consequence; some of it may be recomputed.

## STRONGEST CONTRIBUTION

The strongest contribution is the **post-acceptance forced-history-reset intervention** combined with honest reconstruction-cost accounting.

The accepted boundary matters because prior work on interrupted handoffs shows repository-only takeover can be expensive before a task's intent/evidence has been fully externalised. RaS provides a falsifiable hypothesis about whether validated engineering boundaries change that result.

The reconstruction probe and small semantic-state ablations are useful mechanism tools, but secondary.

## NOVELTY CONCERNS

The following are not novel:
- Git/repository-backed agent memory;
- repository-aware agents;
- commit-history memory;
- sequential software-evolution evaluation;
- external memory/context retrieval;
- stateless/replaceable compute;
- checkpoint/restart;
- durable workflows;
- model routing;
- lower-cost repository explorers;
- tests/docs as engineering knowledge;
- repository infrastructure with durable storage and replaceable serving nodes.

The paper previously risked claiming too much from their combination.

Closest prior work:
1. KC & Budathoki, Handoff Debt, arXiv:2606.02875.
2. Frank Guo, Why Git Is the Memory Solution for the Agentic Development Lifecycle, arXiv:2607.14390.
3. Shastry et al., Beyond Isolated Tasks / SWE-STEPS, arXiv:2604.03035.
4. Wang et al., Improving Code Localization with Repository Memory, arXiv:2510.01003.
5. Li et al., Learning to Commit, arXiv:2603.26664.
6. Gloaguen et al., Evaluating AGENTS.md, arXiv:2602.11988.
7. Khatri, Do Context Files Help Coding Agents?, arXiv:2607.27250.
8. Al Awad & Ivanov, Cost-Effective Repository Exploration, arXiv:2608.29675.
9. Durable Functions and durable AI semantic-isolation work.
10. Cursor Continuity as repository-state infrastructure precedent.

The remaining novelty is narrow but sufficient for P0, provided no earlier equivalent accepted-boundary A/B study is found in the continuing literature review.

## TECHNICAL SOUNDNESS

The core architecture is technically coherent after clarification.

The crucial requirement is that “fresh session” must not secretly mean “different whole machine state”. A and B need:
- the same accepted repository object graph;
- canonical clean workspace materialisation;
- identical task and stable system/developer experiment instructions;
- same model build/config/sampling;
- same tool schema and executor;
- same base environment/dependencies/network policy;
- same verifier.

Persistent condition A may retain predecessor conversation history but must **not** inherit extra untracked files, shell history, IDE state, local databases, or build residue.

If account-level/provider memory cannot be disabled or audited, the treatment is not identifiable on that interface.

## MATHEMATICAL SOUNDNESS

### Removed: KL-divergence repository sufficiency

The original KL expression was not defensible for P0. The action random variable was not operationally defined and the experiment cannot estimate distributions over equivalent engineering actions. It looked more academic than useful.

It has been replaced with a behavioural success target. Later repeated confirmatory studies can define success probability by condition/depth and preregister a non-inferiority/equivalence margin. P0 is explicitly too small for that inference.

### Retained but demoted: quadratic full-history replay

The algebra nB + g*n(n-1)/2 is correct for naive full-history replay.

It is not a realistic universal baseline. Persistent agents can compact, summarise, retrieve, cache, or bound effective history. If effective persistent history is bounded, cumulative supplied input is also linear. The manuscript now states this directly and redraws the conceptual figure accordingly.

### Retained as descriptive: RTF

RTF is useful only as one descriptive ratio. It cannot prove efficiency by itself. Numerator, denominator, total task resource use, failures, and retries must also be reported.

### Demoted: tiered-execution inequality

N_E(c_R-c_E)>C_O is elementary accounting. It is not a novel theoretical result. It is retained only as a sanity condition.

## EXPERIMENTAL DESIGN

The original design was not yet identifiable enough for P0.

Required changes now specified:
- canonical A/B workspace rematerialisation;
- account/session-memory control;
- invariant prompt/model/tool/environment manifests;
- fail-closed FUTURE_HISTORY_LEAK_GATE;
- post-cutoff task-leakage audit;
- frozen verifier hash outside workspace;
- no human rescue;
- preregistered rerun/failure rules;
- frozen corpus window/inclusion-exclusion/task hashes;
- genuine sequential dependence;
- D deferred beyond primary P0.

These are not optional niceties. Failure to implement them converts the experiment into an uncontrolled comparison of two runtime lifecycles.

## ECONOMIC CLAIMS

The original additive cost equations were not acceptable as measured economics because “reasoning”, “context”, and “agent state” can overlap in actual provider billing/inference.

The revised paper reports an observable resource vector and a table of OBSERVABLE / PARTIALLY OBSERVABLE / UNOBSERVABLE quantities.

No provider-internal GPU/KV/cache/margin saving can be claimed from P0 client telemetry.

The most important external evidence is adverse: Handoff Debt reports substantial rediscovery cost for repository-only interrupted-task handoff. RaS must be allowed to lose economically even if it resumes correctly.

## SECURITY CLAIMS

RaS does not prove security improvement.

It permits a least-privilege architecture in which reasoner, executor, verifier, and credentials can be separated. Actual security can get worse through repository prompt injection, malicious tests/dependencies, poisoned durable state, patch/work-package manipulation, compromised commit metadata, and confused-deputy execution.

All positive security claims remain future empirical work.

## RELATED WORK

Related Work was the weakest scholarly section before audit because it missed the closest 2026 overlap.

The revised manuscript now treats Git-bound memory, Handoff Debt, SWE-STEPS, repository-memory localisation, online repository memory, AGENTS/context-file ablations, modular exploration, durable workflows, model routing, and inference-serving work as prior art rather than supporting decoration.

The paper should continue monitoring current 2026 literature before submission because the area is moving rapidly.

## THREATS TO VALIDITY

The strongest threats are:

1. treatment confounding — session reset can change hidden tool/workspace/provider state;
2. private subject/author bias;
3. future-history/task leakage;
4. Handoff Debt as adverse prior;
5. historical survivor/task selection bias;
6. tiny P0 sample;
7. model/provider drift and nondeterminism;
8. verifier leakage/invalidity;
9. documentation/test quality as hidden moderators;
10. reconstruction-cost classification and token telemetry limits.

## MAJOR REQUIRED CHANGES

Before P0 execution:
1. implement and test canonical workspace rematerialisation for both A and B;
2. prove provider/account/session memory is disabled or choose a controllable runtime;
3. implement FUTURE_HISTORY_LEAK_GATE;
4. freeze a reproducible candidate task window and selection rule;
5. freeze task hashes and genuine sequential-dependence justification;
6. freeze hidden-verifier versions/hashes outside workspace;
7. freeze task-leakage audit;
8. freeze reconstruction-probe scoring rubric;
9. freeze resource-accounting classification;
10. freeze timeout/retry/agent-failure/infrastructure-failure rules;
11. commit the preregistration before outcomes.

## MINOR REQUIRED CHANGES

- Keep “transactional” explicitly as lifecycle analogy.
- Do not promote RRI as a standard or major novelty.
- Do not call tests “memory” without qualification.
- Keep conceptual figures visibly labelled non-empirical.
- Do not use subscription pricing to infer internal cost.
- Continue updating the 2026 literature review.

## WHAT WOULD FALSIFY THE PAPER

The strong form is weakened if:
- B materially loses verified task success relative to A;
- sequence success collapses with reset depth;
- reconstruction dominates tokens/events/time;
- required semantic documentation grows like the history it replaces;
- success depends on highly tailored author-created state files;
- advantages disappear on larger/non-local/unrelated repositories;
- the accepted-boundary result resembles the adverse interrupted-handoff result.

See paper/falsification-criteria.md.

## WHAT EVIDENCE WOULD MAKE THE PAPER CONVINCING

A sceptic needs escalation beyond one pilot:
1. valid P0 methodology pilot;
2. repeated same-repository runs;
3. multiple unrelated repositories/task classes;
4. multiple model families;
5. cross-model continuity;
6. independent replication.

See paper/evidence-roadmap.md.

## P0 GO / NO-GO

**GO_WITH_REQUIRED_PROTOCOL_CHANGES**

The theory is sufficiently coherent and the remaining novelty sufficiently specific to justify P0 preparation. P0 is **not ready to execute today** because the corpus, preregistration, isolation gates, verifier hashes, and runtime-control proofs are not yet frozen.

## PRELIMINARY REVIEW SCORE

- **Before hostile-audit fixes: 4/10**
- **After hostile-audit fixes: 6/10**

These are internal pre-review assessments, not venue scores. The absence of empirical evidence caps the post-fix score.
