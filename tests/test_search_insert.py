import pytest

from search_insert import searchInsert


@pytest.mark.parametrize('test_input,target,expected', [([1, 3, 5, 6], 5, 2),
                                                        ([1, 3, 5, 6], 2, 1),
                                                        ([1, 3, 5, 6], 7, 4)])
def test_eval(test_input, target, expected):
    assert searchInsert(test_input, target) == expected
