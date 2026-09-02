# Approximate repository sufficiency

Let:

- H_t be complete historical engineering interaction;
- R_t be durable repository state;
- U be the next task;
- A_(t+1) be a useful next engineering action.

An ideal repository would satisfy:

    P(A_(t+1) | H_t, U) = P(A_(t+1) | R_t, U).

Exact equality is unrealistic. Conceptually, epsilon-repository sufficiency may be expressed as:

    D_KL(
      P(A | H_t, U)
      ||
      P(A | R_t, U)
    ) <= epsilon.

Literal KL divergence over useful engineering actions is unlikely to be directly observable. RaS therefore operationalises sufficiency using engineering success, hidden behavioural verification, resumption success, reconstruction accuracy, regression rate and state-reconstruction cost.

The important object is not lossless conversational memory. It is preservation of the information necessary for future correct action.
