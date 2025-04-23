
def ba9c(string):
    g = {0: {}}

    # build the trie
    for i in range(len(string)):
        p = string[i:]  # TODO use index instead of slice
        node = 0
        for c in p:
            if c in g[node]:
                node = g[node][c]
            else:
                nxt = len(g)
                g[node][c] = nxt
                g[nxt] = {}
                node = nxt

    # compact into a tree
    for k, v in list(g.items()):
        for s, nxt in list(v.items()):
            while nxt in g and len(g[nxt]) == 1:
                s2, nnxt = list(g[nxt].items())[0]
                # print(f'{s} -> {s+s2}, {nxt} -> {nnxt}')
                g[k][s+s2] = nnxt
                del g[k][s]
                del g[nxt]
                nxt, s = nnxt, s + s2

    for k, v in g.items():
        for s in v.keys():
            print(s)
    # print(string)


# ba9c('ATAAATG$')

with open('/Users/oz/Downloads/rosalind_ba9c.txt') as f:
    ba9c(f.read().rstrip())


