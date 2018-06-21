
def combination_sum(candidates, target):
    solns = []
    seen = set()
    for i, c in enumerate(candidates):
        if c in seen:
            continue
        seen.add(c)
        if c > target:
            break
        if c == target:
            solns.append([c])
            break
        sub_solns = combination_sum(candidates[(i+1):], target - c)
        solns += [[c] + sub_s for sub_s in sub_solns]
    return solns


class Solution(object):
    def combinationSum2(self, candidates, target):
        return combination_sum(tuple(sorted(candidates)), target)


if __name__ == '__main__':
    expected = {
        (1, 7),
        (1, 2, 5),
        (2, 6),
        (1, 1, 6)
    }
    actual = Solution().combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
    assert set(tuple(l) for l in actual) == expected
