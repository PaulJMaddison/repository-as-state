# Subject-B isolated runtime v2 validation status

The first local validation of the WSL2 candidate did **not** falsify the
candidate architecture.

It established:

- shared runtime-readiness code passed the full public suite: 86 passed,
  1 skipped;
- the focused runtime-readiness tests passed: 22 passed;
- WSL2 and hardware virtualisation are available;
- the existing general-purpose Ubuntu distro is not isolated: Windows drives
  are mounted, Windows interoperability is available, host outbound policy is
  permissive, and no provider-only relay exists;
- no dedicated P0 distro was provisioned;
- no condition-specific users, provider relay, default-deny firewall, session
  separation controls or network/filesystem negative controls were created;
- no experimental agent ran and P0 was not executed.

Therefore the result is a **pre-provisioning blocker on the existing host
configuration**, not evidence that the dedicated WSL2 runtime described in
`experiments/P0/isolated-runtime-v2.md` cannot satisfy the protocol.

The next step is to provision and validate the dedicated WSL2 runtime exactly
as specified. If that dedicated boundary cannot enforce the required controls,
then runtime v2 is rejected and a runtime-v3 architecture may be selected.

The immutable Subject-B corpus and Protocol v1 lock remain unchanged.
