class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if not any([i for i in nums if i >= 0]):
            return max(nums)
        
        maxSum, current_sum, bounds, starting_index = -float('infinity'), 0, (0, 0), 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum < 0:
                current_sum = 0
                starting_index = i + 1
            if current_sum > maxSum:
                maxSum = current_sum
                bounds = (starting_index, i + 1)
    
        return maxSum
        