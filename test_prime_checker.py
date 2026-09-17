import pytest

from prime_checker import is_prime


@pytest.mark.parametrize(
    "n,expected",
    [
        (-5, False),
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (10, False),
        (100, False),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (17, True),
        (29, True),
        (9, False),
        (15, False),
        (21, False),
        (25, False),
        (27, False),
        (97, True),
        (91, False),
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) is expected
