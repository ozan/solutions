def linear_sum(seq):
    p, pp = 0, 0
    for n in seq:
        p, pp = max(n + pp, p), p

    return p


class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(linear_sum(nums[:-1]), linear_sum(nums[1:]))
