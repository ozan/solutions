# import utils as u


def ba3f(lines):
    g = {}

    total = 0
    for line in lines:
        a, bs = line.split(' -> ')
        g[a] = set(bs.split(','))
        total += len(g[a])

    v = a
    path = [v]
    final = []

    while path:
        if g[v]:
            path.append(v)
            v = g[v].pop()
        else:  # backtrack
            final.append(v)
            v = path.pop()

    print('->'.join(reversed(final)))
    return reversed(final)


sample = """0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6""".split('\n')

# ba3f(sample)


with open('/Users/oz/Downloads/rosalind_ba3f (1).txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    pass
    ba3f(f.read().rstrip().split('\n'))
