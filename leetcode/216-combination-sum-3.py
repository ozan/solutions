"""
Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a
unique set of numbers.
"""


def combination_sum(k, n, digits):
    if k == 0:
        return [[]] if n == 0 else []

    solns = []
    for i, d in enumerate(digits):
        if d > n:
            break
        sub_solns = combination_sum(k - 1, n - d, digits[(i+1):])
        solns += [[d] + sub_s for sub_s in sub_solns]
    return solns


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return combination_sum(k, n, range(1, 10))

if __name__ == '__main__':
    s = Solution()
    assert s.combinationSum3(3, 7) == [[1, 2, 4]]
    assert s.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
