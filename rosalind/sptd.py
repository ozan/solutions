from collections import namedtuple
import io

Node = namedtuple('Node', ['name', 'children'])


def format_tree(node):
    if node.name is not None:
        return node.name
    if node.children:
        return f'({",".join(format_tree(c) for c in node.children)})'
    return ''


def parse_newick(newick):
    newick = newick.rstrip(';')

    if not newick:
        return None

    stack = []
    dummy_root = Node(name=None, children=[])
    node = dummy_root
    name = []

    for char in newick:

        if char == '(':
            if name:
                leaf_name = ''.join(name).strip()
                if leaf_name:
                    node.children.append(Node(name=leaf_name, children=[]))
                name = []

            stack.append(node)
            new_clade_node = Node(name=None, children=[])
            node.children.append(new_clade_node)
            node = new_clade_node

        elif char == ',':
            if name:
                leaf_name = ''.join(name).strip()
                if leaf_name:
                    node.children.append(Node(name=leaf_name, children=[]))
                name = []

        elif char == ')':
            if name:
                leaf_name = ''.join(name).strip()
                if leaf_name:
                    node.children.append(Node(name=leaf_name, children=[]))
                name = []
            if stack:
                node = stack.pop()

        elif not char.isspace():
            name.append(char)

    if name:
        leaf_name = ''.join(name).strip()
        if leaf_name:
            node.children.append(Node(name=leaf_name, children=[]))

    if dummy_root.children:
        return dummy_root.children[0]
    return None


t = "(rat,(dog,cat),(rabbit,(elephant,mouse)));"
t2 = "(rat,(cat,dog),(elephant,(mouse,rabbit)));"

tree = parse_newick(t)

assert format_tree(tree) + ';' == t


def p(t, indent=0):
    if t.name:
        print(' ' * indent + t.name)
    else:
        print(' ' * indent + '-')
    if t.children:
        for c in t.children:
            p(c, indent + 2)


def find_splits(root):
    """
    Determine all the non-trivial splits using a postorder traversal of the tree
    """
    sp = []

    def f(node):
        if not node.children:
            return [node.name]

        s = []
        for c in node.children:
            s.extend(f(c))
        sp.append(sorted(s))

        return s

    f(root)
    return sp


def sptd(f):
    taxa = sorted(f.readline().rstrip().split(' '))
    t1 = parse_newick(f.readline())
    t2 = parse_newick(f.readline())

    sp1 = find_splits(t1)
    sp2 = find_splits(t2)

    # cannonicalize... TODO surely a better way
    sp1_can, sp2_can = [], []
    for splits, canonical in ((sp1, sp1_can), (sp2, sp2_can)):
        for sp in splits:
            if sp[0] != taxa[0]:
                xx = [x for x in taxa if x not in sp]
            else:
                xx = sp

            if 2 <= len(xx) < len(taxa) - 1:
                canonical.append(xx)

    common = 0
    for x in sp1_can:
        if x in sp2_can:  # TODO surely a better way
            common += 1

    out = 2 * (len(taxa) - 3) - 2 * common
    print(out)
    return out


sample = io.StringIO("""dog rat elephant mouse cat rabbit
(rat,(dog,cat),(rabbit,(elephant,mouse)));
(rat,(cat,dog),(elephant,(mouse,rabbit)));""")


# sptd(sample)


with open('/Users/oz/Downloads/rosalind_sptd.txt') as f: assert sptd(f) == 270
