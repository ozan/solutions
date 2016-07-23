
class Solution(object):
    cache = {0: 0}

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1

        for i in range(max(self.cache.keys()) + 1, n + 1):
            self.cache[i] = 1 + min(self.cache[i - sq]
                                    for sq in squares if sq <= i)

        return self.cache[n]
