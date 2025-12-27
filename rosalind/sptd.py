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


def find_splits(root, taxa_map):
    """
    Determine all the non-trivial splits using a postorder traversal of the tree
    """
    sp = []

    def f(node):
        if not node.children:
            return 1 << taxa_map[node.name]

        s = 0
        for c in node.children:
            s |= f(c)
        sp.append(s)

        return s

    f(root)
    return sp


def sptd(f):
    taxa = sorted(f.readline().rstrip().split(' '))
    taxa_map = {taxon: i for i, taxon in enumerate(taxa)}
    num_taxa = len(taxa)
    all_taxa_bm = (1 << num_taxa) - 1

    t1 = parse_newick(f.readline())
    t2 = parse_newick(f.readline())

    sp1 = find_splits(t1, taxa_map)
    sp2 = find_splits(t2, taxa_map)

    # cannonicalize...
    sp1_can, sp2_can = set(), set()
    for splits, canonical in ((sp1, sp1_can), (sp2, sp2_can)):
        for sp_bm in splits:
            # if the first taxon is not in the split, take the complement
            if not (sp_bm & 1):
                xx = all_taxa_bm ^ sp_bm
            else:
                xx = sp_bm
            # number of set bits
            c = bin(xx).count('1')

            if 2 <= c < num_taxa - 1:
                canonical.add(xx)

    common = len(sp1_can & sp2_can)

    out = 2 * (num_taxa - 3) - 2 * common
    print(out)
    return out


sample = io.StringIO("""dog rat elephant mouse cat rabbit
(rat,(dog,cat),(rabbit,(elephant,mouse)));
(rat,(cat,dog),(elephant,(mouse,rabbit)));""")


# sptd(sample)


with open('/Users/oz/Downloads/rosalind_sptd.txt') as f: assert sptd(f) == 270
