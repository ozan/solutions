from collections import defaultdict
import io


sample = """4

2 1
1 2

4 4
4 1
1 2
2 3
3 1

4 3
4 3
3 2
2 1

4 4
1 2
2 3
1 4
4 3
"""


def is_acyclic(edges):
    g = defaultdict(list)
    for a, b in edges:
        g[a].append(b)

    visited = set()  # use for backtracking: add and remove as we descend
    all_explored = set()  # used to avoid re-exploring: never removed

    def dfs(n):

        visited.add(n)

        for nxt in g[n]:
            if nxt in visited:
                return False
            res = dfs(nxt)
            if res is False:
                return False

        visited.remove(n)
        all_explored.add(n)

    starts = list(g.keys())
    for start in starts:
        if start in all_explored:
            continue
        res = dfs(start)
        if res is False:
            return False

    return True


def dag(f):
    n = int(f.readline())  # num graps

    res = []
    for _ in range(n):
        f.readline()  # blank
        num_nodes, num_edges = map(int, f.readline().split(' '))
        edges = []
        for _ in range(num_edges):
            edges.append(map(int, f.readline().split(' ')))
        res.append(is_acyclic(edges))

    print(' '.join('1' if r else '-1' for r in res))


dag(io.StringIO(sample))

with open('/Users/oz/Downloads/rosalind_dag (1).txt') as f: dag(f)
