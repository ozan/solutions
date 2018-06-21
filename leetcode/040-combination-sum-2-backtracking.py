"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Strategy: backtracking. Do not traverse down paths that have exceeded target.
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        results, seen = [], set()
        candidates.sort()

        def dfs(target, candidates, parts=tuple()):
            if target < 0: return

            if target == 0 and parts not in seen:
                seen.add(parts) 
                return results.append(parts)

            for i, c in enumerate(candidates):
                dfs(target - c, candidates[i+1:], parts + (c,))

        dfs(target, candidates)
        return results


if __name__ == '__main__':
    expected = {
        (1, 7),
        (1, 2, 5),
        (2, 6),
        (1, 1, 6)
    }
    actual = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    assert set(tuple(l) for l in actual) == expected
    assert Solution().combinationSum2([2, 5, 2, 1, 2], 5) == [(1, 2, 2), (5,)]
    print('OK')
