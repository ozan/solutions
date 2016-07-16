def legal_move(board, (i, j)):
    return not any(
        oi == i or oj == j or abs(i - oi) == abs(j - oj)
        for oi, oj in board
    )


def formatted(board, n):
    llchar = [['.'] * n for _ in range(n)]
    for i, j in board:
        llchar[i][j] = 'Q'
    return [''.join(row) for row in llchar]


class Solution(object):
    def solveNQueens(self, n):
        def place(board, m):
            if m == n:
                return [board]
            return [
                tail.union({(m, i)})
                for i in range(n)
                if legal_move(board, (m, i))
                for tail in place(board.union({(m, i)}), m + 1)
            ]

        return [formatted(b, n) for b in place(set(), 0)]


if __name__ == '__main__':
    s = Solution()
    expected = [
        ['.Q..', '...Q', 'Q...', '..Q.'],
        ['..Q.', 'Q...', '...Q', '.Q..']
    ]
    assert s.solveNQueens(4) == expected
    print 'ok'
