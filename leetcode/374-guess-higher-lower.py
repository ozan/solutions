# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        lower = 1
        higher = n
        while higher > lower:
            candidate = (lower + higher) / 2
            res = guess(candidate)
            if res == 0:
                return candidate
            if res < 0:
                higher = candidate - 1
            else:
                lower = candidate + 1

        return higher
