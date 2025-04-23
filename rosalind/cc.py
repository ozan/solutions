def cc(data):
    nv, ne = map(int, data[0].split())
    g = {i+1: [] for i in range(nv)}

    for line in data[1:]:
        a, b = map(int, line.split())
        g[a].append(b)
        g[b].append(a)

    visited = set()
    pending = list(g.keys())
    q = []
    c = 0
    while pending:
        if q:
            v = q.pop()
            if v in visited:
                continue
        else:
            v = pending.pop()
            if v in visited:
                continue
            c += 1

        q.extend(g[v])
        visited.add(v)

    print(c)

    # deg2 = [sum(len(g[x]) for x in g[i+1]) for i in range(nv)]

    # print(' '.join(str(n) for n in deg2))


sample = """12 13
1 2
1 5
5 9
5 10
9 10
3 4
3 7
3 8
4 8
7 11
8 11
11 12
8 12""".split('\n')

cc(sample)

with open('/Users/oz/Downloads/rosalind_cc.txt') as f:
    cc(f.read().rstrip().split('\n'))


