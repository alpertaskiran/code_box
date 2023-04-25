'''
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.You may assume that
each input would have exactly one solution, and you may not use the same
element twice.You can return the answer in any order.
https://leetcode.com/problems/two-sum/
'''


def twoSum(nums: list[int], target: int) -> list[int]:
    for indice, number in enumerate(nums):
        for indice_, number_ in enumerate(nums):
            if indice is indice_ or indice_ < indice:
                continue

            if number + number_ == target:
                return [indice, indice_]
    return []
