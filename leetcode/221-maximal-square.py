class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        height, width = len(matrix), len(matrix[0])

        cache = [
            [int(matrix[i][j]) for j in xrange(width)]
            for i in xrange(height)
        ]

        for i in xrange(1, height):
            for j in xrange(1, width):
                if matrix[i][j] == '1':
                    cache[i][j] = min(cache[i-1][j],
                                      cache[i][j-1],
                                      cache[i-1][j-1]) + 1
                else:
                    cache[i][j] = 0

        ans = max([max(i) for i in cache])
        return ans ** 2
