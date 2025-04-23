from collections import defaultdict
from pprint import pprint


def ba7a(data):
    n = int(data[0])

    g = defaultdict(list)

    for line in data[1:]:
        ab_str, w_str = line.split(':')
        w = int(w_str)
        a, b = map(int, ab_str.split('->'))

        # ignore edge direction by only keeping one of each pair
        # TODO this assumes every edge is present twice
        if a > b:
            continue

        # any c that was connected to a and d connected to b are
        # now transtively connected c <-> d
        for c, w2 in g[a]:
            for d, w3 in g[b]:
                g[c].append((d, w+w2+w3))
                g[d].append((c, w+w2+w3))

        # any c that was previously connected to a is now
        # transitively also connected to b. Same with those connected
        # via b to a
        for c, w2 in g[a]:
            g[c].append((b, w+w2))
            g[b].append((c, w+w2))
        for c, w2 in g[b]:
            g[c].append((a, w+w2))
            g[a].append((c, w+w2))

        # finally a -> b and b -> a are also, obviously, edges
        g[a].append((b, w))
        g[b].append((a, w))

    # pprint(g)

    dist = [[None] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # TODO why do we need to take the min, here? How are we accumulating
    # excessive paths when paths should be unique?
    for a, vals in g.items():
        for b, w in vals:
            if a < n and b < n:
                dist[a][b] = w if dist[a][b] is None else min(w, dist[a][b])

    for row in dist:
        print('\t'.join(['0' if x is None else str(x) for x in row]))
    print()


sample = """4
0->4:11
1->4:2
2->5:6
3->5:7
4->0:11
4->1:2
4->5:4
5->4:4
5->3:7
5->2:6""".split('\n')


transitive = """5
0->1:1
1->0:1
0->2:1
2->0:1
3->4:1
4->3:1
0->3:1
3->0:1""".split('\n')

# ba7a(sample)
# ba7a(transitive)

with open('/Users/oz/Downloads/rosalind_ba7a (6).txt') as f:
    ba7a(f.read().rstrip().split('\n'))
