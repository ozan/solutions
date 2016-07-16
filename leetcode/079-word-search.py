"""
Given a 2D board and a word, find if the word exists in the grid.

TODO: this fails with TLE on really big input
"""


def neighbors(board, i, j):
    return set(
        (i + di, j + dj)
        for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1))
        if 0 <= i + di < len(board)
        if 0 <= j + dj < len(board[i + di])
    )


def does_exist(board, substr, candidates, visited):
    if len(substr) == 1:
        return substr in [board[i][j] for i, j in candidates]

    for i, j in candidates:
        if board[i][j] != substr[0]:
            continue
        has_path = does_exist(
            board,
            substr[1:],
            neighbors(board, i, j) - visited,
            visited.union({(i, j)})
        )
        if has_path:
            return True
    return False


class Solution(object):
    def exist(self, board, word):
        coords = set(
            (i, j)
            for i in range(len(board))
            for j in range(len(board[i]))
        )
        return does_exist(board, word, coords, set())


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    s = Solution()
    assert s.exist(board, 'ABCCED') is True
    assert s.exist(board, 'SEE') is True
    assert s.exist(board, 'ABCB') is False
