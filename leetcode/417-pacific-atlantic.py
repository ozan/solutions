"""
Strategy: Perform two BFSs, one from Pacific and other from Atlantic, to determine from which coords each can be reached. Then the intersection of these sets is the result.
"""

deltas = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
                
        def bfs(visited):
            level = visited
            while level:
                level = {(x+dx, y+dy) for x, y in level for dx, dy in deltas
                         if (x+dx, y+dy) not in visited and 0 <= x+dx < m and 0 <= y+dy < n
                         and matrix[x+dx][y+dy] >= matrix[x][y]}
                visited |= level
        
        pacific = {(0, i) for i in xrange(n)}  # top
        pacific.update((i, 0) for i in xrange(1, m))  # left
        atlantic = {(m-1, i) for i in xrange(n)}  # bottom
        atlantic.update((i, n-1) for i in xrange(0, m-1))  # right
        bfs(pacific)
        bfs(atlantic)
        return [list(x) for x in atlantic & pacific]

