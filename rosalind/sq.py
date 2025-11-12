import io


def has_cycle_length(n, g):
    """
    Determine if given graph has a simple cycle of length n or greater
    """

    visited = {}

    def dfs(v):
        visited[v] = len(visited)
        for nxt in g[v]:
            if nxt in visited:
                if len(visited) - visited[nxt] == n:
                    return True
                continue
            if dfs(nxt):
                return True
        del visited[v]  # backtrack
        return False

    for v in g:
        if dfs(v): return True
    return False


def sq(f):
    n = int(f.readline())
    res = []

    for _ in range(n):
        f.readline()  # blank
        n_verts, n_edges = map(int, f.readline().split(' '))
        g = {str(i): [] for i in range(1, n_verts+1)}
        for _ in range(n_edges):
            a, b = f.readline().rstrip().split(' ')
            g[a].append(b)
            g[b].append(a)
        res.append(has_cycle_length(4, g))

    return ' '.join('1' if r else '-1' for r in res)


sample = io.StringIO("""2

4 5
3 4
4 2
3 2
3 1
1 2

4 4
1 2
3 4
2 4
4 1""")

assert sq(sample) == '1 -1'

with open('/Users/oz/Downloads/rosalind_sq.txt') as f: print(sq(f))
