import pytest

from binary_search import search


@pytest.mark.parametrize('test_input,target,expected', [([-1, 0, 3, 5, 9, 12], 9, 4),
                                                        ([-1, 0, 3, 5, 9, 12], 2, -1)])
def test_eval(test_input, target, expected):
    assert search(test_input, target) == expected
