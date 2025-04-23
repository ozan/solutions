from collections import defaultdict
from pprint import pprint

masses = [
    ('A', 71),
    ('C', 103),
    ('D', 115),
    ('E', 129),
    ('F', 147),
    ('G', 57),
    ('H', 137),
    ('I', 113),
    ('K', 128),
    ('L', 113),
    ('M', 131),
    ('N', 114),
    ('P', 97),
    ('Q', 128),
    ('R', 156),
    ('S', 87),
    ('T', 101),
    ('V', 99),
    ('W', 186),
    ('Y', 163),
    ('X', 4),
    ('Z', 5)]


mass_for_aa = dict(masses)
aa_for_mass = dict((v, k) for k, v in masses)


def ba11d(P):
    tot = -1
    out = []
    for i, x in enumerate(P):
        if x == '0':
            continue
        diff = i - tot
        out.append(aa_for_mass[diff])
        tot = i
    return ''.join(out)


sample = '0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 1'.split()

print(ba11d(sample))

with open('/Users/oz/Downloads/rosalind_ba11d.txt') as f:
    print(ba11d(f.read().rstrip().split()))
