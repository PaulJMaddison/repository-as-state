# Subject C Level-3 workspace-access qualification v1

Item 65 substage 65F performed a zero-model filesystem/materialisation qualification after the first locked Subject-C execution block was permanently closed.

The root cause was identified in the workspace materialisation path: copied Subject-C source files carried protected empty DACLs and did not inherit the access required by the restricted execution path, including the Codex sandbox principal used by the successful Subject-B P2 precedent.

A minimum repair was proved on disposable fixtures only. Under the restricted non-admin execution identity, the repaired disposable tree supported read, create, modify and delete operations while protected private roots remained denied.

The failed Subject-C execution workspaces were not modified. No consumed unit was rerun. No Subject-C task-solving model, project build, compiler/typechecker, project/public test, lint, hidden verifier against model output or correctness adjudication was run.

Private workspace-access qualification package commitment:

`8b586ce8ff7821033b5b354f6a7c2ecf6a2e6860b6e79a9acdc4bbe76ffdb1a3`

An additional disposable `codex sandbox` wrapper probe did not execute its harmless command and therefore did not pass. This does not alter the filesystem root-cause result, but the next fresh execution lock must include a zero-model exact-runtime workspace-access readiness gate before any model-active execution is permitted.

65F is accepted as `WORKSPACE_ACCESS_ROOT_CAUSE_REPAIRED_AND_QUALIFIED`.

The first 18-run Subject-C block remains permanently closed and has no correctness result. The next experimental step is 65G: create a completely fresh preregistration/execution lock with a new schedule, blind mapping, workspaces and execution state. Nothing from the failed block may be resumed or converted into a retry.
