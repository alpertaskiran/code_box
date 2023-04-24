'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
https://leetcode.com/problems/maximum-subarray/
'''


def maxSubArray(nums: list[int]) -> int:
    best_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        best_sum = max(best_sum, current_sum)

    return best_sum
