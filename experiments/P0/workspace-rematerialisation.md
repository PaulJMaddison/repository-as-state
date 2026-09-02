# P0 workspace rematerialisation

The primary P0 treatment is predecessor reasoning-session history. Filesystem/process residue must not become a second treatment.

After each accepted task boundary, both Conditions A and B:

1. freeze the same canonical accepted repository state;
2. destroy the task workspace;
3. create a fresh independent Git workspace containing only allowed history;
4. restore the same declared toolchain/dependency state;
5. apply the same cache policy;
6. apply the same network policy;
7. verify a clean workspace;
8. pass the FUTURE_HISTORY_LEAK_GATE before any model invocation.

Condition A then continues with predecessor reasoning-session history retained.

Condition B starts a new reasoning session with predecessor reasoning-session history absent.

Both conditions lose:

- untracked files;
- incidental build residue except identically controlled caches;
- shell history;
- IDE state;
- scratch files;
- previous process state;
- prior reconstruction-probe output.

## Canonical materialisation mechanism

The public harness creates a **fresh independent Git repository** and fetches only the allowed commit ancestry using a local no-tag object transfer. It then creates the sole allowed branch ref and hard-resets to the allowed commit.

The private source repository is never modified.

The result is not trusted merely because refs were deleted. The leak gate compares all Git objects present with objects reachable from allowed refs and rejects unreachable extras.

## Cache policy

Exact model/runtime/cache settings remain pending. Before P0 becomes run-ready, caches must either be reset or identically prewarmed from the same accepted state under a frozen policy.

## Runtime eligibility

If account-level or cross-session model memory cannot be disabled or audited:

`P0_CAUSAL_RUNTIME_ELIGIBLE=false`

P0 must not quietly proceed on that runtime.
## Fixed cross-condition state progression

To preserve causal identifiability, P0 does **not** let A and B produce different repository states for the next task. For each task, both conditions receive independently materialised copies of the same frozen historical accepted pre-state. Experimental outputs are adjudicated and recorded, but the next task advances to the next frozen historical accepted boundary.

This preserves byte-identical repository state across A/B. It also creates a declared limitation: Condition A may retain reasoning about a materially equivalent prior implementation that differs from the next frozen historical boundary. Stable runtime instructions must state that the rematerialised repository is authoritative.

