import io


def general_source(g):
    """
    Return a node from which all others can be reached, if any
    """
    visited = set()

    def dfs(v):
        visited.add(v)
        if len(visited) == len(g):
            return True
        for nxt in g[v]:
            if nxt in visited:
                continue
            if dfs(nxt):
                return True
        visited.remove(v)

    for v in g:
        print(v)
        if dfs(v):
            return v

    return False


def gs(f):
    n = int(f.readline())
    res = []
    for _ in range(n):
        f.readline()  # blank
        n_verts, n_edges = map(int, f.readline().split(' '))
        g = {i: [] for i in range(1, n_verts+1)}
        for _ in range(n_edges):
            a, b = map(int, f.readline().split(' '))
            g[a].append(b)
        print('---')
        res.append(general_source(g))
    
    print('===')
    return ' '.join(str(r) if r else '-1' for r in res)


sample = io.StringIO("""2

3 2
3 2
2 1

3 2
3 2
1 2""")

assert gs(sample) == '3 -1'

with open('/Users/oz/Downloads/rosalind_gs.txt') as f: print(gs(f))
