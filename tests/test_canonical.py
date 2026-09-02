import pytest

from ras.canonical import (
    canonical_json_bytes,
    canonical_text_bytes,
    sha256_canonical_json,
    sha256_canonical_text,
)


def test_text_canonicalisation_normalises_newlines_trailing_space_and_final_lf():
    assert canonical_text_bytes("a  \r\nb\t\r\n\r\n") == b"a\nb\n"


def test_text_hash_is_idempotent_for_equivalent_text():
    first = sha256_canonical_text("a \r\nb\n")
    second = sha256_canonical_text("a\nb\n\n")
    assert first == second


def test_json_canonicalisation_is_deterministic_and_key_sorted():
    left = {"b": [2, 1], "a": {"z": True, "x": None}}
    right = {"a": {"x": None, "z": True}, "b": [2, 1]}
    assert canonical_json_bytes(left) == canonical_json_bytes(right)
    assert sha256_canonical_json(left) == sha256_canonical_json(right)


def test_json_canonicalisation_rejects_nan():
    with pytest.raises(ValueError):
        canonical_json_bytes({"value": float("nan")})


def test_canonical_text_rejects_non_string():
    with pytest.raises(TypeError):
        canonical_text_bytes(b"bytes")  # type: ignore[arg-type]
