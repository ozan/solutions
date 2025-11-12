import io
from collections import defaultdict


def is_bipartite(g):
    """
    DFS the entire graph.

    A previously unvisited vertex should be colored True
    Any vertex connected to True should be colored False, and vice versa
    Graph is not bipartite if False is ever connected to False, or True to True
    """
    colors = {}  # True or False

    def dfs(v, c):
        colors[v] = c

        for nxt in g[v]:
            if nxt == v:
                continue
            if nxt not in colors:
                if not dfs(nxt, not c):
                    return False  # propagate miscoloring in recursive DFS
            elif colors[nxt] == colors[v]:
                return False
        return True

    for v in g:
        if v not in colors:
            if not dfs(v, True):
                return False

    return True


def bip(f):
    n = int(f.readline())
    res = []
    for _ in range(n):
        f.readline()  # blank
        nv, ne = map(int, f.readline().split(' '))
        g = defaultdict(list)
        for _ in range(ne):
            a, b = map(int, f.readline().split(' '))
            g[a].append(b)
            g[b].append(a)
        res.append('1' if is_bipartite(g) else '-1')

    print(' '.join(res))


sample = io.StringIO("""2

3 3
1 2
3 2
3 1

4 3
1 4
3 1
1 2""")

bip(sample)
with open('/Users/oz/Downloads/rosalind_bip.txt') as f:
    bip(f)
