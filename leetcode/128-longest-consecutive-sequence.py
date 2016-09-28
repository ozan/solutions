class DisjointSet(dict):
    def rep(self, k):
        parent, cnt = self[k]
        if parent == k:
            return parent, cnt
        return self.rep(parent)

    def combine(self, subset, target):
        t_rep, t_count = self.rep(target)
        s_rep, s_count = self.rep(subset)
        self[s_rep] = (t_rep, None)
        self[t_rep] = (t_rep, s_count + t_count)
        return s_count + t_count


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        djs = DisjointSet()
        largest = 0

        for n in nums:
            if n in djs:
                # handled n already, so skip
                continue

            djs[n] = (n, 1)
            candidate = 1

            if n + 1 in djs:
                candidate = djs.combine(n, n + 1)

            if n - 1 in djs:
                candidate = djs.combine(n, n - 1)

            largest = max(largest, candidate)

        return largest


if __name__ == '__main__':
    f = Solution().longestConsecutive
    assert f([100, 4, 200, 1, 3, 2]) == 4
    assert f([]) == 0
    assert f([1]) == 1
    assert f([1, 1]) == 1
    assert f([1, 3]) == 1
    assert f([1, 2]) == 2
    assert f([4, 1, 2, 3]) == 4
