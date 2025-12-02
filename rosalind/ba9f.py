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


def smallest_absent(tree, s, sub):
    """
    Find the shortest prefix of sub that is entirely absent from s (represented by tree)

    Start at the root. If the first character of sub isn't the prefix of any key, then
    that's it! If the first is, but second isn't, that's it! If we keep going until a
    prefix of sub is an exact match of an edge of tree, we must continue down the tree
    until we find a non-match. If we exceed the bound of sub itself, we must return None
    """
    node = 0
    subi = 0
    while subi < len(sub):
        tree_edges = tree[node]

        for (start, length), v in tree_edges.items():
            comp = s[start:start+length]
            if comp == sub[subi:subi+length]:
                # exact match, must descend
                node = v
                subi += length
                break
        else:
            if sub[subi:subi+1] == '$':
                return None
            comps = {s[start:start+length] for start, length in tree_edges}
            for j in range(1, len(sub) - subi):
                if sub[subi:subi+j] not in {c[:j] for c in comps}:
                    return sub[:subi+j]
            else:
                return None


def ba9f(f):
    s1 = f.readline().rstrip() + '$'
    s2 = f.readline().rstrip() + '$'

    t1 = suffix_tree(modified_suffix_trie(s1))
    t2 = suffix_tree(modified_suffix_trie(s2))

    smallest = s1
    for sub in all_substrings(t1, s1):
        candidate = smallest_absent(t2, s2, sub)
        if candidate and len(candidate) < len(smallest):
            smallest = candidate

    print(smallest)


sample = io.StringIO("""CCAAGCTGCTAGAGG
CATGCTGGGCTGGCT""")

# ba9f(sample)

with open('/Users/oz/Downloads/rosalind_ba9f.txt') as f: ba9f(f)
