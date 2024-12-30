import utils as u

blosum_names = 'A C D E F G H I K L M N P Q R S T V W Y'.split(' ')

blosum_vals = [list(map(int, l.split())) for l in """
 4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
 0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
-2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
-1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
-2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
 0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
-2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
-1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
-1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
-1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
-1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
-2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
-1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
-1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
-1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
 1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
 0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
 0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
-3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
-2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7
""".strip().rstrip().split('\n')]


def blosum62(a, b):
    return blosum_vals[blosum_names.index(a)][blosum_names.index(b)]


GAP = -5


def gcon(s, t, subf=blosum62):
    memo = [
        (GAP * (i > 0), 0, -GAP * (i > 0))
        for i in range(len(t) + 1)]

    for si, sx in enumerate(s):
        memp, memo[0] = memo[0], (GAP, -GAP, 0)
        # if s == 'AAAAA': print(memo)
        for ti, tx in enumerate(t):
            memp, memo[ti + 1] = memo[ti + 1], max(
                (subf(sx, tx) + memp[0], 0, 0),  # substitution
                (GAP + memo[ti+1][0] + memo[ti+1][1], -GAP, 0),  # deletion
                (GAP + memo[ti][0] + memo[ti][2], 0, -GAP)  # insertion
            )

    # if s == 'AAAAA': print(memo)

    return memo[-1][0]


sample = """>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY"""

assert gcon(*[x for _, x in u.scan_fasta(sample)]) == 13

cases = (
    ('A', '', -5),
    ('AAAA', '', -5),
    ('', 'A', -5),
    ('', 'AAAA', -5),
    ('A', 'B', -9),
    ('X', 'A', -10),
    ('X', 'AAAAAAA', -10),
    ('XX', 'AAAAA', -10),
    ('AA', 'XX', -10),
    ('AAAAA', 'AABAA', -9),
    ('..AA........', '.........BB.', -10),
)


def subs(a, b):
    if a == 'X' or b == 'X':  # X is expensive, better to ins + del
        return -11
    if a == b:
        return 0
    return -9  # otherwise better to sub


for s, t, exp in cases:
    actual = gcon(s, t, subf=subs)
    if actual != exp:
        print(f'Expected f("{s}", "{t}") to be {exp} but was {actual}')

print('ok')

# with open('/Users/oz/Downloads/rosalind_gcon (1).txt') as f:
   # s, t = [x for _, x in u.scan_fasta(f)]
   # print(gcon(s, t))
