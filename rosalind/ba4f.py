# import utils as u

from collections import Counter

from ba4c import ba4c as cyclo


def ba4f(pep, spec):
    observed = Counter(int(x) for x in spec.split(' '))
    expected = Counter(cyclo(pep))
    return sum(v for k, v in (observed & expected).items())


print(ba4f('NQEL', '0 99 113 114 128 227 257 299 355 356 370 371 484'))



with open('/Users/oz/Downloads/rosalind_ba4f (2).txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    pep, spec = f.read().rstrip().split('\n')
    print(ba4f(pep, spec))
