# This is just fibonacci, so use Binet's formula


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        n += 1
        numerator = (1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n
        denominator = 2 ** n * 5 ** 0.5
        return int(numerator / denominator)
