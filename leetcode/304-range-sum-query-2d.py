def make_cache(matrix):
    cache = []
    for i, row in enumerate(matrix):
        cache_row = [row[0]]
        for j, item in enumerate(row):
            if j == 0:
                continue
            cache_row.append(item + cache_row[j - 1])
        if not cache:
            cache.append(cache_row)
            continue
        cache.append([a + b for a, b in zip(cache_row, cache[-1])])
    return cache


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.cache = make_cache(matrix)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        val = self.cache[row2][col2]
        if row1 > 0:
            val -= self.cache[row1 - 1][col2]
        if col1 > 0:
            val -= self.cache[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            val += self.cache[row1 - 1][col1 - 1]
        return val


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
