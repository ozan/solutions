"""
Given n, return all solutions to the n-queens problem

Strategy: use backtracking search to fill in an n-row list containing
numbers [0, n) uniquely, where there is also no diagonal attack.
"""

class Solution(object):
    def solveNQueens(self, n):
        solutions, board = [], []
        
        def dfs(cols):
            if len(board) == n: return solutions.append(self.format(board))
            for i, c in enumerate(cols):
                for j, d in enumerate(board):
                    if abs(c - d) == abs(j - len(board)):  # same diagonal
                        break
                else:
                    board.append(c)
                    dfs(cols[:i] + cols[i+1:])
                    board.pop()
        
        dfs(range(n))
        return solutions

    def format(self, board):
        return [''.join('Q' if i == j else '.' for j in board) for i in range(len(board))]


if __name__ == '__main__':
    s = Solution()
    expected = [
        ['..Q.', 'Q...', '...Q', '.Q..']
        ['.Q..', '...Q', 'Q...', '..Q.'],
    ]
    print s.solveNQueens(4)
    assert s.solveNQueens(4) == expected
    print 'ok'
