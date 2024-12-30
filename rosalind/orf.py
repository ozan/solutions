import itertools as it

import utils as u

trans = dict(zip('ACGT', 'ACGU'))


def orf(s):
    sf = [trans[x] for x in s]
    sr = [trans[x] for x in u.reverse_comp(s)]

    out = set()
    for st in (sf, sr):
        for offset in range(3):
            xs = it.islice(st, offset, None)
            xs = it.batched(xs, n=3)
            xs = map(''.join, xs)
            xs = filter(lambda x: len(x) == 3, xs)
            xs = list(map(u.translate, xs))

            for i in range(len(xs)):
                if xs[i] == 'M':
                    for j in range(i, len(xs)):
                        if xs[j] is None:
                            out.add(''.join(xs[i:j]))
                            break

    for s in out:
        print(s)


sample = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

# orf(sample)

with open('/Users/oz/Downloads/rosalind_orf (1).txt') as f:
    orf(next(u.scan_fasta(f))[1])
