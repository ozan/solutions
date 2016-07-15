"""
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.
"""


def valid_byte(s):
    return len(s) == 1 or len(s) > 1 and s[0] != '0' and int(s) < 256


def ip_parts(s, n):
    if n == 1:
        return [[s]] if valid_byte(s) else []
    return [
        [s[:i]] + tail
        for i in (1, 2, 3)
        if valid_byte(s[:i])
        for tail in ip_parts(s[i:], n - 1)
    ]


class Solution(object):
    def restoreIpAddresses(self, s):
        return ['{}.{}.{}.{}'.format(*sol) for sol in ip_parts(s, 4)]


if __name__ == '__main__':
    expected = ["255.255.11.135", "255.255.111.35"]
    assert Solution().restoreIpAddresses("25525511135") == expected
    print 'ok'
