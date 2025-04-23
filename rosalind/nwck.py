def parse(t):
    """
    Given a newick format tree, return a Python tree of the form:

    (root, [children])

    ... where each child is itself a tree

    >>> parse('a')
    ('a', [])

    >>> parse('(b)a;')
    ('a', [('b', [])])

    >>> parse('(b,c)a;')
    ('a', [('b', []), ('c', [])])

    >>> parse('((b,c),d)a;')
    ('a', [('', [('b', []), ('c', [])]), ('d', [])])

    >>> parse('(b,(c,d))a;')
    ('a', [('b', []), ('', [('c', []), ('d', [])])])

    >>> parse('((b,c),(d,e))a;')
    ('a', [('', [('b', []), ('c', [])]), ('', [('d', []), ('e', [])])])

    >>> parse('((dog,cat),mouse)animal;')
    ('animal', [('', [('dog', []), ('cat', [])]), ('mouse', [])])
    """
    cl, cr, pl, pr = t.find(','), t.rfind(','), t.find('('), t.rfind(')')
    # Handle base case of single node
    if pl == -1:
        return (t.rstrip(';'), [])

    # Get root name after last parenthesis
    root = t[pr+1:].rstrip(';')

    # Get contents between parentheses
    contents = t[pl+1:pr]

    # Split contents on commas if they exist
    if cl == -1:
        children = [contents]
    else:
        # Need to handle nested commas by tracking parentheses
        children = []
        start = 0
        pcount = 0
        for i, c in enumerate(contents):
            if c == '(' : pcount += 1
            elif c == ')': pcount -= 1
            elif c == ',' and pcount == 0:
                children.append(contents[start:i])
                start = i + 1
        children.append(contents[start:])

    # Recursively parse children
    return (root, [parse(child) for child in children])


def find_path(tree, node):
    """
    Given a tree and a node, return the path from the root to the node as a list

    >>> find_path(('a', [('b', []), ('c', [])]), 'b')
    ['a', 'b']

    >>> find_path(('a', [('b', []), ('c', [])]), 'c')
    ['a', 'c']

    >>> find_path(('a', [('b', []), ('c', [])]), 'a')
    ['a']
    """
    if tree[0] == node:
        return [node]
    for child in tree[1]:
        path = find_path(child, node)
        if path:
            return [tree[0]] + path
    return None


def nwck(data):
    cases = [(data[i], data[i+1]) for i in range(0, len(data), 3)]

    out = []
    for nwck_tree, start_end in cases:
        tree = parse(nwck_tree)
        start, end = start_end.split(' ')
        p1, p2 = find_path(tree, start), find_path(tree, end)

        # Find the length of common prefix
        common_length = 0
        for x, y in zip(p1, p2):
            if x == y:
                common_length += 1
            else:
                break
        
        # Distance is sum of path lengths minus twice the common prefix length
        distance = len(p1) + len(p2) - 2 * common_length
        out.append(distance)

    return ' '.join(map(str, out))


sample = """
((c)b)a;
a c

((d,e)c,(f,g)b)a;
d f

(cat)dog;
dog cat

(dog,cat);
dog cat""".strip().split('\n')

# print(nwck(sample))


with open('/Users/oz/Downloads/rosalind_nwck (1).txt') as f:
    print(nwck(f.read().rstrip().split('\n')))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
