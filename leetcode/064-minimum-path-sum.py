class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        last = 0
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                prior = []
                if i > 0:
                    prior.append(grid[i - 1][j])
                if j > 0:
                    prior.append(grid[i][j - 1])
                grid[i][j] = last = el + min(prior or [0])
        return last
