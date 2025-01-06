from collections import defaultdict


def ba5n(data):
    g = defaultdict(list)
    for line in data:
        a, bs = line.split(' -> ')
        for b in bs.split(','):
            g[a].append(b)

    topsort = []
    visited = set()

    def dfs(node):
        visited.add(node)
        for nxt in g[node]:
            if nxt not in visited:
                dfs(nxt)
        topsort.append(node)

    for node in list(g.keys()):
        if node not in visited:
            dfs(node)

    topsort.reverse()

    print(', '.join(str(x) for x in topsort))
    return topsort


sample = '''1 -> 2
2 -> 3
4 -> 2
5 -> 3'''.split('\n')

ba5n(sample)

with open('/Users/oz/Downloads/rosalind_ba5n.txt') as f:
    ba5n(f.read().rstrip().split('\n'))
