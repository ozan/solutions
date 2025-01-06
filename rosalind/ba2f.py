from collections import Counter
from functools import reduce, partial
from random import randint

import utils as u


product = partial(reduce, lambda a, b: a * b)


def count(kmers):
    return [Counter(row) for row in zip(*[[k for k in kmer] for kmer in kmers])]


def profilemost(counts, kmers):  # profile-most kmer for the given profile
    return max(
        (product(c[x] + 1 for x, c in zip(k, counts)), -i, k)
        for i, k in enumerate(kmers)
    )[2]


def score(kmers):  # sum of all the non-consensus counts
    return sum(sum(sorted(c.values())[:-1]) for c in count(kmers))


NUM_RUNS = 1000


def rand_slice(k, s):
    i = randint(0, len(s) - k)
    return s[i:i+k]


def ba2f(data):
    k, t = map(int, data[0].split())
    dna = data[1:]

    best_overall = []

    for _ in range(NUM_RUNS):
        motifs = [rand_slice(k, s) for s in dna]
        best = motifs

        while True:
            counts = count(motifs)
            motifs = []
            for s in dna:
                candidates = [s[ii:ii+k] for ii in range(0, len(s) - k + 1)]
                motifs.append(profilemost(counts, candidates))
            if score(motifs) >= score(best):
                break
            best = motifs

        if not best_overall or score(best) < score(best_overall):
            best_overall = best

    print('\n'.join(best_overall))

    return best_overall


sample = """8 5
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA""".split('\n')

ba2f(sample)

with open('/Users/oz/Downloads/rosalind_ba2f.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    ba2f(f.read().rstrip().split('\n'))
