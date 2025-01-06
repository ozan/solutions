from collections import Counter
from functools import reduce, partial
from random import choices, randint


product = partial(reduce, lambda a, b: a * b)


def count(kmers, skip=None):
    return [Counter(row) for row in zip(*[[k for k in kmer]
                                          for i, kmer in enumerate(kmers)
                                          if i != skip])]


def profilemost(counts, kmers):  # profile-most kmer for the given profile
    return max(
        (product(c[x] + 1 for x, c in zip(k, counts)), -i, k)
        for i, k in enumerate(kmers)
    )[2]


def profile_sample(counts, kmers):
    probs = [(k, product(c[x] + 1 for x, c in zip(k, counts))) for k in kmers]
    out = choices(*zip(*probs), k=1)
    return out[0]


def score(kmers):  # sum of all the non-consensus counts
    return sum(sum(sorted(c.values())[:-1]) for c in count(kmers))


def consensus(profile):
    return ''.join(max((v, k) for k, v in c.items())[1] for c in profile)


STARTS = 20
STEP_PER_START = 5000


def rand_slice(k, s):
    i = randint(0, len(s) - k)
    return s[i:i+k]


def DosR(dna):

    for k in range(20, 21):
        best_overall = []
        for _ in range(STARTS):
            motifs = [rand_slice(k, s) for s in dna]
            best = motifs

            for _ in range(STEP_PER_START):
                i = randint(0, len(dna)-1)
                counts = count(motifs, skip=i)
                candidates = (dna[i][ii:ii+k] for ii in range(0, len(dna[i]) - k + 1))
                motifs[i] = profile_sample(counts, candidates)
                if score(motifs) < score(best):
                    best = motifs

            if not best_overall or score(best) < score(best_overall):
                best_overall = best

        print(f'{k:<2} {score(best_overall) / k:.3f} {consensus(count(best_overall))}')

        print('\n'.join(best_overall))

    return best_overall



with open('/Users/oz/Downloads/DosR.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    DosR(f.read().rstrip().split('\n'))
