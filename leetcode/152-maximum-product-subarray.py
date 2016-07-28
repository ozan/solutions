class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        running_max, running_min, best_product = [nums[0]] * 3
        for n in nums[1:]:
            possibilities = (n, n * running_max, n * running_min)
            running_max, running_min = max(*possibilities), min(*possibilities)
            best_product = max(running_max, best_product)
        return best_product
