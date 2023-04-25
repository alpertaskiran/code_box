import pytest

from arrow_shots import findMinArrowShots


@pytest.mark.parametrize('test_input,expected', [(
    [[9, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2
     )])
def test_eval(test_input, expected):
    assert findMinArrowShots(test_input) == expected
