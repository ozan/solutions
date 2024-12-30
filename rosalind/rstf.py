# import utils as u

import functools

product = functools.partial(functools.reduce, lambda a, b: a * b)


def rstf(n, gc, s):
    pn = dict(zip('GCAT', [gc/2, gc/2, (1-gc)/2, (1-gc)/2]))
    pns = 1 - product(pn[x] for x in s)
    return 1 - pns ** n


print(rstf(90000, 0.6, 'ATAGCCGA'))
print(rstf(81654, 0.478673, 'GGTGTTGCT'))

# with open('/Users/oz/Downloads/rosalind_orf (1).txt') as f:
    # orf(next(u.scan_fasta(f))[1])
