class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        try:
            prior, subsequent = 0, nums[0]
        except IndexError:
            return 0

        for num in nums[1:]:
            prior, subsequent = subsequent, max(subsequent, num + prior)

        return subsequent
