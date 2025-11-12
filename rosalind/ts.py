import io


sample = """4 5
1 2
3 1
3 2
4 3
4 2
"""


def ts(f):
    num_v, num_e = map(int, f.readline().split(' '))
    g = [[] for i in range(num_v + 1)]
    rev = [0 for i in range(num_v + 1)]

    for _ in range(num_e):
        a, b = map(int, f.readline().split(' '))
        g[a].append(b)
        rev[b] += 1

    # Topsort using Kahn's algorithm:
    # Track any vertex with indegree 0: for each, add it to the output before
    # decrementing the indegree of each of its neighbors. If the neighbor now
    # has indegree 0, add it to the indegree 0 set
    inzero = [i for i, v in enumerate(rev) if v == 0 and i > 0]
    topsort = []

    while inzero:
        v = inzero.pop()
        topsort.append(v)
        for nxt in g[v]:
            rev[nxt] -= 1
            if rev[nxt] == 0:
                inzero.append(nxt)

    print(' '.join(str(n) for n in topsort))


# ts(io.StringIO(sample))
with open('/Users/oz/Downloads/rosalind_ts.txt') as f: ts(f)
