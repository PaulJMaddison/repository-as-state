# Architectural precedent: durable repository state and replaceable serving compute

Cursor's 2026 engineering article **“Git at any scale”** describes Continuity, a Git storage architecture built around a write-ahead log persisted in S3-compatible object storage. Cursor describes the object-store WAL as the source of truth and local repository copies as materialised or warm-cache state that can be reconstructed on serving nodes.

This is relevant to RaS only as an infrastructure precedent for separating durable repository history from replaceable repository-serving compute.

The distinction is essential:

- Continuity addresses **repository-state scalability**.
- RaS investigates **agent-state scalability**.

Continuity does not test whether fresh reasoning sessions can reconstruct sufficient software-engineering context, does not establish the Repository Resumability Index, and does not prove RaS's cost hypotheses.

Conceptually, the systems can be placed in different layers:

    durable object/log storage
            |
    scalable repository-serving compute
            |
    durable engineering repository state
            |
    ephemeral reasoning
            |
    ephemeral/constrained execution workers

Authoritative source: Vicent Martí, “Git at any scale”, Cursor Research, 18 August 2026, https://cursor.com/blog/git-at-any-scale (accessed 2 September 2026).
