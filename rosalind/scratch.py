from collections import defaultdict


def ba5d(data):
    start, end = data[0], data[1]

    g = defaultdict(list)
    inv = defaultdict(list)
    for line in data[2:]:
        adj, w = line.split(':')
        a, b = adj.split('->')
        g[a].append((b, int(w)))  # TODO do we need w here?
        inv[b].append((a, int(w)))

    # first, topsort g

    topsort = []
    visited = set()

    def dfs(node):
        visited.add(node)
        for nxt, _ in g[node]:
            if nxt not in visited:
                dfs(nxt)
        topsort.append(node)

    for node in list(g.keys()):
        if node not in visited:
            dfs(node)

    topsort.reverse()

    # then, compute maximum path from start to end, by calculating
    # for each in topsort order
    best = {start: (0, None)}
    for n in topsort:
        x, y = 0, None
        for prev, w in inv[n]:
            try:
                xx = w + best[prev][0]
            except KeyError:
                continue
            if xx > x:
                x, y = xx, prev
        if y:
            best[n] = (x, y)

    score, prev = best[end]
    print(score)
    path = [end]
    while prev:
        path.append(prev)
        prev = best[prev][1]

    print('->'.join(reversed(path)))

    return best[end]


sample = """9
4
9->1:7
9->2:4
2->3:2
1->4:1
3->4:3""".split('\n')

# print(ba5d(sample))

with open('/Users/oz/Downloads/rosalind_ba5d (1).txt') as f:
    ba5d(f.read().rstrip().split('\n'))
