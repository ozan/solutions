# import utils as u


def ba3g(lines):
    g = {}
    inv = {}

    for line in lines:
        a, bs = line.split(' -> ')
        g[a] = set(bs.split(','))
        for b in g[a]:
            if b in inv:
                inv[b] += 1
            else:
                inv[b] = 1

    v = [k for k, v in inv.items() if k in g and len(g[k]) != v][0]

    path = [v]
    final = []

    while path:
        if v in g and g[v]:
            path.append(v)
            v = g[v].pop()
        else:  # backtrack
            final.append(v)
            v = path.pop()

    print('->'.join(reversed(final)))
    return reversed(final)


sample = """0 -> 2
1 -> 3
2 -> 1
3 -> 0,4
6 -> 3,7
7 -> 8
8 -> 9
9 -> 6""".split('\n')

# ba3g(sample)


with open('/Users/oz/Downloads/rosalind_ba3g.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    ba3g(f.read().rstrip().split('\n'))
