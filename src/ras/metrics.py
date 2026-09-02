"""Pure metric helpers used by RaS experiment analysis.

These functions compute proposed research metrics only. They do not imply
that Repository-as-State has been empirically validated.
"""

from __future__ import annotations


def repository_resumability_index(successful_continuations: int, eligible_resets: int) -> float:
    """Return the proposed Repository Resumability Index (RRI)."""
    if successful_continuations < 0 or eligible_resets < 0:
        raise ValueError("counts must be non-negative")
    if eligible_resets == 0:
        raise ValueError("eligible_resets must be greater than zero")
    if successful_continuations > eligible_resets:
        raise ValueError("successful_continuations cannot exceed eligible_resets")
    return successful_continuations / eligible_resets


def reconstruction_token_fraction(reconstruction_tokens: int, total_ras_input_tokens: int) -> float:
    """Return Reconstruction Token Fraction (RTF)."""
    if reconstruction_tokens < 0 or total_ras_input_tokens < 0:
        raise ValueError("token counts must be non-negative")
    if total_ras_input_tokens == 0:
        raise ValueError("total_ras_input_tokens must be greater than zero")
    if reconstruction_tokens > total_ras_input_tokens:
        raise ValueError("reconstruction_tokens cannot exceed total_ras_input_tokens")
    return reconstruction_tokens / total_ras_input_tokens
