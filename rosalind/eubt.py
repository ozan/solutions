

def newick(tree):
    """
    Warmup: given a binary tree as array of arrays, format in newick

    Internal repr is that trees and subtrees are list types; leaves are non-lists
    """

    def fmt(t):
        if type(t) is list:
            return '(' + ','.join(fmt(tt) for tt in t) + ')'
        else: return str(t)

    return fmt(tree) + ';'  # TODO arbitrary root choice


def eubt_prior(labels):
    """
    Enumerate all possible unrooted binary trees with the given labels.

    If only 3 labels, there's only one unrooted tree: [a, [b, c]]

    Note that a root is chosen arbitrarily here for the sake of representation.

    With 4 labels, we can construct trees by starting with this one, and adding
    the fourth label by branching at any existing edge:

    """

    def f(t, new):
        x, y = t
        if type(x) is not list:
            yield [[x, new], y]
        else:
            for subt in f(x, new):
                yield [subt, y]
        if type(y) is not list:
            yield [x, [y, new]]
        else:
            for subt in f(y, new):
                yield [x, subt]

        if type(x) is list and type(y) is list:
            yield [[x, new], y]
            yield [x, [y, new]]

    assert len(labels) >= 3

    # start with size 3 tree
    tree = [labels[0], labels[1:3]]

    # iteratively generate more
    trees = [tree]
    for i in range(3, len(labels)):
        nxt = []
        for t in trees:
            for tt in f(t, labels[i]):
                nxt.append(tt)
        trees = nxt

    for t in trees:
        print(newick(t))



def eubt(labels):
    """
    This time try representing as an edge list, including with internal nodes.

    Enumerate internal nodes from 1 up, as needed (first after 3)
    """
    if len(labels) == 3:
        return [[(x, 1) for x in labels]]

    assert len(labels) == 4
    tree = eubt(labels[:3])[0]
    out = []
    for edge in tree:
        print(edge)
        # t2 = treeZZ

    # each edge can be split to form a new tree


# print(newick([[1, 2], 3]))
# print(newick(['dog', ['cat', ['mouse', 'elephant']]]))

# eubt(['a', 'b', 'c', 'd', 'e'])
print(eubt('abcd'))

sample = 'dog cat mouse elephant'.split()

#print(sample)
