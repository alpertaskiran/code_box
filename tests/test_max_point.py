import pytest

from max_point import maxPoints


@pytest.mark.parametrize('test_input,expected', [
    ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 6),
    ([[1, 1], [2, 2], [3, 3]], 3)])
def test_eval(test_input, expected):
    assert maxPoints(test_input) == expected
