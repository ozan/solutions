from collections import defaultdict
# import utils as u


def ba3i(n):
    """
    k-Universal circular string
    """
    # iterate over every 2**n strings and construct the de-bruijn graph
    g = defaultdict(list)
    for i in range(1 << n):
        s = f'{{:0{n}b}}'.format(i)
        pref, suff = s[:-1], s[1:]
        g[pref].append(suff)

    v = pref
    final = []
    path = [v]

    while path:
        if g[v]:
            path.append(v)
            v = g[v].pop()
        else:
            # backtrack
            final.append(v)
            v = path.pop()

    parts = list(reversed(final))
    out = [parts[0]]
    out.extend(p[-1:] for p in parts[1:-(n-1)])
    return ''.join(out)


# print(ba3i(4))


with open('/Users/oz/Downloads/rosalind_ba3i.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    print(ba3i(8))
