from collections import defaultdict


def parse(s):
    i = 0
    out = []
    while i < len(s):
        j = s.index(')', i)
        out.append([int(x) for x in s[i+1:j].split()])
        i = j + 1
    return out


def ba6c(ps, qs):
    pqs = parse(ps)
    pqs.extend(parse(qs))

    g = defaultdict(list)

    for seq in pqs:
        for i, x in enumerate(seq):
            y = seq[(i + 1) % len(seq)]
            g[x].append(-y)
            g[-y].append(x)

    q = list(g.keys())
    visited = set()
    path = set()
    cycles = 0
    while q:
        v = q.pop()

        if v in path:
            cycles += 1
            path = set()
            continue
        path.add(v)

        for nxt in g[v]:
            if nxt not in visited:
                q.append(nxt)
        visited.add(v)

    return len(g) // 2 - cycles


sample = """
(+1 +2 +3 +4 +5 +6)
(+1 -3 -6 -5)(+2 -4)""".strip().split('\n')

print(ba6c(*sample))

with open('/Users/oz/Downloads/rosalind_ba6c.txt') as f:
    print(ba6c(*f.read().rstrip().split('\n')))
