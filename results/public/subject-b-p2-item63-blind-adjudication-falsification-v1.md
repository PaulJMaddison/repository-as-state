# Subject B P2 — Item 63 blind-adjudication falsification

Item 63 remains active. The accepted Item-62 experiment and its 24 frozen candidates are unchanged.

The first Item-63 Stage-A attempt was invalidated by a verifier-path mistake. The worker made 24 calls against coordinator-side placeholder entrypoints rather than the sealed qualified verifier package. Those calls produced no correctness adjudication output and are not accepted as blinded adjudications.

The worker then unblinded the mapping before discovering the path mismatch and made one diagnostic call to the real sealed verifier. Because that diagnostic call occurred after condition information was available, it is quarantined and is not accepted as a blinded Stage-A adjudication.

No P2 candidate was rerun or modified. No task-solving model was invoked. P0 and P1 were not rerun.

The recovery is to preserve the failed Item-63 evidence, create a neutral blind-ID-only candidate bundle, and execute the unchanged sealed verifier through a scoring process that cannot access condition labels or the blind-to-condition mapping. All 24 accepted blinded adjudications must be frozen before the permitted unblinding and matched analysis.

Item 63 is not complete and Item 64 may not start.
