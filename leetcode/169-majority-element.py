class Solution:
    def majorityElement(self, nums):
        return sorted(nums)[len(nums)/2]
