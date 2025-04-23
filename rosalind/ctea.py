import utils as u


def ctea(s, t):
    memo = [(i, 1) for i in range(len(t) + 1)]

    for si, sx in enumerate(s):
        memp, memo[0] = memo[0], (si+1, 1)
        for ti, tx in enumerate(t):
            opts = [
                (memp[0] + (tx != sx), memp[1]),
                (memo[ti+1][0] + 1, memo[ti+1][1]),
                (memo[ti][0] + 1, memo[ti][1])
            ]
            best = min(opts)[0]
            ways = sum(x[1] for x in opts if x[0] == best)
            memp, memo[ti+1] = memo[ti+1], (best, ways)

    score, ways = memo[-1]

    # print(score, ways)
    print(ways % 134217727)


sample = """>Rosalind_78
PLEASANTLY
>Rosalind_33
MEANLY"""


ctea(*[x for _, x in u.scan_fasta(sample)])

with open('/Users/oz/Downloads/rosalind_ctea.txt') as f:
    s, t = [x for _, x in u.scan_fasta(f)]
    ctea(s, t)
