class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        values = [[(el + 1) % 2 for el in row] for row in obstacleGrid]
        for i, row in enumerate(values):
            for j, current_val in enumerate(row):
                if current_val == 0:
                    continue
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    the_value = values[0][j-1]
                elif j == 0:
                    the_value = values[i-1][0]
                else:
                    the_value = values[i-1][j] + values[i][j-1]
                values[i][j] = the_value
        return values[-1][-1]
