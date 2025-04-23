"""
Note: this one is a bit of a mess, but mostly because I was trying to
figure out what exactly they were looking for. Next one should be
both more meaningful and much cleaner.
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


def ba5k(v, w, subf=blosum62, debug=False):
    """
    Plan: first just build out the full matrix to see what the scores
    are in the middle. Then, confirm same matrix can be built out from
    both ends. Findally, find that edge without building out the matrix
    """
    memo = [(i * GAP, '>') for i in range(len(w) + 1)]

    matrix = [memo]

    for vi, vx in enumerate(v):
        nxt = [((vi + 1) * GAP, 'v')]
        for wi, wx in enumerate(w):
            best = max(
                (blosum62(vx, wx) + memo[wi][0], '\\'),
                (GAP + memo[wi+1][0], 'v'),
                (GAP + nxt[wi][0], '>'))
            nxt.append(best)
        memo = nxt
        matrix.append(nxt)

    # print('\n'.join('\t'.join(f'{x[1]} {x[0]}' for x in row) for row in matrix))

    # print()

    # ok now try just the top half
    mid = len(w) // 2
    memo = [(i * GAP, '>') for i in range(len(v) + 1)]

    matrix_top = [memo]
    
    # print(v[:mid], w)

    for wi, wx in enumerate(w[:mid-1]):
        nxt = [((wi + 1) * GAP, 'v')]
        for vi, vx in enumerate(v):
            best = max(
                (blosum62(vx, wx) + memo[vi][0], '\\'),
                (GAP + memo[vi+1][0], 'v'),
                (GAP + nxt[vi][0], '>'))
            nxt.append(best)
        memo = nxt
        matrix_top.append(nxt)
    
    # print()
    # print('\n'.join('\t'.join(f'{x[1]} {x[0]}' for x in row) for row in matrix_top))

    # ok, now just the bottom matrix, which will be built with the same logic,
    # just from the rear of each string

    memo = [(i * GAP, '>') for i in range(len(v) + 1)]

    matrix_bottom = [memo]
    
    # print()
    # print(v[mid:][::-1], w[::-1])
    for wi, wx in enumerate(reversed(w[mid:])):
        nxt = [((wi + 1) * GAP, 'v')]
        for vi, vx in enumerate(reversed(v)):
            best = max(
                (blosum62(vx, wx) + memo[vi][0], '\\'),
                (GAP + memo[vi+1][0], 'v'),
                (GAP + nxt[vi][0], '>'))
            nxt.append(best)
        memo = nxt
        matrix_bottom.append(nxt)

    # print()
    # print('\n'.join('\t'.join(f'{x[1]} {x[0]}' for x in row[::-1]) for row in matrix_bottom[::-1]))

    # ok now consider the best possible transitions between each
    # and hopefully end up at 3 -> 4 with a sub, giving us (mid, 3) (mid+1, 4)
    # as our result
    # print()
    top = matrix_top[-1]
    bottom = matrix_bottom[-1][::-1]
    # print('\t'.join(str(x[0]) for x in top))

    # sub_scores = []
    # del_scores = []
    # blosums = []
    best_score, best_ij = None, None
    for i, x in enumerate(top):
        score = x[0] + bottom[i][0] + GAP
        # del_scores.append(score)
        if best_score is None or score > best_score:
            best_score = score
            best_ij = (i, i)
        if i < len(bottom) - 1:
            score = x[0] + bottom[i+1][0] + blosum62(w[mid-1], v[i])
            if score > best_score:
                best_score = score
                best_ij = (i, i+1)
                # sub_scores.append(sub_score)
    # print('\t'.join(str(x[0]) for x in bottom))

    # print('sub scores')
    # print('\t'.join(str(x) for x in sub_scores))

    # print('blosums')
    # print('\t'.join(str(x) for x in blosums))

    # print('del_scores')
    # print('\t'.join(str(x) for x in del_scores))

    besti, bestj = best_ij
    print((besti+1, mid), (bestj+1, mid+1))


sample = """PLEASANTLY
MEASNLY""".split('\n')

ba5k(*sample)


with open('/Users/oz/Downloads/rosalind_ba5k (3).txt') as f:
    a, b = f.read().rstrip().split('\n')
    print(len(a), len(b), len(a) // 2, len(b) // 2)
    print(ba5k(a, b))
