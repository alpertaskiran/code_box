'''
Given an array of points where points[i] = [xi, yi]
represents a point on the X-Y plane, return the maximum
number of points that lie on the same straight line.
https://leetcode.com/problems/max-points-on-a-line/
'''
from itertools import combinations


def maxPoints(points: list[list[int]]) -> int:
    size_numbers = len(points)
    if size_numbers == 1:
        return 1
    elif size_numbers == 2:
        return 2
    else:
        maximum_points = 0
        for i in list(combinations(points, 2)):
            count = 0
            for j in points:
                if condition_check(i, j):
                    count += 1
            maximum_points = max(maximum_points, count)
        return maximum_points


def condition_check(i, j):
    first_part = (j[1] - i[0][1]) * (i[1][0] - i[0][0])
    second_part = (j[1] - i[0][1]) * (i[1][0] - i[0][0])
    return first_part == second_part
