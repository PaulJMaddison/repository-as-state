# Resource and economic model — hostile-audit revision

The original additive conceptual cost model risked double counting because reasoning, context and agent-state costs can overlap in actual provider billing and inference.

P0 should therefore report an **observable resource vector**, not infer provider-internal cost:

    Z_c = (
      input_tokens,
      output_tokens,
      model_calls,
      tool_calls,
      repository_bytes_read,
      files_read,
      reconstruction_time,
      total_time,
      retries,
      provider_billed_cost_if_exposed
    )

for condition c.

## Observability classes

### OBSERVABLE
- input/output tokens exposed by the interface;
- model/tool calls;
- files and repository bytes read;
- searches;
- elapsed time;
- retries;
- provider-billed charges when explicitly exposed.

### PARTIALLY OBSERVABLE
- cached/uncached token counters;
- prompt-cache hits;
- session-persistence indicators;
- opaque provider usage categories.

Report the interface/version and limitations.

### UNOBSERVABLE
- exact provider GPU allocation;
- exact KV-cache residency cost;
- internal storage/scheduler amortisation;
- hidden cache implementation;
- provider profit margin.

Do not call these measured savings.

## Reconstruction Token Fraction

    RTF = reconstruction_input_tokens / total_RaS_input_tokens.

RTF is descriptive only. Report numerator, denominator, total resource vector, failures and retries.

## Economic falsifier

The resource/economic thesis fails if reconstruction, retry and execution burden erases any advantage from removing predecessor history.

Subscription price is not evidence of provider-internal inference cost.
