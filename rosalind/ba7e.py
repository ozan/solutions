import io


def ba7e(f):
    """Neighbor joining"""
    m = int(f.readline())  # identity of new nodes, starting at number of current nodes

    T = []  # final tree output stored as a list of vert1, vert2, distance

    # D is our distance matrix, per the book. We extend this but zero out merged nodes, to
    # avoid losing track of the identities of nodes, which are indexes into this matrix
    D = [[float(x) for x in f.readline().split()] for _ in range(m)]

    # We track nodes left to merge, since the others are simply zeroed out in D
    remaining = set(range(m))

    while len(remaining) > 2:
        # Find nodes i and j to merge (without explicitly building D* matrix)
        TD = {i: sum(D[i]) for i in remaining}
        _, mi, mj = min(
            ((len(remaining)-2)*D[i][j] - TD[i] - TD[j], i, j)
            for i in TD for j in TD
            if i > j
        )
        delta = (TD[mi] - TD[mj]) / (len(remaining) - 2)
        T.append((mi, m, (D[mi][mj] + delta) / 2))  # limb length to mi
        T.append((mj, m, (D[mi][mj] - delta) / 2))  # limb length to mj
        remaining -= {mi, mj}
        remaining.add(m)
        m += 1

        # add a row to D and for now also extend each row
        # TODO this would probably be tidier if we added rows and not columns, although
        # it would then be hard to maintain the invariant that we only index into D
        # is D[i][j] where i > j
        col = []
        for k, row in enumerate(D):
            dkm = (D[mi][k] + D[mj][k] - D[mi][mj]) / 2
            dkm = max(0, dkm)
            row.append(dkm)
            col.append(dkm)
        col.append(0)
        D.append(col)

        # zero out i and j rows of D
        for k in range(len(D)):
            D[k][mi] = D[k][mj] = D[mi][k] = D[mj][k] = 0

    mi, mj = list(remaining)  # must only be 2 remaining at this point
    T.append((mi, mj, D[mi][mj]))

    T.sort()
    return '\n'.join(f'{a}->{b}:{w:.3f}\n{b}->{a}:{w:.3f}' for a, b, w in T)


sample = io.StringIO("""4
0   23  27  20
23  0   30  28
27  30  0   30
20  28  30  0""")

# print(ba7e(sample))

with open('/Users/oz/Downloads/rosalind_ba7e.txt') as f: print(ba7e(f))
