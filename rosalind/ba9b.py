

def build_trie(patterns):
    g = [{}]

    for p in patterns:
        node = 0
        for c in p:
            if c in g[node]:
                node = g[node][c]
            else:
                nxt = len(g)
                g[node][c] = nxt
                g.append({})
                node = nxt
        g[node][''] = True
    return g


def ba9b(data):
    text = data[0]
    patterns = data[1:]
    trie = build_trie(patterns)

    out = []
    for start in range(len(text)):
        i = 0
        node = 0
        while start + i <= len(text):
            if '' in trie[node]:
                out.append(start)
                break
            try:
                c = text[start + i]
                node = trie[node][c]
                i += 1
            except (IndexError, KeyError):
                break

    print(' '.join(str(o) for o in out))


sample = """AATCGGGTTCAATCGGGGT
ATCG
GGGT""".split('\n')

ba9b(sample)

# with open('/Users/oz/Downloads/rosalind_ba9b.txt') as f:
#    ba9b(f.read().rstrip().split('\n'))


