"""Deterministic canonicalisation helpers for RaS research artefacts."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_text_bytes(text: str) -> bytes:
    """Return UTF-8 text with LF endings, stripped line tails and one final LF."""
    if not isinstance(text, str):
        raise TypeError("text must be str")
    normalised = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in normalised.strip("\n").split("\n")]
    return ("\n".join(lines) + "\n").encode("utf-8")


def canonical_json_bytes(value: Any) -> bytes:
    """Return deterministic compact UTF-8 JSON bytes."""
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    if not isinstance(data, (bytes, bytearray, memoryview)):
        raise TypeError("data must be bytes-like")
    return hashlib.sha256(bytes(data)).hexdigest()


def sha256_canonical_text(text: str) -> str:
    return sha256_hex(canonical_text_bytes(text))


def sha256_canonical_json(value: Any) -> str:
    return sha256_hex(canonical_json_bytes(value))
