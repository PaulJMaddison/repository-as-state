# Repository Resumability Index (RRI)

RRI is a **proposed** research metric:

    RRI =
      successful correct continuations after complete agent-state reset
      ---------------------------------------------------------------
                           eligible forced resets

Conceptually:

    RRI = P(correct continuation | complete conversational-state reset).

RRI may be measured at sequential depth RRI_1, RRI_2, ..., RRI_n to detect degradation as the engineering programme progresses.

A “successful correct continuation” must be defined before the experiment and should require task completion plus hidden behavioural verification or another independent acceptance criterion. Mere compilation, textual similarity, or agent self-report is insufficient.

Ineligible resets, exclusions and human interventions must be pre-registered and reported. RRI is not an established benchmark metric and should not be presented as one.
