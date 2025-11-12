import io


def bf(f):
    """Bellman-Ford algorithm, with guarantee of NO negative cycles"""
    n_verts, n_edges = map(int, f.readline().split(' '))
    dist = [float('inf')] * (n_verts + 1)
    dist[1] = 0
    edges = [list(map(int, line.split(' '))) for line in f.readlines()]

    for _ in range(n_verts - 1):
        any_changes = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                any_changes = True
        if not any_changes:
            break  # no need for relaxation

    out = ' '.join('x' if x == float('inf') else str(x) for x in dist[1:])
    return out


sample = io.StringIO("""9 13
1 2 10
3 2 1
3 4 1
4 5 3
5 6 -1
7 6 -1
8 7 1
1 8 8
7 2 -4
2 6 2
6 3 -2
9 5 -10
9 4 7""")

# assert bf(sample) == '0 5 5 6 9 7 9 8 x'
with open('/Users/oz/Downloads/rosalind_bf.txt') as f: print(bf(f))
