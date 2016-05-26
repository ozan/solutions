"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution.
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        indices = {}
        for i, n in enumerate(nums):
            try:
                return (indices[target - n], i)
            except KeyError:
                indices[n] = i
        return None


assert Solution().twoSum([2, 7, 11, 15], 9) == (0, 1)
