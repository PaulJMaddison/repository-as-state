# Subject-B P2 item-60 hidden-material isolation repair v2

Status: **ACCEPTED**

Worker terminal:

`VALID_TERMINAL_A_ITEM60_HIDDEN_MATERIAL_ISOLATION_REPAIRED_AND_QUALIFIED`

## Why item 60 was reopened

The first live item-62 experimental invocation falsified the previous isolation assumption: the experimental process shared the coordinator Windows identity and could therefore read private methodology by absolute path. The contaminated execution was stopped before any accepted experimental unit completed and before any hidden-verifier adjudication.

The semantic hidden-verifier logic itself was not changed by this repair.

## Repaired boundary

A separate restricted Windows identity is now used for future experimental execution. It is non-administrator and has a dedicated experimental workspace and Codex home outside the private methodology tree.

The restricted identity is denied access to the private RAS tree, coordinator research repository, coordinator Codex profile, sealed methodology roots and contaminated execution evidence. Coordinator access is retained.

## Qualification

Live restricted-token access probes produced:

- forbidden access probes: **14/14 denied**
- private bytes returned: **0**
- absolute-path private reads: **0/6 succeeded**
- private directory-enumeration attempts: **0/5 succeeded**
- allowed workspace operations: **8/8 passed**
- privileged filesystem broker bypass detected: **false**
- tool child more privileged than experimental parent: **false**

This directly addresses the absolute-path access mechanism that contaminated the previous item-62 attempt.

## Semantic verifier immutability

The accepted item-60 semantic verifier artifacts remain byte-for-byte unchanged. Task contracts, task set, model, repetition count and condition definitions were not changed.

The contaminated execution remains preserved for methodology audit, is inaccessible to the restricted experimental identity, is not reused, and was not used for correctness analysis or future schedule selection.

## Isolation freeze identities

- root-cause audit: `8F27A0F784505F7EDE229E5D8B230CC756DA9743C9B2CD9F06AAE9A59AD480BF`
- experimental-identity manifest: `9E1F6C394542F40807F195C9A93A697A7DB9079D68A8B92450EAE9C2CB2BAA6B`
- negative-access probe manifest: `AD6A2F4CB49CE68A9DDF95063461C338FFC79A6F0AF07CE144A6A428BB19069A`
- positive-workspace probe manifest: `3C12BC74661D01B48E33BA5A0FCD7B3802CED763543D167FF82C080BBC052775`
- process-token audit: `7A03DBF35EDF8200A92CF109FC239BA29D8936C4FF3662503BAF27CB77E5927C`
- isolation qualification summary: `2B0DF0851AC5FBEDBCBA04A1BE450F5C8C5587FEB7C089BEF22A5223A4047DA7`
- isolation freeze: `9CD6FE3E1F2B204864B6973B115831411CD911EF4363A5F1139DBFBE795AE266`
- isolation package: `CF652E017FE9E84B95EB671087537294C1953611B2D705BD74BFB55791FB5895`

All listed hashes are 64-character SHA-256 values with repeat matches, and the isolation package internal bindings validate.

## Zero-activity repair

During this repair:

- model completions: **0**
- P2 experimental agent runs: **0**
- task-solving model invoked: **false**
- hidden-verifier experimental adjudications: **0**
- P2 executed: **false**
- P0 rerun: **false**
- P1 rerun: **false**

## Consequence

Item 60 is restored to complete after coordinator acceptance. The old item-61 preregistration/execution lock remains superseded. A **fresh post-repair item-61 preregistration, public commitment and execution lock** is required before any new P2 experimental execution.
