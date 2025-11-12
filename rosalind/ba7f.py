from collections import defaultdict
import io

SYMBOLS = 'ACGT'


def ba7f(f):
    _ = int(f.readline())

    g = defaultdict(list)
    tags = {}
    bt = {}
    edges = [line.rstrip().split('->') for line in f]
    for a, b in edges:
        g[a].append(b)
        bt[b] = []
        tags[a] = tags[b] = 0

    sk = defaultdict(list)

    # initialize leaves
    for _, v in edges:
        if v in g:
            continue
        tags[v] = 1
        # TODO more compact representation
        sk[v] = [{sym: 0 if sym == c else float('inf') for sym in SYMBOLS} for c in v]

    final_processed = None
    while True:
        remaining = False
        for v, children in g.items():
            if tags[v]:
                continue  # already processed  TODO surely better way to track this
            if 0 in {tags[k] for k in children}:
                continue  # not ripe TODO again better way to track?

            remaining = True
            tags[v] = 1
            final_processed = v

            nn = len(sk[children[0]])  # TODO zip instead?

            for i in range(nn):
                d = {}
                for k in SYMBOLS:
                    tot = 0
                    for kid in children:
                        x, xj = min((j_cost + (j != k), j) for j, j_cost in sk[kid][i].items())
                        tot += x
                        try:
                            bt[kid][i][k] = xj
                        except IndexError:
                            bt[kid].append({k: xj})

                    d[k] = tot

                sk[v].append(d)

        if not remaining:
            break

    label = []
    total = 0
    for scores in sk[final_processed]:
        c, s = min(scores.items(), key=lambda x: x[1])
        label.append(c)
        total += s
    print(total)

    verdict = {final_processed: ''.join(label)}

    stack = [final_processed]
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
