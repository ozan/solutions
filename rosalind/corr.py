# from io import StringIO
from collections import defaultdict

import utils as u


def corr(dataset):
    dataset = list(dataset)
    counts = defaultdict(lambda: 0)
    for _, s in dataset:
        counts[s] += 1
        counts[''.join(u.reverse_comp(s))] += 1

    valid = {}
    singletons = []

    for _, s in dataset:
        v = counts[s]
        if v == 1:
            singletons.append(s)
        else:
            rev = ''.join(u.reverse_comp(s))
            for i in range(len(s)):
                valid[rev[:i] + '.' + rev[i+1:]] = rev
                valid[s[:i] + '.' + s[i+1:]] = s

    for s in singletons:
        for i in range(len(s)):
            k = s[:i] + '.' + s[i+1:]
            if k in valid:
                print(f'{s}->{valid[k]}')
                break


sample = """>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC
"""

# print(corr(u.scan_fasta(sample)))

with open('/Users/oz/Downloads/rosalind_corr.txt') as f:
    corr(u.scan_fasta(f))
