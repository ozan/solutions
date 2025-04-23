import heapq


def dij(data):
    nv, ne = map(int, data[0].split())
    g = {i+1: [] for i in range(nv)}

    for line in data[1:]:
        a, b, w = map(int, line.split())
        g[a].append((b, w))

    dist = [-1] * (nv + 1)
    
    q = [(0, 1)]
    visited = set()

    while q:
        d, v = heapq.heappop(q)

        if v in visited:
            continue

        visited.add(v)
        dist[v] = d

        for nxt, d2 in g[v]:
            heapq.heappush(q, (d+d2, nxt))



    print(' '.join(str(x) for x in dist[1:]))


sample = """6 10
3 4 4
1 2 4
1 3 2
2 3 3
6 3 2
3 5 5
5 4 1
3 2 1
2 4 2
2 5 3""".split('\n')

dij(sample)

with open('/Users/oz/Downloads/rosalind_dij.txt') as f:
    dij(f.read().rstrip().split('\n'))


