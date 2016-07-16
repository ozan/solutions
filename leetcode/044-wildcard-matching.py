"""
TODO: this fails with TLE on very large strings, probably need DP approach
"""


def memoize(f):
    memo = {}

    def inner(*args):
        if args in memo:
            return memo[args]
        res = f(*args)
        memo[args] = res
        return res
    return inner


@memoize
def matches(s, p):
    if p == '':
        return s == ''

    if s == '':
        return p == '' or p[0] == '*' and matches(s, p[1:])

    # try to short circuit
    if len([ch for ch in p if ch != '*']) > len(s):
        return False

    if p[0] == '?':
        return matches(s[1:], p[1:])

    if p[-1] == '?':
        return matches(s[:-1], p[:-1])

    if p[0] != '*':
        return p[0] == s[0] and matches(s[1:], p[1:])

    if p[-1] != '*':
        return p[-1] == s[-1] and matches(s[:-1], p[:-1])

    return any(
        matches(s[i:], p[1:])
        for i in range(len(s), -1, -1)
    )


class Solution(object):
    def isMatch(self, s, p):
        return matches(s, p)


if __name__ == '__main__':
    s = Solution()
    assert s.isMatch("aa", "a") is False
    assert s.isMatch("aa", "aa") is True
    assert s.isMatch("aaa", "aa") is False
    assert s.isMatch("aa", "*") is True
    assert s.isMatch("aa", "a*") is True
    assert s.isMatch("ab", "?*") is True
    assert s.isMatch("aab", "c*a*b") is False
    assert s.isMatch("", "*") is True
    assert s.isMatch("c", "*?*") is True

    st = "ababaabaabbbbbabbbaaababbaabbbbbaaabaabababaaaabbabbbbabbaaaaaaaaabaababbaabaaababaababaabbabbbbbabababbabaabbbaababbbababaaabbbbbbbbbabaababaaabababbbbabbaabaaabbbababbbbbbbbabaaaabbabbbbabbaaabbbbababab"
    p = "ab**bbb*a*ab*bb*aa*a***ab*b**b***bba****b*aaabaa**bb*ab*a***abb****bb*a**b*****a*abaa**a****aab**aa**bbb"
    assert s.isMatch(st, p) is False
