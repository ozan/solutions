from pprint import pprint


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
                stack.append(v[0])
    return out


def modified_suffix_trie(text):
    """
    Construct a modified suffix trie, per the pseudocode on p 165
    """
    g = {0: {}}

    # build the trie
    for start in range(len(text)):
        i = start
        node = 0
        while i < len(text):
            c = text[i]
            # each value was previously the node id
            # now it should be (node_id, first_i, len)
            if c in g[node]:
                node = g[node][c][0]
            else:
                if c == '$':
                    g[node][c] = start
                else:
                    nxt = len(g)
                    g[node][c] = (nxt, i, 1)
                    g[nxt] = {}
                    node = nxt
            i += 1
    return g


def sufix_tree(g):
    """
    Convert the modified suffix trie to a tree by replacing each non-branching path depth first
    """
    stack = [0]
    while stack:
        n = stack.pop()
        for k, v in g[n].items():
            if k == '$': continue
            nxt_node, first_i, lngth = v
            while len(g[nxt_node]) == 1:

                kk = list(g[nxt_node].keys())[0]
                try:
                    nxt_nxt_node = g[nxt_node][kk][0]
                    del g[nxt_node]
                    nxt_node = nxt_nxt_node
                    lngth += 1
                except TypeError:  # could be end of string TODO cleanup
                    lngth += 1
                    break
            g[n][k] = (nxt_node, first_i, lngth)
            stack.append(nxt_node)
    return g


def find(tree, pattern):
    """
    Find the given pattern in the suffix tree, if any

    Not actually required for the problem, but good to know that we can!
    """
    node = 0
    i = 0
    while i < len(pattern):
        c = pattern[i]
        if c in tree[node]:
            match = tree[node][c]
            node = match[0]
            i += match[2]
        else:
            return []
    return leaves(tree, node)


def print_edges(tree, text):
    stack = [0]
    while stack:
        node = stack.pop()
        for k, v in tree[node].items():
            if k == '$':
                continue
            print(text[v[1]:v[1]+v[2]])
            stack.append(v[0])


def ba9d(text):
    g = modified_suffix_trie(text)

    pprint(g)

    gg = sufix_tree(g)
    pprint(gg)

    """
    for pattern in ('antenna', 'ana', 'as'):
        idxs = find(gg, pattern)
        if idxs:
            print(f'{pattern} FOUND starting at {", ".join(str(n) for n in idxs)}')
        else:
            print(f'{pattern} not found')
    """

    print_edges(gg, text)


ba9d('banana')

# ba9d('ATATCGTTTTATCGTT$')

# with open('/Users/oz/Downloads/rosalind_ba9d.txt') as f: ba9d(f.read().rstrip())


