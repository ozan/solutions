def parse(data):
    i = 0
    out = []
    while i < len(data):
        j = data.find(')', i)
        out.append([int(x) for x in data[i+1:j].split()])
        i = j+1
    return out


def ba6h(data):
    parts = parse(data)

    edges = []
    for part in parts:
        for i, x in enumerate(part):
            y = part[(i+1) % len(part)]
            frm = x*2 if x > 0 else -x*2-1
            to = y*2-1 if y > 0 else -y*2
            edges.append((frm, to))

    print(', '.join(str(edge) for edge in edges))


def ba6k(data):
    """
    Steps:

    genome -> edges (including node renaming step)
    replace an edge
    edges -> genome
    """
    edges = []
    for part in parse(data[0]):
        for i, x in enumerate(part):
            y = part[(i+1) % len(part)]
            frm = x*2 if x > 0 else -x*2-1
            to = y*2-1 if y > 0 else -y*2
            edges.append((frm, to))

    a, b, c, d = [int(n) for n in data[1].split(', ')]

    broken = []
    for x, y in edges:
        if x == a and y == b:
            broken.append((a, c))
        elif x == b and y == a:
            broken.append((c, a))
        elif x == c and y == d:
            broken.append((b, d))
        elif x == d and y == c:
            broken.append((d, b))
        else:
            broken.append((x, y))
    
    g = {}
    for a, b in broken:
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

sample = """(+1 -2 -4 +3)
1, 6, 3, 8""".split('\n')
# expected: (2, 4), (3, 1), (7, 5), (6, 8)
# ba6k(sample)

with open('/Users/oz/Downloads/rosalind_ba6k.txt') as f:
    ba6k(f.read().strip().split('\n'))

