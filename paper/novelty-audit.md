# Novelty audit — Repository-as-State paper v0.1

## Bottom line

The broad novelty case does **not** survive hostile review.

The literature already contains repository-aware coding agents, Git-bound agent memory, commit-history memory, sequential software-evolution evaluation, interrupted-task agent handoff, repository context files, lower-cost repository exploration, durable workflow recovery, model routing, and repository infrastructure with durable state plus replaceable compute.

The defensible RaS novelty is narrower:

1. deliberately terminating high-capability reasoning-session state **after validated accepted engineering transitions**, not during partial work;
2. a matched A/B experiment intended to vary predecessor reasoning-session history while holding accepted repository state, dependent task, model/configuration, tools, and environment constant;
3. treating rediscovery cost as an outcome capable of defeating the thesis;
4. combining accepted-boundary forced reset with a non-chain-of-thought reconstruction probe and semantic-state ablation to identify marginal continuity carriers.

RRI, Git persistence, tests, sequential tasks, repository retrieval, model routing, tiered execution, and “repository memory” are not individually strong novelty claims.

## Closest-work matrix

| Work/system | Durable state mechanism | Model-native persistent state | Repository use | Restart/resumption behaviour | Context reconstruction | Explicit forced reset? | Reconstruction cost measured? | Reasoning/execution separation? | Continuity metric? | Empirical SE evaluation? | Similarity to RaS | Remaining RaS distinction |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SWE-agent (Yang et al., 2024) | Repository + environment state during task | Agent trajectory/context | Direct repo editing/search/tests | Task-local agent execution | Repository exploration | No sequential history intervention | Token/context design indirectly | Tool/interface separation | No RaS-style continuity metric | Yes | Repository-aware coding | Does not isolate predecessor-history value across accepted dependent transitions |
| OpenHands / SDK (Wang et al., 2024/2025) | Sandbox/workspace plus configurable memory | Supports memory/lifecycle mechanisms | Direct | Lifecycle and sandbox abstractions | Agent/tool dependent | No matched accepted-boundary history ablation identified | General telemetry, not RaS rediscovery estimand | Yes, modular tools/runtime | No | Yes | Strong execution/lifecycle overlap | RaS focuses on causal disposal of reasoning history, not runtime platform design |
| SWE-STEPS (Shastry et al., 2026; arXiv:2604.03035) | Accumulating repository across dependent PRs | Conversational setting retains interaction | Central | Sequential evolution | Agent dependent | No matched persistent-vs-reset treatment | Not the central contribution | No | Sequential task success/health | Yes | Strong overlap on dependent task chains | RaS treatment is predecessor-history availability at each accepted boundary |
| Handoff Debt (KC & Budathoki, 2026; arXiv:2606.02875) | Frozen partial repository state | Raw trace / summary / structured-note alternatives | Central | Successor takeover after interruption | Explicit repo-only rediscovery | Yes in spirit: successor lacks predecessor context | **Yes**: events/tokens/time-like effort | Not primary | Handoff solve/efficiency outcomes | **Yes** | **Closest empirical overlap and adverse prior** | Handoff occurs during partially completed tasks; RaS resets after validated accepted transitions |
| Why Git Is the Memory Solution... (Guo, 2026; arXiv:2607.14390) | Git-bound ledger, structural map, commit-session links | Session episodes deliberately persisted | Central | Later query/reconstruction over Git-bound memory | Explicit routing/reconstruction | No disposal experiment | Token use measured | Router separates query modes | Answer sufficiency/retrieval | Yes, on production history | Very strong overlap with “Git/repo as memory” | Guo persists session-derived reasoning; RaS tests absence of predecessor session state |
| Improving Code Localization with Repository Memory (Wang et al., 2025; arXiv:2510.01003) | Commit-history non-parametric memory | Memory retrieved per task | Central | New tasks use historical repository memory | Explicit retrieval | No | Localisation evaluation, not handoff cost | No | Localisation metrics | Yes | Repository history as memory | Does not test accepted-boundary session disposal |
| Learning to Commit (Li et al., 2026; arXiv:2603.26664) | Online repository memory distilled from chronological commits | Learned/project skills carried forward | Central | Future tasks use accumulated skills | Explicit reflection/memory | No | Not RaS reconstruction estimand | No | Organicity/correctness metrics | Yes | Repository evolution as durable memory | RaS does not learn extra skills from oracle future diffs; tests history removal |
| Evaluating AGENTS.md (Gloaguen et al., 2026; arXiv:2602.11988) | Repository-level context files | File content injected to agent | Central context artefact | New task receives context file | Agent explores repository | No | **Yes**, reports increased inference cost | No | Task success | Yes | Tests semantic state files | Direct warning that more repository context can hurt |
| Do Context Files Help? (Khatri, 2026; arXiv:2607.27250) | AGENTS/CLAUDE-style files | Context file supplied per run | Central | Per-task fresh evaluation | Repository exploration | Controlled context ablation, not history reset | Token/behavioural analysis | No | Correctness with equivalence framing | Yes | Strong methodological overlap on context ablation | RaS studies predecessor-history treatment at sequential accepted boundaries |
| Cost-Effective Repository Exploration (Al Awad & Ivanov, 2026; arXiv:2608.29675) | Repository inspected by explorer | Explorer context per task | Central | Not programme-resumption study | Explicit exploration stage | No | **Yes**: tokens/time | **Yes**, modular exploration | Localisation metrics | Yes | Strong overlap with tiered exploration | Makes tiered lower-cost exploration non-novel; RaS core continuity remains separate |
| MemGPT (Packer et al., 2023) | Multi-tier external memory | Explicit managed memory | Not repository-specific | Long-horizon interaction | Memory retrieval | No | Context management central | No | Memory/task outcomes | Not SE-specific | External-memory precedent | RaS asks whether predecessor interaction can disappear rather than be retained in memory |
| Durable Functions (Burckhardt et al., 2021) | Durable workflow history/state | N/A | No | Failure recovery / replay | Deterministic replay | Worker replacement yes | Systems overhead, not repo rediscovery | Compute/storage separation | Workflow correctness | Systems evaluation | Strong checkpoint/restart precedent | RaS reconstructs semantic engineering state for nondeterministic reasoners |
| BEGIN AI TRANSACTION (Mozafari, 2026; arXiv:2608.05412) | Durable workflow/checkpoint state + semantic resource bindings | Continuation state persists | Not repository-specific | Paused/resumed AI workflows | Semantic environment validation | No RaS-style accepted-boundary history ablation | Middleware overhead | Workflow middleware | Isolation anomalies | Empirical source audit/prototype | Terminology and durable-workflow overlap | RaS uses “transactional” only as lifecycle analogy; different semantic question |
| RouteLLM (Ong et al., 2024) | N/A | N/A | No | Per-request routing | N/A | No | Cost/quality routing | Yes by model capability | Routing quality/cost | Yes | Tiering precedent | Model routing is not RaS novelty |
| vLLM/PagedAttention; DistServe; Mooncake | KV-cache / serving infrastructure | Inference serving state | No | Serving lifecycle | N/A | No agent reset experiment | Serving throughput/latency | Yes at serving layer | Serving metrics | Systems evaluation | State-cost infrastructure context | Do not imply session termination equals dedicated GPU release |
| Cursor Continuity (Martí, 2026) | S3-compatible WAL + repository materialisation | None | Repository infrastructure itself | Serving nodes can reconstruct repo state | Repository materialisation | No agent experiment | Repository systems focus | Storage/serving separation | No agent metric | First-party production description | Architectural analogy | Repository-state scalability, not agent-state continuity |

## Reviewer conclusion on novelty

### Claims that must be abandoned as novelty

- “Git can be memory.”
- “Repositories can preserve agent context.”
- “Commit history can provide long-term repository knowledge.”
- “Sequential coding tasks should be evaluated as chains.”
- “Fresh agents can resume from repository state” in the broad, unqualified sense.
- “Context/repository exploration should be measured.”
- “Cheaper models can perform repository exploration.”
- “Durable compute can be reconstructed from external state.”
- “Repository-serving compute can be replaceable.”
- “Tests/docs can preserve engineering knowledge.”

### Plausibly novel research gap worth P0

The reviewed work does not establish a matched, post-acceptance experiment in which a dependent engineering programme is advanced through validated repository states and the experiment deliberately destroys predecessor high-capability reasoning-session history at each accepted boundary while holding the other causal inputs fixed and measuring both correctness and rediscovery.

That is narrow enough to be defensible and specific enough to falsify.

## What would kill the novelty claim

The novelty case should be revisited immediately if prior work is found that already:

1. uses dependent sequential software-engineering tasks;
2. resets the reasoner after accepted/verified task boundaries;
3. compares against a matched history-retaining control;
4. holds workspace/model/tools/environment fixed;
5. measures repository reconstruction cost and continuation quality.

If such work predates RaS, the paper becomes primarily a replication/measurement study unless it contributes a materially different intervention.
