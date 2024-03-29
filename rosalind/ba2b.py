from itertools import product


def hamming(xs, ys):
    return sum(x != y for x, y in zip(xs, ys))


def f(k, dna):
    d = None
    best_pattern = None
    for pattern in product('ACGT', repeat=k):
        dist = sum(
            min(hamming(pattern, s[i:i+k]) for i in range(len(s) - k + 1))
            for s in dna
        )
        if d is None or dist < d:
            d = dist
            best_pattern = pattern
    return best_pattern


print(f(6, """
GTTTTCGGACAAAAGGAAGATCGTAGATGGCAAGATGCCACT
CTCGGTTTTCTCAAATTGATCCCCTCTAACAGATCGGCTACG
AATGACCTGATAAGTGATGCAAAGAGGTTTAGATGGGATCCA
GGGGAGCTCCAGTTTATCCATCAAAGATGGCCGTGAAAGCTA
CCGTGAAGATCGGATAGCACTGCACCTCTTGCTACATTCCAA
AAATATCATGGTAGATGGAGCCTCTGTGTAACTTGTCAGATG
GTACTTGGCGCACAGGCCATATCTACCGGGAGATAGTTTTTG
TTATCGTAGCTCGGTAAAGGATTTGCATAAAGATCGTCTTGG
TAGTCGGCCTTCTTTGCGAGATAGACCCGAGTTACGACAGCA
GTCTTGTCCGTCAGATAGGTAAAGTGAGTATATGGGTGCAGT""".strip().split("\n")))
