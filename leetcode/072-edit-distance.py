
class Solution(object):
    def minDistance(self, x, y):
        """
        Fisher and Wagner dynamic programming approach:
        O(mn) time, O(n) space
        """
        memo = range(0, len(y) + 1)
        for i, cx in enumerate(x):
            new_memo = [i + 1]
            for j, cy in enumerate(y):
                new_memo.append(min(
                    1 + memo[j + 1],
                    1 + new_memo[j],
                    (cx != cy) + memo[j]
                ))
            memo = new_memo
        return memo[-1]


cases = (
    ('a', 'ab', 1),
    ('ab', 'a', 1),
    ('ab', 'cb', 1),
    ('avery', 'garvey', 3)
)

if __name__ == '__main__':
    f = Solution().minDistance
    for x, y, n in cases:
        result = f(x, y)
        if result != n:
            print('Expected f({}, {}) to be {}, was {}'
                  .format(x, y, n, result))
    print 'ok'
