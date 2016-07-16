def legal_move(board, (i, j)):
    return not any(
        oi == i or oj == j or abs(i - oi) == abs(j - oj)
        for oi, oj in board
    )


class Solution(object):
    def solveNQueens(self, n):
        def place(board, m):
            if m == n:
                return 1
            return sum(
                place(board.union({(m, i)}), m + 1)
                for i in range(n)
                if legal_move(board, (m, i))
            )

        return place(set(), 0)


if __name__ == '__main__':
    s = Solution()
    assert s.solveNQueens(4) == 2
