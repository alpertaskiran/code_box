'''
https://leetcode.com/problems/roman-to-integer/
'''


def romanToInt(s: str) -> int:

    dictionary_map = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0

    for a in range(len(s) - 1):
        if dictionary_map[s[a]] < dictionary_map[s[a + 1]]:
            sum = sum - dictionary_map[s[a]]
        else:
            sum = sum + dictionary_map[s[a]]

    return sum + dictionary_map[s[-1]]
