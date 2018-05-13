"""
Strategy: Perform two DFSs, one from Pacific and other from Atlantic, to determine from which coords each can be reached. Then the intersection of these sets is the result.
"""


def dfs(matrix, visited):
    """
    Perform a DFS where edges exist where water can flow upwards; update visited.
    """
    queue = list(visited)
    while queue:
        x, y = queue.pop()
        adjacent = [(x+dx, y+dy) for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1))
                    if 0 <= x+dx < len(matrix) and 0 <= y+dy < len(matrix[0])
                    and (x+dx, y+dy) not in visited
                    and matrix[x+dx][y+dy] >= matrix[x][y]]
        queue.extend(adjacent)
        visited.update(adjacent)


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        pacific = {(0, i) for i in range(n)}  # top
        pacific.update((i, 0) for i in range(1, m))  # left
        atlantic = {(m-1, i) for i in range(n)}  # bottom
        atlantic.update((i, n-1) for i in range(0, m-1))  # right
        dfs(matrix, pacific)
        dfs(matrix, atlantic)
        return [list(coord) for coord in atlantic.intersection(pacific)]

