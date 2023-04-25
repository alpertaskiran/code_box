import pytest

from duplicate import containsDuplicate


@pytest.mark.parametrize('test_input,expected', [([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
                                                 ([1, 2, 3, 4], False),
                                                 ([1, 2, 3, 1], True)])
def test_eval(test_input, expected):
    assert containsDuplicate(test_input) == expected
