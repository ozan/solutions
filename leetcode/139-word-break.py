class Solution(object):

    def wordBreak(self, s, wordDict):
        memo = {}

        def can_break(s):
            if not s:
                return True
            if s in memo:
                return memo[s]
            res = any(
                can_break(s[i:])
                for i in range(len(s), 0, -1)
                if s[:i] in wordDict
            )
            memo[s] = res
            return res

        return can_break(s)


if __name__ == '__main__':
    s = Solution()
    assert s.wordBreak('leetcode', {'leet', 'code'}) is True
