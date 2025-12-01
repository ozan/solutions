from pprint import pprint


def modified_suffix_trie(text):
    """
    Construct a modified suffix trie, per the pseudocode on p 165.

    Vertices are simply incrementing integers, starting at 0 for the root.
    Edges are mappings of the next letter to the next node, annotated too with the start
    index of the first occurence of that substring
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
    tree = {}
    while stack:
        n = stack.pop()
        tree[n] = {}
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
            tree[n][(first_i, lngth)] = nxt_node
            g[n][k] = (nxt_node, first_i, lngth)
            stack.append(nxt_node)
    return tree


def ba9d(text):
    text += '$'
    g = modified_suffix_trie(text)

    # pprint(g)

    gg = sufix_tree(g)
    # pprint(gg)

    # find the deepest node that still has two or more children
    stack = [(0, '')]
    best = (0, '')
    while stack:
        node, ss = stack.pop()
        for k, v in gg[node].items():
            start, lngth = k
            if not gg[v]:
                continue
            # print(text[start:start+lngth], depth + lngth)
            nxt = ss + text[start:start+lngth]
            best = max(best, (len(nxt), nxt))
            stack.append((v, nxt))
    print(best[1])


ba9d('ATATCGTTTTATCGTT')
# ba9d('panamabanana')


# with open('/Users/oz/Downloads/rosalind_ba9d.txt') as f: ba9d(f.read().rstrip())
