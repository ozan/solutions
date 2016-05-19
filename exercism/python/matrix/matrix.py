

class Matrix(object):
    def __init__(self, M):
        self.rows = [[int(x) for x in xs.split()] for xs in M.splitlines()]
        self.columns = [list(col) for col in zip(*self.rows)]
