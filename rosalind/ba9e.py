import io
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


def suffix_tree(g):
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


def all_substrings(tree, s):
    """
    Generate all possible substrings of the given suffix tree, depth first
    """
    stack = [(0, '')]
    while stack:
        node, sub = stack.pop()
        yield sub
        for k, v in tree[node].items():
            start, length = k
            stack.append((v, sub + s[start:start+length]))


def find(tree, s, sub):
    """
    Determine if the given subtring exists in the suffix tree
    """
    node = 0
    i = 0
    while i < len(sub):
        for k, v in tree[node].items():
            start, length = k
            if s[start:start+length] == sub[i:i+length]:
                i += length
                node = v
                break
            for j in range(length-1, 0, -1):
                if s[start:start+j] == sub[i:i+j]:
                    return sub[:i+j]
        else:
            return False
    return sub


def ba9e(f):
    s1 = f.readline().rstrip() + '$'
    s2 = f.readline().rstrip() + '$'

    t1 = suffix_tree(modified_suffix_trie(s1))
    t2 = suffix_tree(modified_suffix_trie(s2))

    best = ''
    for sub in all_substrings(t1, s1):
        if len(sub) <= len(best):
            continue
        found = find(t2, s2, sub)
        if found and len(found) > len(best):
            best = found
    print(best)


sample = io.StringIO("""TCGGTAGATTGCGCCCACTC
AGGGGCTCGCAGTGTAAGAA""")

# ba9e(sample)

with open('/Users/oz/Downloads/rosalind_ba9e.txt') as f: ba9e(f)
