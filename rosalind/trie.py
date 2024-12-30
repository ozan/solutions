# import utils as u


def print_edges(tree, prior, count):
    for k, v in tree.items():
        count += 1
        print(f'{prior} {count} {k}')
        count = print_edges(v, count, count)
    return count


def trie(ss):
    root = {}

    for s in ss:
        t = root
        for c in s:
            if c not in t:
                t[c] = {}
            t = t[c]

    print_edges(root, 1, 1)


sample = """ATAGA
ATC
GAT""".split('\n')

sample2 = """ABC""".split('\n')

# trie(sample)

with open('/Users/oz/Downloads/rosalind_trie.txt') as f:
    (trie(f.read().rstrip().split('\n')))
