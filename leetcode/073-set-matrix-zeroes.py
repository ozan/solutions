class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        sentinel = {}

        def set_rowcol_vals(i, j):
            for ii in range(len(matrix)):
                if matrix[ii][j] != 0:
                    matrix[ii][j] = sentinel
            for jj in range(len(matrix[i])):
                if matrix[i][jj] != 0:
                    matrix[i][jj] = sentinel

        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == 0:
                    set_rowcol_vals(i, j)

        for row in matrix:
            for j, x in enumerate(row):
                if x == sentinel:
                    row[j] = 0
