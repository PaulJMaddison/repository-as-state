# Subject-B P2 execution lock v3

Item 61 is accepted again after repair of the restricted Codex runtime-access failure discovered before any fresh Item-62 model activity.

The repair provisioned an isolated experimental runtime at `C:\Kyntic\ras-p2-experimental-runtime-v2` for `DESKTOP-BFTREBH\ras-p2-experimental`, retaining the exact `codex-cli 0.153.0-alpha.5` runtime and target model `gpt-5.6-luna` while preserving the protected coordinator/private boundary.

The prior v2 execution lock remains preserved as historical evidence of the readiness assumption that was later falsified. This v3 lock supersedes v2 for execution only.

All frozen experimental choices remain unchanged: prompts, model, PRE workspaces, randomisation, schedule and blind mapping. No fresh Item-62 scheduled unit reached model activity during repair or relock; accepted units remain 0, hidden-verifier runs remain 0 and correctness adjudications remain 0.

Private v3 identities:

- execution-lock manifest: `A0A8D89CDC226EE5619C9AA0BE80F936EC84B6218EA14E84F992B650699844DD`
- execution-lock contents manifest: `C774396F9F56DD94CFE0194E2916F891CF5D9CF6DD29D63F6E97AE48A9FBFC73`
- execution-lock package: `908CCB709B08379E616EF62C04B996DB7A526ED91BB66E73491CDE3D8C377D99`

All SHA-256 values repeat, the package bindings validate, and the public record contains no seed, private schedule, blind mapping, hidden verifier, credentials or correctness results.
