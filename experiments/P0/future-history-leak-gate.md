# FUTURE_HISTORY_LEAK_GATE

Version: **0.1.0**

Status: **IMPLEMENTED AND SYNTHETICALLY VALIDATED**

**HARNESS TEST DATA — NOT RESEARCH EVIDENCE.**

A historical checkout inside a complete clone is not sufficient isolation. The P0 workspace must contain only Git objects reachable from explicitly allowed refs and must not be able to retrieve future private state.

## Isolation mechanism

The generic public harness:

1. receives a source repository and one privately supplied allowed commit;
2. creates a fresh independent Git repository;
3. performs a local no-tag fetch of only the allowed commit ancestry;
4. creates the single allowed P0 ref;
5. hard-resets the fresh workspace to the allowed commit;
6. does not configure a remote;
7. runs this gate before any future model invocation.

The source repository is never modified.

## Fail-closed checks

The gate verifies:

1. no Git remotes;
2. no non-empty Git alternates file;
3. no linked-worktree `.git` indirection;
4. only preregistered allowed refs/tags exist;
5. reflog object IDs do not expose history outside reachable closure;
6. each privately supplied forbidden future commit ID is unresolvable;
7. all Git objects physically present are reachable from allowed refs;
8. no selected patch/bundle/archive sidecar is present beside the workspace;
9. no symlink escapes the workspace;
10. workspace is clean;
11. network isolation has been independently asserted by the execution harness.

Any validation/parsing/repository error also fails closed.

Failure contract:

```
FUTURE_HISTORY_LEAK_GATE=FAIL
RUN_VALID=false
ACTION=STOP_BEFORE_MODEL_INVOCATION
```

## Synthetic validation

The generic tests exercise:

- genuinely truncated history;
- duplicate forbidden OIDs;
- invalid SHA;
- configured remote;
- forbidden future branch;
- forbidden future tag;
- future commit retained in reflog;
- deleted refs with unreachable future objects still present;
- Git alternates;
- malformed/non-UTF-8 alternates;
- linked worktree;
- symlink escape;
- future-state sidecar;
- missing network-isolation assertion;
- missing repository;
- empty directory;
- malformed Git directory;
- unsafe export destination;
- existing export destination;
- invalid export OID;
- deterministic failure ordering.

Current harness validation:

`21 tests passed`

This establishes only that the public isolation code behaves as specified on synthetic fixtures. It is **not evidence that Repository-as-State works**.

Implementation commitment:

`9f9e9d76c63338c7b4a7b98a208c94b5663bfb4e0f759b5ddba09c91c06f836b`
