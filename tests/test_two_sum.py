import pytest

from two_sum import twoSum


@pytest.mark.parametrize('test_input,target,expected', [([2, 7, 11, 15], 9, [0, 1]),
                                                        ([3, 2, 4], 6, [1, 2]),
                                                        ([3, 3], 6, [0, 1])])
def test_eval(test_input, target, expected):
    assert twoSum(test_input, target) == expected
