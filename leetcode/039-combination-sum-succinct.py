"""
Given a set of candidate numbers C and a target number T, find all unique
combinations of members of C that sum to T. All numbers are positive ints.

Plan: backtracking search (do not search beyond exceeded target)

This is a more succinct but slower version of plain backtracking.
"""


class Solution(object):
    def combinationSum(self, candidates, target, res=False):
        if res and target == 0: return [[]]
        return [[c] + sub for i, c in enumerate(candidates) if target - c >= 0
                for sub in self.combinationSum(candidates[i:], target - c, True)]


if __name__ == '__main__':
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


