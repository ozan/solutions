class Solution(object):

    def wordBreak(self, s, wordDict):
        memo = {}

        def breaks(s):
            if not s:
                return [[]]

            if s in memo:
                return memo[s]

            res = [
                [s[:i]] + tail
                for i in range(len(s), 0, -1)
                if s[:i] in wordDict
                for tail in breaks(s[i:])
            ]
            memo[s] = res
            return res

        return [' '.join(words) for words in breaks(s)]


if __name__ == '__main__':
    s = Solution()
    d = {'cat', 'cats', 'and', 'sand', 'dog'}
    expected = ['cats and dog', 'cat sand dog']
    assert s.wordBreak('catsanddog', d) == expected
