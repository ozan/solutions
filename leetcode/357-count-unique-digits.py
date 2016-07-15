

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        tot = 1
        prod = 1
        for k in range(1, n + 1):
            prod *= min(9, 11 - k)
            tot += prod
        return tot


if __name__ == '__main__':
    f = Solution().countNumbersWithUniqueDigits
    assert f(0) == 1
    assert f(1) == 10
    assert f(2) == 91
