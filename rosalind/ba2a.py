from collections import defaultdict
from itertools import combinations, product


def mutations(s, d):
    seen = set()
    for indices in combinations(range(len(s)), d):
        for replacements in product('ATCG', repeat=d):
            m = dict(zip(indices, replacements))
            mut = ''.join(m[i] if i in m else ch for i, ch in enumerate(s))
            if mut not in seen:
                seen.add(mut)
                yield mut


def f(dna, k, d):
    motifs = None
    for s in dna:
        muts = set()
        for i in range(len(s) - k + 1):
            muts.update(set(mutations(s[i:i+k], d)))
        if motifs is None:
            motifs = muts
        else:
            motifs.intersection_update(muts)
    return motifs


print(' '.join(f("""TTCCGGGCGTCTCAATAACGAAGTA
AATAGGATTGCATAGCGCTCGTCGT
GATTTATGGCACCAGAAAAAGCCGT
AGGTAGCCGCTCCCACCTATGTCGT
GCCGTGACTTCTCAAATTCACACAG
TCCACGCCGTGACATTATCTCTTCC
GTCGTGCCGAGAACCGTATATGACG
CCCGCGCCGTGCTCGATAATTGAGT
GCCGTAGTGGTACGATCTGTTTAGA
GCCTTTCGAGGCCGTCCACAAATTG""".split("\n"), 5, 1)))
