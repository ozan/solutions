from collections import defaultdict
# import utils as u


# Maximal Non-Branching Path Problem
def ba3m(data):
    g = defaultdict(list)
    ins = defaultdict(lambda: 0)
    outs = defaultdict(lambda: 0)

    for line in data:
        a, bs = line.split(' -> ')
        g[a] = list(set(bs.split(',')))
        for b in g[a]:
            ins[b] += 1
        outs[a] += len(g[a])

    # start stack with all nodes, but place those with *no* inbound
    # nodes close to end (processed first). That way we will eventually
    # deal with isolated cycles, but avoid starting any path at a non-cycle
    # intermediate node
    stack = [(k, [k]) for k in g.keys()]
    stack.sort(key=lambda x: ins[x[0]], reverse=True)
    # stack = [(x, [x]) for x in set(g.keys()) if x not in ins]
    out = []

    while stack:
        v, path = stack.pop()

        while g[v]:
            nxt = g[v].pop()
            if ins[nxt] == 1 and outs[nxt] == 1 and nxt not in path:  # non-branching
                stack.append((nxt, path + [nxt]))
            else:
                out.append(path + [nxt])
                stack.append((nxt, [nxt]))
    
    print('\n'.join(' -> '.join(path) for path in out))
    return out


sample = """1 -> 2
2 -> 3
3 -> 4,5
6 -> 7
7 -> 6""".split('\n')

# ba3m(sample)


with open('/Users/oz/Downloads/rosalind_ba3m (1).txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    ba3m(f.read().rstrip().split('\n'))
    """
    print('digraph {')
    for line in f.readlines():
        a, bs = line.rstrip().split(' -> ')
        print(f'  {a} ->', '{', ' '.join(b for b in bs.split(',')), '}')
    print('}')
    """
