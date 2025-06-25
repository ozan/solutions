import io

from Bio import Phylo


def nwck(data):
    cases = [(data[i], data[i+1]) for i in range(0, len(data), 3)]

    out = []
    for nwck_tree, start_end in cases:
        start, end = start_end.split(' ')

        tree2 = Phylo.read(io.StringIO(nwck_tree), "newick")
        p1 = tree2.get_path(start)
        p2 = tree2.get_path(end)

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


with open('/Users/oz/Downloads/rosalind_nwck (2).txt') as f:
    print(nwck(f.read().rstrip().split('\n')))
