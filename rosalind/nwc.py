import io


def has_negative_cycle(n_verts, edges):
    """
    Run Bellman-Ford algorithm, then see if an additional "relaxation" is possible after n_vert-1
    prior updates. If so, this must be due to a negative cycle.

    Uses a dummy vert (0) and augmented edges, in case the negative cycle exists somewhere
    unreachable from node 1.
    """
    dist = [float('inf')] * (n_verts + 1)
    dist[0] = 0

    for i in range(1, n_verts + 1):
        edges.append((0, i, 0))

    for _ in range(n_verts):
        for u, v, w in edges:
            dist[v] = min(dist[v], dist[u] + w)

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return True

    return False


def nwc(f):
    n_graphs = int(f.readline())
    out = []

    for _ in range(n_graphs):
        # f.readline()
        n_verts, n_edges = map(int, f.readline().split(' '))
        edges = [list(map(int, f.readline().split(' '))) for _ in range(n_edges)]
        out.append(has_negative_cycle(n_verts, edges))

    return ' '.join('1' if res else '-1' for res in out)


sample = io.StringIO("""2

4 5
1 4 4
4 2 3
2 3 1
3 1 6
2 1 -7

3 4
1 2 -8
2 3 20
3 1 -1
3 2 -30""")

# assert nwc(sample) == '-1 1'
with open('/Users/oz/Downloads/rosalind_nwc (2).txt') as f: print(nwc(f))
