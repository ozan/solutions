"""
Given a set of candidate numbers C and a target number T, find all unique
combinations of members of C that sum to T. All numbers are positive ints.

Plan: backtracking search (do not search beyond exceeded target)
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        results, parts = [], []

        def dfs(total=0, i=0):
            if total == target: return results.append(parts[:])
            if total > target: return
            for j in range(i, len(candidates)):
                parts.append(candidates[j])
                dfs(total + candidates[j], j)
                parts.pop()
        
        dfs()
        return results


if __name__ == '__main__':
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]

