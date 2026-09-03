# Subject-B P0 isolated-runtime selection v2

The unrestricted-host runtime correctly failed the isolation gate. The next
candidate for local validation is a dedicated WSL2 execution boundary with
Windows-drive automount and Windows interoperability disabled, unprivileged
condition-specific users, default-deny tool networking, and provider transport
through a privileged allow-listed relay.

This is a **candidate architecture**, not a claim that isolation is already
working. Local privileged validation must prove filesystem denial, provider/tool
network separation and cross-session-memory boundaries before P0.

The immutable Subject-B corpus, Protocol v1 lock, model selection and execution
order remain unchanged. The task timeout remains unresolved and requires
explicit approval before execution.

Experimental agent runs: 0. P0 executed: false.
