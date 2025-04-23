from collections import defaultdict
from pprint import pprint

masses = [
    ('A', 71),
    ('C', 103),
    ('D', 115),
    ('E', 129),
    ('F', 147),
    ('G', 57),
    ('H', 137),
    ('I', 113),
    ('K', 128),
    ('L', 113),
    ('M', 131),
    ('N', 114),
    ('P', 97),
    ('Q', 128),
    ('R', 156),
    ('S', 87),
    ('T', 101),
    ('V', 99),
    ('W', 186),
    ('Y', 163),
]


mass_for_aa = dict(masses)
aa_for_mass = dict((v, k) for k, v in masses)


def ba11e(data):
    S = [int(x) for x in data]

    g = defaultdict(list)
    inv = defaultdict(list)

    for i in range(len(S) - 1):
        w = 0 if i == 0 else S[i-1]
        for j in range(i+1, len(S)+1):
            if j - i in aa_for_mass:
                g[i].append(j)
                inv[j].append((i, w))

    # first, topsort g
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

    # then, compute maximum path from start to end, by calculating
    # for each in topsort order
    best = {0: (0, None)}
    for n in topsort:
        x, y = 0, None
        for prev, w in inv[n]:
            try:
                xx = w + best[prev][0]
            except KeyError:
                continue
            if xx >= x:
                x, y = xx, prev
        if y is not None:
            best[n] = (x, y)

    # reconstruct peptide
    j = len(S)
    i = best[j][1]
    out = []
    while i is not None:
        out.append(aa_for_mass[j-i])
        i, j = best[i][1], i

    out.reverse()
    print(''.join(out))


sample = '0 0 0 4 -2 -3 -1 -7 6 5 3 2 1 9 3 -8 0 3 1 2 1 0'.split()


with open('/Users/oz/Downloads/rosalind_ba11e (3).txt') as f:
    print(ba11e(f.read().rstrip().split()))
