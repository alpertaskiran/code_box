import pytest

from max_ice_cream import maxIceCream


@pytest.mark.parametrize('test_input,target,expected', [([1, 3, 2, 4, 1], 7, 4),
                                                        ([10, 6, 8, 7, 7, 8], 5, 0),
                                                        ([1, 6, 3, 1, 2, 5], 20, 6)])
def test_eval(test_input, target, expected):
    assert maxIceCream(test_input, target) == expected
