import pytest

from ras.metrics import reconstruction_token_fraction, repository_resumability_index


@pytest.mark.parametrize(
    ("successes", "resets", "expected"),
    [(0, 1, 0.0), (1, 1, 1.0), (1, 2, 0.5), (9, 10, 0.9)],
)
def test_repository_resumability_index(successes, resets, expected):
    assert repository_resumability_index(successes, resets) == expected


@pytest.mark.parametrize("successes,resets", [(-1, 1), (1, -1), (2, 1), (0, 0)])
def test_repository_resumability_index_rejects_invalid_counts(successes, resets):
    with pytest.raises(ValueError):
        repository_resumability_index(successes, resets)


@pytest.mark.parametrize(
    ("reconstruction", "total", "expected"),
    [(0, 1, 0.0), (1, 1, 1.0), (25, 100, 0.25)],
)
def test_reconstruction_token_fraction(reconstruction, total, expected):
    assert reconstruction_token_fraction(reconstruction, total) == expected


@pytest.mark.parametrize("reconstruction,total", [(-1, 1), (1, -1), (2, 1), (0, 0)])
def test_reconstruction_token_fraction_rejects_invalid_counts(reconstruction, total):
    with pytest.raises(ValueError):
        reconstruction_token_fraction(reconstruction, total)
