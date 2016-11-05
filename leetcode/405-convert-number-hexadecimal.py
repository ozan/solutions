SYMS = '0123456789abcdef'


class Solution(object):
    def toHex(self, num):
        if num < 0:
            num = (1 << 32) + num
        digits = []
        while num > 0:
            digits.append(SYMS[num & 15])
            num >>= 4
        return digits and ''.join(reversed(digits)) or '0'

if __name__ == '__main__':
    f = Solution().toHex
    assert f(26) == "1a"
    assert f(-1) == "ffffffff"
