# Subject-B PR8-base boundary recovery

Status: **retry required because the previous worker queried the wrong repository remote**.

The previous worker classified PR8 base as `UNRESOLVED_HISTORICAL_OBJECT` after looking for the SearchForCars historical objects through the `repository-as-state` remote. That classification is invalid.

The authoritative historical source repository is:

`PaulJMaddison/searchforcars`

Local source repository:

`C:\Sass\searchforcars`

The required historical objects are available in the SearchForCars repository/hosting API:

- PR8 merge: `575dc1e531c2a5e6bf39579869720fb8c6deff76`
- PR8 first parent/base: `b818d5e50c588113529c5545843446618dba4e4e`
- PR8 reviewed head/second parent: `5658fa1ae922afa56ba76f1d8dffd9bd95d60209`
- B4 predecessor: `96aa7162faa48e47104916331a9ffcfd66af7171`

GitHub PR #8 also resolves and records the same merge/base/head identities.

No boundary acceptance claim is made by this correction. The exact PR8-base state still needs to be materialised from the SearchForCars repository and subjected to the restore/build/test accepted-boundary gate. Candidate contracts remain unfrozen and no discriminator or P0 run has occurred.

Next step: `VALIDATE_PR8_BASE_FROM_SEARCHFORCARS_SOURCE`.
