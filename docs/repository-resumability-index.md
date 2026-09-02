# Repository Resumability Index (RRI)

RRI is a **proposed descriptive metric**, not a causal estimator and not an established standard:

    RRI =
      verified successful continuations after eligible forced resets
      -------------------------------------------------------------
                         eligible forced resets

An eligible reset requires:
- correct canonical starting state;
- successful reset and contamination gates;
- declared task/model/tool/environment availability;
- no preregistered infrastructure failure before a valid agent test.

A successful continuation requires the frozen behavioural verifier to pass.

Report:
- RRI by task/depth;
- repository/task identifiers;
- uncertainty only when repeated observations justify it;
- infrastructure failures separately;
- **complete-sequence success** for dependent task chains.

Easy tasks can inflate aggregate RRI. RRI also mixes reconstruction and implementation ability. The primary causal evidence is the matched A/B comparison; the reconstruction probe provides mechanism evidence.
