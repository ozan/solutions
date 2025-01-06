from collections import defaultdict
# import utils as u


def fmt(k, d, x, indent=0):
    s, t = x[:k-1], x[k-1:]
    return f'{indent*' '}{s}{d * '-'}{t}'


def ba3j(data):
    k, d = (int(x) for x in data[0].split())

    g = defaultdict(list)
    inv = set()
    for row in data[1:]:
        s, t = row.split('|')
        pref = s[:-1] + t[:-1]
        suff = s[1:] + t[1:]
        g[pref].append(suff)
        inv.add(suff)

    v = list(set(g.keys()) - inv)[0]
    final = []
    path = [v]

    while path:
        if g[v]:
            v = g[v].pop()
            path.append(v)
        else:
            v = path.pop()
            final.append(v)

    rev = list(reversed(final))
    out = [rev[0][:k-1]]
    out.extend(s[k-2:k-1] for s in rev[1:])
    out.extend(s[-1] for s in rev[-(k+d):])
    # for i, x in enumerate(rev):
        # print(fmt(k, d, x, indent=i))
    return ''.join(out)
    # print(''.join(out))



sample = """4 2
GAGA|TTGA
TCGT|GATG
CGTG|ATGT
TGGT|TGAG
GTGA|TGTT
GTGG|GTGA
TGAG|GTTG
GGTC|GAGA
GTCG|AGAT""".split('\n')

# print(ba3j(sample))


with open('/Users/oz/Downloads/rosalind_ba3j.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    print(ba3j(f.read().rstrip().split('\n')))
