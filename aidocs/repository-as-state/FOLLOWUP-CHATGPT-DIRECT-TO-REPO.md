# Follow-up — ChatGPT direct-to-repo workflow

Status: OPEN

This is a tooling/workflow follow-up and is **not part of the Item 65 Subject-C experiment**.

After the current Subject-C execution blocker is handled, fix and verify the ChatGPT direct-to-repository workflow end-to-end.

Required outcome:

- ChatGPT can read the target GitHub repository directly;
- ChatGPT can create/update repository files directly through the connected GitHub workflow;
- branch/ref handling is explicit and reliable;
- authoritative HEAD is verified before writes;
- writes are confirmed against the remote after completion;
- no unnecessary copy/paste handoff is required for normal direct-to-repo work;
- failures/authentication/connector issues are surfaced clearly rather than silently falling back to manual workflow.

Do not change Item 65 methodology or experimental state as part of this follow-up.
