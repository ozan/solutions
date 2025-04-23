
def ba6i(data):
    edges = [tuple(map(int, part.split(', ')))
             for part in data[1:-1].split('), (')]
    
    g = {}
    for a, b in edges:
        aa = (-1 if a % 2 == 1 else 1) * (a+1) // 2
        bb = (-1 if b % 2 == 0 else 1) * ((b+1) // 2)
        g[aa] = bb

    cycle = []
    q = list(g.keys())
    visited = set()
    out = []
    while q:
        v = q.pop()
        if v in visited:
            continue
        visited.add(v)
        cycle.append(v)

        nxt = g[v]
        if nxt in cycle:
            out.append(cycle)
            cycle = []
            continue
        
        q.append(nxt)

    print(''.join('(' + ' '.join(f'{x:+}' for x in cycle) + ')' for cycle in out))


# sample = '(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)'
# expected: (+1 -2 -3)(-4 +5 -6)
# ba6i(sample)

with open('/Users/oz/Downloads/rosalind_ba6i.txt') as f:
    ba6i(f.read().strip())

