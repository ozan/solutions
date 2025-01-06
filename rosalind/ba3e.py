# import utils as u
import itertools as it


def ba3e(patterns):
    pairs = sorted((p[:-1], p[1:]) for p in patterns)
    for source, neighbors in it.groupby(pairs, lambda x: x[0]):
        print(f'{source} -> {",".join(n[1] for n in neighbors)}')


sample = """GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG""".split('\n')

# ba3e(sample)


with open('/Users/oz/Downloads/rosalind_ba3e (1).txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    ba3e(f.read().rstrip().split('\n'))
