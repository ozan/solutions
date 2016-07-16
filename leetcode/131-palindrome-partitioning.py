"""
Given a string s, partition s such that every substring of the partition is a
palindrome.

Strategy: recursive backtracking given a string, return the cartesian product
of every palindrome prefix with every valid partitioning of the suffix.

"""


def is_palindrome(s):
    for i in range(len(s) / 2):
        if s[i] != s[-(i+1)]:
            return False
    return True


class Solution(object):
    def partition(self, s):
        if len(s) == 0:
            return [[]]
        return [
            [s[:i]] + tail
            for i in range(1, len(s) + 1)
            if is_palindrome(s[:i])
            for tail in self.partition(s[i:])
        ]


if __name__ == '__main__':
    assert is_palindrome('a') is True
    assert is_palindrome('aa') is True
    assert is_palindrome('ab') is False
    assert is_palindrome('aba') is True
    assert is_palindrome('abba') is True
    assert is_palindrome('aaba') is False
    assert Solution().partition('bb') == [['b', 'b'], ['bb']]
    assert Solution().partition('aab') == [['a', 'a', 'b'], ['aa', 'b']]
