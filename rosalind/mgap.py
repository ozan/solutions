import utils as u


m = 5
d = -5
g = -1


def mgap(s, t):
    """
    Weird question, but total # gaps is total string length - common subsequence
    length in both strings
    """
    memo = [0] * (len(t) + 1)
    for si, sx in enumerate(s):
        nxt = [0]
        for ti, tx in enumerate(t):
            nxt.append(memo[ti] + 1 if sx == tx else max(memo[ti+1], nxt[ti]))
        memo = nxt

    return len(s) + len(t) - 2 * memo[-1]


sample = """>Rosalind_92
AACGTA
>Rosalind_47
ACACCTA"""

print(mgap(*[x for _, x in u.scan_fasta(sample)]))


with open('/Users/oz/Downloads/rosalind_mgap (1).txt') as f:
    s, t = [x for _, x in u.scan_fasta(f)]
    print(mgap(s, t))
