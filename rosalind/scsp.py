#  import utils as u
from functools import cache


@cache
def scsp_rec(s, t):
    if len(s) == 0:
        return t
    if len(t) == 0:
        return s

    s0, t0, s_rest, t_rest = s[0], t[0], s[1:], t[1:]
    return min(
        s0 + scsp_rec(s_rest, t_rest if t0 == s0 else t),
        t0 + scsp_rec(s_rest if t0 == s0 else s, t_rest),
        key=len
    )


def scsp(s, t):
    if len(s) < len(t):
        s, t = t, s

    memo = [t[:i] for i in range(len(t) + 1)]

    for si, sx in enumerate(s):
        mp, memo[0] = memo[0], s[:si + 1]
        for ti, tx in enumerate(t):
            mp, memo[ti+1] = memo[ti+1], (
                mp + sx if sx == tx else
                memo[ti+1] + sx if len(memo[ti+1]) < len(memo[ti]) else
                memo[ti] + tx)

    return memo[-1]


print(scsp('ATCTGAT', 'TGCATA'))

print(scsp('GAGCTCGGAAGGGGAGGGAGGAGAAGCGAATTCGTAAAACTCTGGGACTTTGGCCTCGGTGTCAATAATCGGTCTAAACCACGGCGTTAA', 'AGACCGACCAGCGGTCGGGGACCATTACACGGAACAGCTTTAGCCACGCTGGTCCTTGTTACCCTCGGGGCCAGGCCTCAAGATCTGTAACAGGA'))

# with open('/Users/oz/Downloads/rosalind_motz (1).txt') as f:
#    print(motz(next(u.scan_fasta(f))[1]))
