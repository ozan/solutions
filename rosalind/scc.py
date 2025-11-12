import io


def scc(f):
    n_verts, n_edges = map(int, f.readline().split(' '))
    g = {i+1: [] for i in range(n_verts)}
    rev = {i+1: [] for i in range(n_verts)}

    for _ in range(n_edges):
        a, b = map(int, f.readline().split(' '))
        g[a].append(b)
        rev[b].append(a)

    finished = []
    visited = set()

    # pass 1: dfs original graph tracking finishing times
    def dfs_g(v):
        if v in visited:
            return
        visited.add(v)

        for nxt in g[v]:
            dfs_g(nxt)

        finished.append(v)

    for v in range(1, n_verts + 1):
        dfs_g(v)

    # pass 2: dfs inverse graph in reverse order of finish time
    visited = set()

    def dfs_rev(v):
        if v in visited:
            return
        visited.add(v)

        for nxt in rev[v]:
            dfs_rev(nxt)

    count = 0
    while finished:
        v = finished.pop()
        if v not in visited:
            count += 1
            dfs_rev(v)

    print(count)


sample = io.StringIO("""6 7
4 1
1 2
2 4
5 6
3 2
5 3
3 5""")

# scc(sample)

with open('/Users/oz/Downloads/rosalind_scc.txt') as f: scc(f)
