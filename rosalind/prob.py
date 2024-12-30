import math
# import utils as u


def prob(s, A):
    gc = sum(c in 'GC' for c in s)
    at = len(s) - gc
    return [gc * math.log10(a/2) + at * math.log10((1-a) / 2) for a in A]



s = 'CTAGTTTTTGTGTTAACGGTACTAACCAGCCTGATGCCGAATCGAGGGCCACATCTAACCCTGCTAGCTGGATGTCGATACGCGAGCTTATTGA'
A = map(float, '0.079 0.125 0.192 0.290 0.335 0.396 0.416 0.492 0.579 0.635 0.661 0.740 0.809 0.846 0.915'.split(' '))

print(' '.join(map(str, prob(s, A))))
