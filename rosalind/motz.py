import utils as u
from functools import cache


match = dict(zip('AUCG', 'UAGC'))


@cache
def motz(s, start=0, end=None):
    # Num imperfect matchings in interval [start, end)
    if end is None:
        end = len(s)

    if start == end:
        return 1

    tot = motz(s, start + 1, end)  # first, consider omiting start
    exp = match[s[start]]
    for i in range(start + 1, end):  # then, try every match
        if s[i] == exp:
            tot += motz(s, start + 1, i) * motz(s, i+1, end)
    return tot % 1000000


sample = """>Rosalind_57
AUAU"""

print(motz(next(u.scan_fasta(sample))[1]))

with open('/Users/oz/Downloads/rosalind_motz (1).txt') as f:
    print(motz(next(u.scan_fasta(f))[1]))
