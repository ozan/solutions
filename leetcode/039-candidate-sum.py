"""
Given a set of candidate numbers C and a target number T, find all unique
combinations of members of C that sum to T. All numbers are positive ints.

Plan:

Recursive where f(C, T) is union of c + f(C, T - c) for all c in C.

Memoization should theoretically improve running time but empirically the
overhead is higher than the benefit on the leetcode data.

"""


def combination_sum(candidates, target):
    solns = []
    for i, c in enumerate(candidates):
        if c > target:
            break
        if c == target:
            solns.append([c])
            break
        sub_solns = combination_sum(candidates[i:], target - c)
        solns += [[c] + sub_s for sub_s in sub_solns]
    return solns


class Solution(object):
    def combinationSum(self, candidates, target):
        return combination_sum(tuple(sorted(candidates)), target)


if __name__ == '__main__':
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
