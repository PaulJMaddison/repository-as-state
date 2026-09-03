# Subject-B P2 task-selection freeze v1

P2 uses the complete eligible SearchForCars task pool discovered under the accepted deterministic selection rule.

Selection rule: **all eligible candidates in the historical inventory window, ordered by POST date then commit ID**.

- candidates inventoried: 10
- eligible: 5
- excluded under the frozen criteria: 5
- substitutions: 0
- outcome-based exclusions: 0

| P2 task | Historical candidate | PRE | POST | Complexity |
|---|---|---|---|---|
| P2_T01 | C06 | `a120b02abf4dd2bef11ae621d7283282159622f3` | `ddb2d79c65342e8585ef5aefe966e7b2e70b9406` | MEDIUM |
| P2_T02 | C07 | `5941869627443548a9042d900b1a4ffeda58dacb` | `c265580ac53a4e85a164a7f62a5b90f3ecf04cfe` | MEDIUM |
| P2_T03 | C08 | `142a007c64d1c20136742155b672055100128056` | `a740ce1965ba26ab5e06ed5c466430f1e28c5ac5` | LOW |
| P2_T04 | C09 | `c3b813d14973c28ed3bc063c2440224b26dc2a87` | `d7199f391983eb94bb48d8524915245898831a3a` | LOW |
| P2_T05 | C10 | `e9eb063944d604ec0c4cf6b3534f5db87fff82c0` | `a64a727d1ce22dfb851419e46958f08014a48b04` | LOW |

Complexity composition: **3 LOW, 2 MEDIUM, 0 HIGH**.

The absence of a HIGH-complexity eligible task is an explicit limitation. P2 must not be used to claim independent replication of the highest-complexity stratum.

Private binding hashes:

- accepted design-input manifest: `D65E88E8A49114554DBF9C911144BF998172FDD494757AEB6F4491EB9C1F88AF`
- task-selection freeze: `829CD09A84616C5282AFAED1FB4EDA168BE238E344E02EC8AE54A8C11D6ADE94`
- curation package: `5832646A66A37E7F47F124796EEE4E289F72584424E37E2E600970FDC929F6A6`

At this stage no P2 hidden verifier is qualified, P2 is not yet finally preregistered, and P2 experimental-agent runs remain zero.
