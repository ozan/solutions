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


INDEL = -5


def ba5e(s, t, subf=blosum62, debug=False):
    memo = [[(INDEL * i, (0, i)) for i in range(len(t) + 1)]]

    for si, sx in enumerate(s):
        nxt = [(INDEL * (si + 1), (si + 1, 0))]
        memo_row = memo[-1]
        for ti, tx in enumerate(t):
            nxt.append(max(
                (blosum62(sx, tx) + memo_row[ti][0], (si, ti)),
                (INDEL + memo_row[ti+1][0], (si, ti+1)),
                (INDEL + nxt[ti][0], (si+1, ti))))
        memo.append(nxt)

    score, (pi, pj) = memo[-1][-1]
    print(score)
    steps = [(len(s), len(t)), (pi, pj)]
    while pi != 0 and pj != 0:
        nxt = memo[pi][pj]
        _, (pi, pj) = nxt
        steps.append((pi, pj))

    pi, pj, si, ti = 0, 0, 0, 0
    sa, ta = [], []
    while steps:
        ni, nj = steps.pop()
        di, dj = ni - pi, nj - pj
        if di == 1 and dj == 1:
            sa.append(s[si])
            ta.append(t[ti])
            si += 1
            ti += 1
        elif di == 1:
            sa.append(s[si])
            ta.append('-')
            si += 1
        elif dj == 1:
            sa.append('-')
            ta.append(t[ti])
            ti += 1
        else:
            print(f'Invalid step: {di}, {dj}')
        pi, pj = ni, nj

    print(''.join(sa))
    print(''.join(ta))


sample = """PLEASANTLY
MEANLY"""

ba5e(*sample.split('\n'))

with open('/Users/oz/Downloads/rosalind_ba5e.txt') as f:
    print(ba5e(*f.read().rstrip().split('\n')))
