

class Matrix(object):
    def __init__(self, M):
        self.rows = [[int(x) for x in xs.split(' ')] for xs in M.split('\n')]
        self.columns = list(map(list, zip(*self.rows)))
