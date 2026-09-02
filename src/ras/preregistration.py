"""Validation helpers for public P0 preregistration artefacts."""

from __future__ import annotations

from typing import Any

from .canonical import sha256_canonical_json


_REQUIRED_TOP_LEVEL = {
    "experiment",
    "research_question",
    "audit_base_sha",
    "subject",
    "corpus",
    "conditions",
    "endpoints",
    "leakage",
    "workspace",
    "run_control",
    "interpretation",
    "falsification",
    "public_private_boundary",
    "model_runtime",
    "results",
}


def validate_public_preregistration(value: dict[str, Any]) -> tuple[str, ...]:
    failures: list[str] = []
    missing = sorted(_REQUIRED_TOP_LEVEL - set(value))
    if missing:
        failures.append("missing_top_level:" + ",".join(missing))
    if value.get("experiment", {}).get("id") != "P0":
        failures.append("experiment_id_must_be_P0")
    if value.get("subject", {}).get("identifier") != "PRIVATE_SUBJECT_A":
        failures.append("public_subject_must_be_pseudonymous")
    if value.get("results", {}).get("experimental_agent_runs") != 0:
        failures.append("experimental_agent_runs_must_be_zero_before_P0")
    if value.get("results", {}).get("positive_empirical_ras_results") is not False:
        failures.append("positive_empirical_ras_results_must_be_false_before_P0")
    if value.get("conditions", {}).get("D", {}).get("enabled_for_p0") is not False:
        failures.append("tiered_execution_must_be_disabled_for_primary_P0")
    if value.get("corpus", {}).get("task_count") not in range(1, 11):
        failures.append("task_count_out_of_pilot_range")
    hashes = value.get("corpus", {}).get("task_spec_sha256", {})
    if not isinstance(hashes, dict) or len(hashes) != value.get("corpus", {}).get("task_count"):
        failures.append("task_hash_count_mismatch")
    return tuple(sorted(failures))


def preregistration_digest(value: dict[str, Any]) -> str:
    failures = validate_public_preregistration(value)
    if failures:
        raise ValueError("; ".join(failures))
    return sha256_canonical_json(value)
