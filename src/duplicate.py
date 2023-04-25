'''
Given an integer array nums, return true if any value appears at
least twice in the array, and return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/
'''


def containsDuplicate(nums: list[int]) -> bool:
    set_of_numbers = set(nums)
    boolean = False
    if len(list(set_of_numbers)) < len(nums):
        boolean = True
    return boolean
