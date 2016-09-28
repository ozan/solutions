CANDIDATE = NOT_CAPTURED = 'O'
CAPTURED = 'X'
DONT_CAPTURE = 'NO'


class Solution(object):
    def solve(self, board):
        if not any(board):
            return

        h, w = len(board), len(board[0])

        # DFS from every edge square
        stack = \
            [(0, i) for i in range(w)] + \
            [(h-1, i) for i in range(w)] + \
            [(i, 0) for i in range(h)] + \
            [(i, w-1) for i in range(h)]

        while stack:
            i, j = stack.pop()
            if 0 <= i < h and 0 <= j < w and board[i][j] == CANDIDATE:
                board[i][j] = DONT_CAPTURE
                stack += [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]

        for row in board:
            for i, val in enumerate(row):
                row[i] = NOT_CAPTURED if val == DONT_CAPTURE else CAPTURED
