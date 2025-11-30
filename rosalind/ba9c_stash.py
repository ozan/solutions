def leaves(g, node):
    """
    DFS to find all leaves reachable from the given node
    """
    out = []
    stack = [node]
    while stack:
        n = stack.pop()
        for k, v in g[n].items():
            if k == '$':
                out.append(v)
            else:
                stack.append(v)
    return out


def ba9c(string):
    g = {0: {}}

    # build the trie
    for start in range(len(string)):
        # p = string[start:]  # TODO use index instead of slice
        i = start
        node = 0
        while i < len(string):
            c = string[i]
            if c in g[node]:
                node = g[node][c]
            else:
                if c == '$':
                    g[node][c] = start
                else:
                    nxt = len(g)
                    g[node][c] = nxt
                    g[nxt] = {}
                    node = nxt
            i += 1

    for case in ('antenna', 'ana', 'as'):
        node = 0
        for c in case:
            if c in g[node]:
                node = g[node][c]
            else:
                print(f'{case} not found')
                break
        else:
            print(f'{case} FOUND starting at {leaves(g, node)}')

    return

    # TODO check text for better way compact into a tree
    for k, v in list(g.items()):
        for s, nxt in list(v.items()):
            while nxt in g and len(g[nxt]) == 1:
                s2, nnxt = list(g[nxt].items())[0]
                # print(f'{s} -> {s+s2}, {nxt} -> {nnxt}')
                g[k][s+s2] = nnxt
                del g[k][s]
                del g[nxt]
                nxt, s = nnxt, s + s2

    # print(g)
    for k, v in g.items():
        for s in v.keys():
            print(s)
    # print(string)


# ba9c('hi$')
ba9c('panamabananas$')
# ba9d('ATATCGTTTTATCGTT$')

# with open('/Users/oz/Downloads/rosalind_ba9c.txt') as f: ba9d(f.read().rstrip())


