from collections import Counter
from functools import reduce, partial

import utils as u


product = partial(reduce, lambda a, b: a * b)


def count(kmers):
    return [Counter(row) for row in zip(*[[k for k in kmer] for kmer in kmers])]


def profilemost(counts, kmers):  # profile-most kmer for the given profile
    return max(
        (product(c[x] for x, c in zip(k, counts)), -i, k)
        for i, k in enumerate(kmers)
    )[2]


def score(kmers):  # sum of all the non-consensus counts
    return sum(sum(sorted(c.values())[:-1]) for c in count(kmers))


def ba2d(data):
    k, t = map(int, data[0].split())
    dna = data[1:]

    best_motifs = [s[:k] for s in dna]

    for j in range(len(dna[0]) - k + 1):
        motifs = [dna[0][j:j+k]]
        for i in range(1, t):
            candidates = [dna[i][ii:ii+k] for ii in range(0, len(dna[i]) - k + 1)]
            motifs.append(profilemost(count(motifs), candidates))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    print('\n'.join(best_motifs))
    return best_motifs


sample = """3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG""".split('\n')

# ba2d(sample)

with open('/Users/oz/Downloads/rosalind_ba2d.txt') as f:
#    s, t = [x for _, x in u.scan_fasta(f)]
    ba2d(f.read().rstrip().split('\n'))
