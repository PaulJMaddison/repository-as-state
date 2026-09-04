# Subject-B P2 ten-candidate eligibility re-audit v2

The full P2 historical inventory of ten SearchForCars candidates was re-audited under the original pre-existing eligibility and anti-cherry-picking rules.

The required observable PRE-to-POST behavioural-delta condition was confirmed as explicit or logically required by the original methodology; it was not introduced after seeing the contract defects.

## Result

- candidates audited: **10**
- historically eligible: **5**
- corrected eligible: **4**
- corrected excluded: **6**
- corrected eligible set: **C07, C08, C09, C10**
- corrected selected order: **C07 → C08 → C09 → C10**
- ad-hoc replacements: **0**
- outcome-based eligibility decisions: **0**
- post-hoc slot filling: **false**

C06 changes from historically eligible to **ineligible** because no legitimate disclosed governing behaviour remains that demonstrates the required observable PRE-to-POST behavioural change under the original eligibility rule.

C07 remains **eligible**. Its over-curated non-delta behaviour `P2_T02_B02` is removed rather than replaced, leaving two genuine governing behaviours. C08, C09 and C10 remain eligible.

The corrected four-task set contains **13 genuine governing behaviours**. Every retained behaviour has the required PRE=false / POST=true historical delta, there are zero undisclosed governing requirements, and all task fairness audits pass.

Private eligibility re-audit SHA256:

`D55B610B6E2FFB1B032137F30C348FEFE9EF3542321720090C6690885D749E41`

Repeat-hash verification: **TRUE**.

No build, test or compiler commands were used. No P2 task-solving model was invoked and P2 experimental runs remain **0**.

## Programme consequence

The previously accepted five-task Level-2 design is no longer execution-authoritative. Item 58 must be reopened for a transparent design repair. The sample must not be forced back to five tasks and the historical 30-run total must not be preserved post hoc merely for convenience.
