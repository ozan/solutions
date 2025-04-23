"""
TODO need to try and make sense of this on my own terms, e.g. simplify
the final edge finding step... then fix
"""
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


def alignment(s, t):
    memo = [(i * GAP, '>') for i in range(len(s) + 1)]
    for ti, tx in enumerate(t):
        mp, memo[0] = memo[0], ((ti + 1) * GAP, (ti, 0))
        for si, sx in enumerate(s):
            mp, memo[si+1] = memo[si+1], max(
                (blosum62(sx, tx) + mp[0], (ti, si)),
                (GAP + memo[si+1][0], (ti, si+1)),
                (GAP + memo[si][0], (ti+1, si)))
    return memo


def find_edge(v, w):
    mid = len(w) // 2

    top = alignment(v, w[:mid-1])
    bottom = alignment(v[::-1], w[mid:][::-1])[::-1]

    # best_score, best_ij = None, None
    best = None
    for i, x in enumerate(top):
        score = x[0] + bottom[i][0] + GAP
        if best is None:
            best = (score, i, i)
        best = max(best, (score, i, i))
        if i < len(bottom) - 1:
            score = x[0] + bottom[i+1][0] + blosum62(w[mid-1], v[i])
            best = max(best, (score, i, i+1))

    score, i, j = best
    return (i+1, mid), (j+1, mid+1)


def ba5l(v, w):
    a, b = find_edge(v, w)

    print(a, b)

    print(find_edge(v[:a[0]], w[:a[1]]))
    print(find_edge(v[b[0]:], w[b[1]:]))


sample = """PLEASANTLY
MEASNLY""".split('\n')

# assert ba5l(*sample) == ((4, 3), (5, 4))


print('ok')
