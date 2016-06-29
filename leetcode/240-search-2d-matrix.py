class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0
        j = len(matrix[0]) - 1
        while True:
            try:
                n = matrix[i][j]
            except IndexError:
                return False
            if n == target:
                return True
            if n > target:
                j -= 1
            if n < target:
                i += 1
        return False
