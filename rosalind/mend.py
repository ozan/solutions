import io

from Bio import Phylo


GENOTYPES = ('AA', 'Aa', 'aa')


C_PROBS = (
    (1.0, 0.5, 0.0, 0.5, 0.25, 0.0, 0.0, 0.0, 0.0),  # weightings for AA
    (0.0, 0.5, 1.0, 0.5, 0.5,  0.5, 1.0, 0.5, 0.0),  # weightings for Aa
    (0.0, 0.0, 0.0, 0.0, 0.25, 0.5, 0.0, 0.5, 1.0),  # weightings for aa
)


def prob(clade):
    if clade.name in GENOTYPES:
        return [1.0 if clade.name == g else 0.0 for g in GENOTYPES]

    if clade.name is None:
        X, Y = prob(clade.clades[0]), prob(clade.clades[1])
        P = [x * y for x in X for y in Y]  # parent probs

        return [
            sum(c * p for c, p in zip(cps, P))
            for cps in C_PROBS
        ]

    return (0.0, 0.0, 0.0)  # invalid input


def mend(nwck_tree):
    tree = Phylo.read(io.StringIO(nwck_tree), 'newick')
    vec = prob(tree.root)
    return ' '.join(f'{x:.3f}' for x in vec)


# sample = "(aa, Aa);"
sample = "((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);"

print(mend(sample))


with open('/Users/oz/Downloads/rosalind_mend.txt') as f:
    print(mend(f.read()))
