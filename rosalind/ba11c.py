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


def ba11c(peptide):
    tot = 0
    pref_masses = set()
    for aa in peptide:
        tot += mass_for_aa[aa]
        pref_masses.add(tot)
    print(' '.join(str(1 if i in pref_masses else 0) for i in range(1, tot+1)))


sample = 'XZZXX'

print(ba11c(sample))

with open('/Users/oz/Downloads/rosalind_ba11c.txt') as f:
    print(ba11c(f.read().rstrip()))
