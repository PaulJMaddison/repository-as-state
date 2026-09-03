# Subject-B protocol-version audit

The durable chronology supports the conclusion that the original narrow protocol governed the original corpus result. The initial P0 verifier contract was committed at `487eca9…` before the candidate verifier freezes and narrow adjudications. It required frozen, implementation-independent behavioural verification, PRE failure/POST pass, and behavioural negative controls, but did not require every broader hidden requirement to be separately evaluated.

The original narrow evidence remains intact for WP04, WP05 and WP06: task and requirement hashes match, verifier freezes and PRE/POST/negative-control results are present, and the recorded aggregate is four PRE-fail/POST-pass candidates with four detected negative controls and a three-task sequential chain.

The comprehensive requirement-level coverage gate was introduced later, after the narrow adjudication and corpus-feasibility result. Its subsequent WP04 failure therefore represents a later robustness/protocol amendment and does not invalidate the original narrow proof or claim that the original protocol was non-compliant.

This audit did not rebuild, test, probe, search boundaries, create verifier versions, run agents, execute P0, or create the final lock.

Next step: `HUMAN_APPROVE_PROTOCOL_V1_FOR_FINAL_LOCK`.
