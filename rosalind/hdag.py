import io


sample = """2

3 3
1 2
2 3
1 3

4 3
4 3
3 2
4 1"""


def ts(g, rev):
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

    return topsort


def hdag(f):
    """
    Find a Hamiltonian path (if any) by first finding a topological sort order
    (which is guaranteed, since this is a dag)
    """
    n_graphs = int(f.readline())

    for _ in range(n_graphs):
        f.readline()
        num_v, num_e = map(int, f.readline().split(' '))
        g = [[] for i in range(num_v + 1)]
        rev = [0 for i in range(num_v + 1)]

        for _ in range(num_e):
            a, b = map(int, f.readline().split(' '))
            g[a].append(b)
            rev[b] += 1

        topsort = ts(g, rev)
        # Now that we have a (any) topolical ordering, we can check if there are edges
        # between each. If so, it is a Hamiltonian path. If not, NONE exists
        for i in range(num_v - 1):
            a, b = topsort[i], topsort[i+1]
            if b not in g[a]:
                print('-1')
                break
        else:
            print('1 ' + ' '.join(str(n) for n in topsort))


# hdag(io.StringIO(sample))
with open('/Users/oz/Downloads/rosalind_hdag (1).txt') as f: hdag(f)
