# Security and research-data handling

This repository is public and must be treated as an untrusted publication boundary.

Do not report secrets by opening a public issue. If a secret is accidentally committed, revoke or rotate it first and remove it through an appropriate incident process; Git history should be assumed durable.

The planned experiments may use private software as a subject, but private subject code, verifier implementations, raw model traces containing source, credentials, and customer or employer data are out of scope for this repository. Only sanitised protocol metadata, aggregate measurements, derived statistics, and evidence specifically approved for publication may cross into results/public/.

The security architecture investigated by RaS also follows a least-privilege principle: high-capability reasoning should not automatically imply high operational privilege. Reasoners, executors, and production credentials should be independently scoped.
