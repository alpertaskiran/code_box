import pytest

from max_sub_array import maxSubArray


@pytest.mark.parametrize('test_input,expected', [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
                                                 ([1], 1),
                                                 ([5, 4, -1, 7, 8], 23)])
def test_eval(test_input, expected):
    assert maxSubArray(test_input) == expected
