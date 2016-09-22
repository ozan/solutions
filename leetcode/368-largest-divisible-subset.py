class Solution(object):
    def largestDivisibleSubset(self, nums):
        # map k: v where v is the largest subset for which k is a divisor
        S = {1: []}
        for n in sorted(nums):
            S[n] = [n] + max((S[d] for d in S if n % d == 0), key=len)
        return max(S.values(), key=len)
