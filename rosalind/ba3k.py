from collections import defaultdict
# import utils as u


def ba3k(patterns):
    # construct the De Bruijn graph
    g = defaultdict(list)
    edges_out = defaultdict(lambda: 0)
    edges_in = defaultdict(lambda: 0)
    for p in patterns:
        pref, suff = p[:-1], p[1:]
        g[pref].append(suff)
        edges_out[pref] += 1
        edges_in[suff] += 1

    # start q from entry nodes (AG and GA in the sample)
    # we store both the vertex, and the path so far
    q = [(k, k) for k in g.keys() if k not in edges_in]

    out = []

    while q:
        v, path = q.pop()

        while g[v]:
            nxt = g[v].pop()
            if edges_out[nxt] == 1 and edges_in[nxt] == 1:
                q.append((nxt, path + nxt[-1]))
            else:
                out.append(path + nxt[-1])
                q.append((nxt, nxt))

    print(' '.join(out))


sample = """ATG
ATG
TGT
TGG
CAT
GGA
GAT
AGA""".split('\n')

# print(ba3k(sample))


with open('/Users/oz/Downloads/rosalind_ba3k.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    ba3k(f.read().rstrip().split('\n'))
