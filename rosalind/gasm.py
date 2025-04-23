from collections import defaultdict

comp = dict(zip('ACGT', 'TGCA'))


def gasm(reads):
    for k in range(2, len(reads[0]) - 1):
        g = defaultdict(list)
        for read in reads:
            rc = ''.join(comp[x] for x in reversed(read))
            for i in range(len(read) - k):
                g[read[i:i+k]].append(read[i+1:i+k+1])
                g[rc[i:i+k]].append(rc[i+1:i+k+1])

        # if there are two cycles, we should be able to
        # start anywhere in the graph, exhaust part of it
        # with one cycle, then return the path formed from the other

        for _ in range(2):
            q = [list(g.keys())[0]]
            path = []
            while q:
                v = q.pop()
                if v in path:
                    break
                path.append(v)
                for nxt in g[v]:
                    q.append(nxt)
                del g[v]
        if not g:
            return ''.join(p[0] for p in path)


sample = """AATCT
TGTAA
GATTA
ACAGA""".split('\n')

print(gasm(sample))

with open('/Users/oz/Downloads/rosalind_gasm.txt') as f:
    print(gasm(f.read().rstrip().split('\n')))
