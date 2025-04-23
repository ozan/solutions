from pprint import pprint
from collections import Counter


def find_repeated(g, depth=0):
    for s in g:
        # print('  ' * depth, s, len(g[s]))
        if not len(g[s]):
            yield ''
        for ss in find_repeated(g[s], depth + 1):
            yield s + ss


def all_substrings(g, n=0):
    for k, v in g[n].items():
        if len(g[v]) == 0:
            yield k
        for k2 in all_substrings(g, v):
            yield k + k2


def restructure(g, node=0):
    return {k: restructure(g, n) for k, n in g[node].items()}


def ba9d(string):
    g = {0: {}}

    # build the trie
    for i in range(len(string)):
        p = string[i:]  # TODO use index instead of slice
        node = 0
        for c in p:
            if c in g[node]:
                node = g[node][c]
            else:
                nxt = len(g)
                g[node][c] = nxt
                g[nxt] = {}
                node = nxt
    
    # compact into a tree
    for k, v in list(g.items()):
        for s, nxt in list(v.items()):
            while nxt in g and len(g[nxt]) == 1:
                s2, nnxt = list(g[nxt].items())[0]
                g[k][s+s2] = nnxt
                print(k, s, s2, nnxt)
                del g[k][s]
                del g[nxt]
                nxt, s = nnxt, s + s2
    
    subs = all_substrings(g)
    print(list(subs))

    # gg = restructure(g)
    return g


from functools import cache
from os.path import commonprefix

def get_edges(graph):
    for k in graph.keys():
        yield k
        yield from get_edges(graph[k])


@cache
def suffix_tree(seq, starts):
    graph = {}
    bases = sorted(set([seq[start] for start in starts]))
    for base in bases:
        matching = [start for start in starts if seq[start] == base]
        seqs = [seq[s:] for s in matching]
        prefix = commonprefix(seqs)
        size = len(prefix)
        new_starts = [start + size for start in matching if start + size < len(seq)]
        graph[prefix] = suffix_tree(seq, tuple(new_starts))
    return graph


def suff(seq):
    return suffix_tree(seq, tuple(range(len(seq))))

def find_repeated(g, depth=0):
    for s in g:
        print('  ' * depth, s, len(g[s]))
        if not len(g[s]):
            yield ''
        for ss in find_repeated(g[s], depth + 1):
            yield s + ss

def internal_edges(tree):
    for n1 in tree.keys():
        if not len(tree[n1]):
            yield ""
        for n2 in internal_edges(tree[n1]):
            yield n1 + n2


def longest_shared_substring(tree):
    return max(internal_edges(tree), key=lambda x: len(x))


# tr = suff('ATATCGTTTTATCGTT')
# pprint(tr)
# print(list(internal_edges(tr)))

tr2 = ba9d('ATATCGTTTTATCGTT')
pprint(tr2)
# print(list(internal_edges(tr2)))

# ba9d('ATATCGTTTTATCGTT')
# ba9d('panamabananas$')

# with open('/Users/oz/Downloads/rosalind_ba9d.txt') as f:
#    ba9d(f.read().rstrip())


