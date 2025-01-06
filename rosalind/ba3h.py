from collections import defaultdict
# import utils as u


def ba3h(data):
    patterns = data[1:]

    # construct the De Bruijn graph
    g = defaultdict(list)
    inv = set()
    for p in patterns:
        pref, suff = p[:-1], p[1:]
        g[pref].append(suff)
        inv.add(suff)

    v = list(set(g.keys()) - inv)[0]

    path = [v]
    final = []

    while path:
        if v in g and g[v]:
            path.append(v)
            v = g[v].pop()
        else:  # backtrack
            final.append(v)
            v = path.pop()

    # construct full string
    path = reversed(final)
    out = [next(path)]
    out.extend(p[-1] for p in path)
    return ''.join(out)


sample = """4
CTTA
ACCA
TACC
GGCT
GCTT
TTAC""".split('\n')

print(ba3h(sample))


with open('/Users/oz/Downloads/rosalind_ba3h.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    print(ba3h(f.read().rstrip().split('\n')))
