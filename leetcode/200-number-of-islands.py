WATER = '0'
LAND = '1'
POSITION_DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == LAND:
                grid[i][j] = WATER
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
