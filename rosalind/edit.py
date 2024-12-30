import utils as u


def edit(s, t):
    memo, memp = list(range(len(t) + 1)), 0

    for si, sx in enumerate(s):
        memp, memo[0] = memo[0], si + 1
        for ti, tx in enumerate(t):
            memp, memo[ti + 1] = memo[ti + 1], min(
                (tx != sx) + memp,  # substitution
                1 + memo[ti+1],  # deletion
                1 + memo[ti])  # insertion

    return memo[-1]


sample = """>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY"""

print(edit(*[x for _, x in u.scan_fasta(sample)]))


with open('/Users/oz/Downloads/rosalind_edit.txt') as f:
    s, t = [x for _, x in u.scan_fasta(f)]
    print(edit(s, t))
