deltas = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        elif board[x][y] == 'E':                
            adj = [[x+dx, y+dy] for dx, dy in deltas
                   if 0 <= x+dx < len(board) and 0 <= y+dy < len(board[0])]
            num_mines = len([True for xx, yy in adj if board[xx][yy] == 'M'])
            if num_mines == 0:
                board[x][y] = 'B'
                for reclick in adj:
                    self.updateBoard(board, reclick)
            else:
                board[x][y] = str(num_mines)
        
        return board