import pytest

from roman_integer import romanToInt


@pytest.mark.parametrize('test_input,expected', [('III', 3),
                                                 ('LVIII', 58),
                                                 ('MCMXCIV', 1994)])
def test_eval(test_input, expected):
    assert romanToInt(test_input) == expected
