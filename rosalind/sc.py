import io


def scc(g, rev):

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

    for v in g:
        dfs_g(v)

    # Pass 2: DFS on the reversed graph in reverse order of finish time
    visited = set()
    components = []

    def dfs_rev(v, current_component):
        if v in visited:
            return
        visited.add(v)
        current_component.add(v)
        for nxt in rev[v]:
            dfs_rev(nxt, current_component)

    while finished:
        v = finished.pop()
        if v not in visited:
            current_component = set()
            dfs_rev(v, current_component)
            components.append(current_component)

    return components


def ts(g, rev):
    # Topsort using Kahn's algorithm:
    # Track any vertex with indegree 0: for each, add it to the output before
    # decrementing the indegree of each of its neighbors. If the neighbor now
    # has indegree 0, add it to the indegree 0 set
    inzero = [i for i, v in enumerate(rev) if v == 0]
    topsort = []

    while inzero:
        v = inzero.pop()
        topsort.append(v)
        for nxt in g[v]:
            rev[nxt] -= 1
            if rev[nxt] == 0:
                inzero.append(nxt)
    return topsort


def sc(f):
    """For each of the given graphs, determine if they are semi-connected. To do so:

    1. Find the strongly connected components
    2. Use the SCC to construct the condensation graph
    3. The graph is semi connected if and only if the condensation graph is a simple path
    """
    n = int(f.readline())
    res = []

    for _ in range(n):
        f.readline()  # blank
        n_verts, n_edges = map(int, f.readline().split(' '))
        g = {i+1: [] for i in range(n_verts)}
        rev = {i+1: [] for i in range(n_verts)}

        for _ in range(n_edges):
            a, b = map(int, f.readline().split(' '))
            g[a].append(b)
            rev[b].append(a)

        components = scc(g, rev)
        # print(components)

        # iterate through each vert of each component, and find the component containing
        # the vert. This is effectively a vert -> component index, for the next step
        c_for_v = {}
        for i, c in enumerate(components):
            for v in c:
                c_for_v[v] = i

        # now we can iterate over each edge, constructing the condensation graph
        cond = {i: set() for i in range(len(components))}
        rev = [0] * len(components)  # indegrees
        for v, neighbors in g.items():
            for nxt in neighbors:
                c_v, c_nxt = c_for_v[v], c_for_v[nxt]
                if c_v == c_nxt:
                    continue
                cond[c_v].add(c_nxt)
                rev[c_nxt] += 1

        ordered = ts(cond, rev)
        # print(ordered)
        # verify simple path order
        for i in range(len(ordered) - 1):
            u, v = ordered[i], ordered[i+1]
            if cond[u] != {v}:
                res.append(False)
                break
        else:
            res.append(cond[ordered[-1]] == set())  # ensure outdegree 0 at sink

    return ' '.join('1' if r else '-1' for r in res)


sample = io.StringIO("""2

3 2
3 2
2 1

3 2
3 2
1 2""")

assert sc(sample) == '1 -1'

with open('/Users/oz/Downloads/rosalind_sc (1).txt') as f: print(sc(f))
