

def get_path(g, src, dst):
    q = [(src, [])]
    visited = set()
    while q:
        n, path = q.pop()
        if n in visited:
            continue
        visited.add(n)

        if n == dst:
            return path

        for nxt, w in g[n].items():
            q.append((nxt, path + [(nxt, w)]))

    return None


def limb(n, j, D):
    return min(D[j][i] + D[j][k] - D[i][k]
               for i in range(n) for k in range(i+1, n)
               if i != j and k != j) // 2


def additive_phylogeny(n, D, intern_i=None):
    if intern_i is None:
        intern_i = n

    if n == 2:
        return {0: {1: D[0][1]}, 1: {0: D[1][0]}}, intern_i

    l = limb(n, n-1, D)

    # TODO do we really need a copy?
    D_bald = [
        [x - (0 if i == j else l if i == n - 1 or j == n - 1 else 0)
         for i, x in enumerate(row)]
        for j, row in enumerate(D)]

    i_match, k_match = None, None
    for i in range(n-1):
        for k in range(i+1, n-1):
            if D_bald[i][k] == D_bald[i][n-1] + D_bald[k][n-1]:
                i_match = i
                k_match = k
                dist = D_bald[i][n-1]
                break
    if i_match is None or k_match is None:
        return {}

    D_trimmed = [row[:-1] for row in D_bald[:-1]]

    g, intern_i = additive_phylogeny(n-1, D_trimmed, intern_i)

    for other in (i_match, k_match):
        # TODO incorporate into path split?
        if D_bald[other][n-1] == 0:
            g[n-1] = {other: l}
            g[other][n-1] = l
            break
    else:
        # insert node (if not exists) at distance dist between i_match and k_match
        path = get_path(g, i_match, k_match)

        path_i = 0
        curr, subs = i_match, None
        forward = dist  # e.g. 11
        rest = None

        while True:
            subs, next_dist = path[path_i]  # e.g. 1, 13
            if next_dist < forward:
                forward -= next_dist
                curr = subs
                path_i += 1
                continue
            rest = next_dist - forward
            break

        # print(forward, rest, curr, subs)

        # insert new node
        g[curr][intern_i] = forward
        g[subs][intern_i] = rest
        g[intern_i] = {
            curr: forward,
            subs: rest,
            n-1: l
        }
        g[n-1] = {intern_i: l}  # TODO what if n-1 already exists? possible?

        # delete split edge
        for neighbor, _ in g[curr].items():
            if neighbor == subs:
                del g[curr][neighbor]
                break

        for neighbor, _ in g[subs].items():
            if neighbor == curr:
                del g[subs][neighbor]
                break

        intern_i += 1

        # don't forget about j

    return g, intern_i


def ba7c(data):
    n = int(data[0])
    D = [[int(x) for x in row.split()] for row in data[1:]]
    g, _ = additive_phylogeny(n, D, n)

    for x, ys in g.items():
        for y, w in ys.items():
            print(f'{x}->{y}:{w}')

    return g


sample = """4
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0""".split('\n')

# print(ba7b(sample))


def test():
    cases = [
        [[[0, 2],
          [2, 0]],
         {0: {1: 2}, 1: {0: 2}}],
        [[[0, 3, 7],
          [3, 0, 4],
          [7, 4, 0]],
         {0: {1: 3}, 1: {0: 3, 2: 4}, 2: {1: 4}}],
        [[[0, 5, 6],
          [5, 0, 3],
          [6, 3, 0]],
         {0: {3: 4}, 1: {3: 1}, 2: {3: 2}, 3: {0: 4, 1: 1, 2: 2}}],
        [[[0, 13, 21, 22],
          [13, 0, 12, 13],
          [21, 12, 0, 13],
          [22, 13, 13, 0]],
         {0: {4: 11}, 1: {4: 2}, 2: {5: 6}, 3: {5: 7}, 4: {0: 11, 1: 2, 5: 4}, 5: {4: 4, 3: 7, 2: 6}}]
    ]
    for D, exp in cases:
        actual, _ = additive_phylogeny(len(D), D)
        if actual != exp:
            print(f'Expected {exp}\nbut got  {actual}')
            exit()

    print(f'{len(cases)} tests passed')


test()


# with open('/Users/oz/Downloads/rosalind_ba7c (1).txt') as f:
#   ba7c(f.read().rstrip().split('\n'))
