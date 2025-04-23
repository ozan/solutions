def bfs(data):
    nv, ne = map(int, data[0].split())
    g = {i+1: [] for i in range(nv)}

    for line in data[1:]:
        a, b = map(int, line.split())
        g[a].append(b)

    dist = [-1] * (nv + 1)

    level = 0
    nodes = [1]
    visited = set()

    while nodes:
        nxt = []
        for x in nodes:
            dist[x] = level
            for neighbor in g[x]:
                if neighbor not in visited:
                    nxt.append(neighbor)
                    visited.add(neighbor)
        nodes = nxt
        level += 1

    print(' '.join(str(x) for x in dist[1:]))


sample = """6 6
4 6
6 5
4 3
3 5
2 1
1 4""".split('\n')

# bfs(sample)

with open('/Users/oz/Downloads/rosalind_bfs.txt') as f:
    bfs(f.read().rstrip().split('\n'))


