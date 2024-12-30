from collections import Counter
from math import factorial as fact

import utils as u

sample = """>Rosalind_92
AUGCUUC"""


def mmch(s):
    counter = Counter(s)
    n1, k1, n2, k2 = [counter[x] for x in 'GCAU']
    if n1 < k1:
        n1, k1 = k1, n1
    if n2 < k2:
        n2, k2 = k2, n2

    return fact(n1) * fact(n2) // (fact(n1 - k1) * fact(n2 - k2))


print(mmch('AGUUUGGUCAUAGUAAAGUUCUAAGUGCUCUUGGCACAUGAACCACUAAGCACCAUCUGGGGGGUCGGUCUCGUAAUAACUCCUUCGGU'))

print(mmch('AUGCUUC'))

# with open('/Users/oz/Downloads/rosalind_mmch.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # print(mmch(s, t))
    # s = next(u.scan_fasta(f))[1]
