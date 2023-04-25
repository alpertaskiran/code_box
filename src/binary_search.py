'''
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists,then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
https://leetcode.com/problems/binary-search/
'''


def search(nums: list[int], target: int) -> int:
    ans = -1
    for index, number in enumerate(nums):
        print(index, number)
        if number == target:
            return index
        if number > target:
            return ans
    return ans
