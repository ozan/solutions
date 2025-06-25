import io

from Bio import Phylo


def nkew(data):
    cases = [(data[i], data[i+1]) for i in range(0, len(data), 3)]

    out = []
    for nwck_tree, start_end in cases:
        start, end = start_end.split(' ')

        tree = Phylo.read(io.StringIO(nwck_tree), 'newick')
        out.append(int(tree.distance(start, end)))

    return ' '.join(map(str, out))


sample = """
(dog:42,cat:33);
cat dog

((dog:4,cat:3):74,robot:98,elephant:58);
dog elephant
""".strip().split('\n')

print(nkew(sample))


with open('/Users/oz/Downloads/rosalind_nkew.txt') as f:
    print(nkew(f.read().rstrip().split('\n')))
