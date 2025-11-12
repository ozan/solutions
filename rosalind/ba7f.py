from collections import defaultdict
import io

SYMBOLS = 'ACGT'


def ba7f(f):
    _ = int(f.readline())

    g = defaultdict(list)
    tags = {}
    nn = None
    sk = defaultdict(list)

    # initialize our graph and Sk lookup
    for line in f:
        a, b = line.rstrip().split('->')
        g[a].append(b)
        g[b]
        tags[a] = tags[b] = 0
        try:
            int(b)
        except ValueError:
            # this is a leaf
            nn = nn or len(b)
            tags[b] = 1
            sk[b] = [{sym: 0 if sym == c else nn for sym in SYMBOLS} for c in b]

    bt = {v: [{sym: None for sym in SYMBOLS} for _ in range(nn)] for v in g}
    # run the DP algorithm to completion
    root = None
    while True:
        remaining = False
        for v, children in g.items():
            if tags[v]:
                continue  # already processed  TODO surely better way to track this
            if 0 in {tags[k] for k in children}:
                continue  # not ripe TODO again better way to track?

            remaining = True
            tags[v] = 1
            root = v

            for i in range(nn):
                d = {}
                for k in SYMBOLS:
                    tot = 0
                    for kid in children:
                        x, xj = min((j_cost + (j != k), j) for j, j_cost in sk[kid][i].items())
                        tot += x
                        bt[kid][i][k] = xj
                    d[k] = tot
                sk[v].append(d)

        if not remaining:
            break

    # compute the final root label and total
    label = []
    total = 0
    for scores in sk[root]:
        c, s = min(scores.items(), key=lambda x: x[1])
        label.append(c)
        total += s
    print(total)

    # backtrack to compute inner node labels and weights
    verdict = {root: ''.join(label)}
    stack = [root]
    out = []
    while stack:
        v = stack.pop()
        parent_label = verdict[v]
        for kid in g[v]:
            verd = []
            diff = 0
            for i, x in enumerate(parent_label):
                verd.append(bt[kid][i][x])
                if bt[kid][i][x] != x:
                    diff += 1
            vv = ''.join(verd)
            verdict[kid] = vv
            out.append((parent_label, vv, diff))
            stack.append(kid)

    for a, b, w in out:
        print(f'{a}->{b}:{w}')
        print(f'{b}->{a}:{w}')


sample = io.StringIO("""4
4->CAAATCCC
4->ATTGCGAC
5->CTGCGCTG
5->ATGGACGA
6->4
6->5""")

ba7f(sample)


# with open('/Users/oz/Downloads/rosalind_ba7f (2).txt') as f: ba7f(f)
