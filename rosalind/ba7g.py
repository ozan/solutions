from collections import defaultdict
import io

SYMBOLS = 'ACGT'


def ba7g(f):
    _ = int(f.readline())

    g = defaultdict(list)
    nn = None
    sk = defaultdict(list)

    # initialize graph
    for line in f:
        a, b = line.rstrip().split('->')
        g[a].append(b)
        try:
            int(b)
        except ValueError:
            # this is a leaf
            nn = nn or len(b)

    # remove the most recent edge and add a new root!
    g[a].remove(b)
    g[b].remove(a)
    root = str(len(g))
    g[root].extend([a, b])

    # initialize sk lookup and bt table
    sk = {}
    for v in g:
        try:
            int(v)
            # internal node
            sk[v] = [{sym: 0 for sym in SYMBOLS} for i in range(nn)]
        except ValueError:
            # leaf node
            sk[v] = [{sym: 0 if sym == v[i] else nn for sym in SYMBOLS} for i in range(nn)]
    bt = {v: [{sym: None for sym in SYMBOLS} for _ in range(nn)] for v in g}

    # create a rooted tree and get post-order traversal
    q = [root]
    visited = {root}
    parent = {root: None}
    rooted_g = defaultdict(list)

    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        for v_ in g[u]:
            if v_ not in visited:
                visited.add(v_)
                parent[v_] = u
                rooted_g[u].append(v_)
                q.append(v_)

    post_order = q

    # run the DP algorithm
    for v_ in reversed(post_order):
        if not rooted_g[v_]:  # is leaf
            continue
        for kid in rooted_g[v_]:
            for i in range(nn):
                for k in SYMBOLS:
                    x, xj = min((j_cost + (j != k), j) for j, j_cost in sk[kid][i].items())
                    sk[v_][i][k] += x
                    bt[kid][i][k] = xj

    # compute the final root label and total
    label, scores = zip(*(min(place.items(), key=lambda x: x[1]) for place in sk[root]))

    print(sum(scores))

    # backtrack to compute inner node labels and weights
    verdict = {root: ''.join(label)}
    stack = [root]
    out = []
    while stack:
        v = stack.pop()
        parent_label = verdict[v]
        for kid in rooted_g[v]:
            verd = []
            diff = 0
            for i, x in enumerate(parent_label):
                verd.append(bt[kid][i][x])
                if bt[kid][i][x] != x:
                    diff += 1
            vv = ''.join(verd)
            verdict[kid] = vv
            out.append((v, kid, diff))
            stack.append(kid)

    # reconstruct the original tree and print
    final_edges = []
    v_neighbors = []
    for u1, u2, w in out:
        if u1 == root:
            v_neighbors.append(u2)
            continue
        final_edges.append((verdict[u1], verdict[u2], w))

    if len(v_neighbors) == 2:
        u1, u2 = v_neighbors
        label1, label2 = verdict[u1], verdict[u2]
        diff = sum(c1 != c2 for c1, c2 in zip(label1, label2))
        final_edges.append((label1, label2, diff))

    for a, b, w in final_edges:
        print(f'{a}->{b}:{w}')
        print(f'{b}->{a}:{w}')


sample = io.StringIO("""4
TCGGCCAA->4
4->TCGGCCAA
CCTGGCTG->4
4->CCTGGCTG
CACAGGAT->5
5->CACAGGAT
TGAGTACC->5
5->TGAGTACC
4->5
5->4""")

# ba7g(sample)


with open('/Users/oz/Downloads/rosalind_ba7g.txt') as f: ba7g(f)
