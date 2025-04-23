

def ba9a(patterns):
    g = {0: {}}

    for p in patterns:
        node = 0
        for c in p:
            if c in g[node]:
                node = g[node][c]
            else:
                nxt = len(g)
                g[node][c] = nxt
                g[nxt] = {}
                node = nxt

    for a, v in g.items():
        for c, b in v.items():
            print(f'{a}->{b}:{c}')


sample = """ATAGA
ATC
GAT""".split('\n')

# ba9a(sample)

with open('/Users/oz/Downloads/rosalind_ba9a.txt') as f:
    ba9a(f.read().rstrip().split('\n'))


