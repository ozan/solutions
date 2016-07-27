"""
Given a string, find the length of the longest substring without repeating
characters.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        seen = {}
        the_max = 0
        j = 0
        for i, ch in enumerate(s):
            if ch in seen:
                j = max(j, seen[ch] + 1)
            seen[ch] = i
            the_max = max(the_max, i - j + 1)
        return the_max


if __name__ == '__main__':
    f = Solution().lengthOfLongestSubstring
    assert f('abcabcbb') == 3
    assert f('bbbbb') == 1
    assert f('pwwkew') == 3
