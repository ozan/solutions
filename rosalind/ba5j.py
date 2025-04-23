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


GAP_OPEN = -11
GAP_EXT = -1
DEL, INS, SUB = 'DIS'


def ba5j(s, t, subf=blosum62, debug=False):
    """
    This time, store a tuple in each entry of the memo, (a, b, c)
    where a = best overall for that subproblem, as before
          b = best score where the latest operation was a deletion
          c = best score where the latest operation was an insertion

    As before, a deletion is from s, ie s is longer. An insertion into s would
    form t, ie t is longer.
    """
    memo = [
        ((0 if i == 0 else GAP_OPEN + GAP_EXT * (i-1), [(INS, j) for j in range(i)]),
         (float('-inf'), []),
         (0 if i == 0 else GAP_OPEN + GAP_EXT * (i-1), [(INS, j) for j in range(i)]))
        for i in range(len(t) + 1)]

    for si, sx in enumerate(s):
        del_entry = (GAP_OPEN + GAP_EXT * (si), [(DEL, i) for i in range(si + 1)])
        if debug: print(memo)
        memp, memo[0] = memo[0], (del_entry, del_entry, (float('-inf'), []))
        for ti, tx in enumerate(t):
            memp, memo[ti+1] = memo[ti+1], (
                max((subf(sx, tx) + cost, ops + [(SUB, si)]) for cost, ops in memp),
                max((memo[ti+1][0][0] + GAP_OPEN, memo[ti+1][0][1] + [(DEL, ti+1)]),
                    (memo[ti+1][1][0] + GAP_EXT,  memo[ti+1][1][1] + [(DEL, ti+1)]),
                    (memo[ti+1][2][0] + GAP_OPEN, memo[ti+1][2][1] + [(DEL, ti+1)])),
                max((memo[ti  ][0][0] + GAP_OPEN, memo[ti  ][0][1] + [(INS, ti)]),
                    (memo[ti  ][1][0] + GAP_OPEN, memo[ti  ][1][1] + [(INS, ti)]),
                    (memo[ti  ][2][0] + GAP_EXT,  memo[ti  ][2][1] + [(INS, ti)]))
            )

    if debug: print(memo)

    best_score, best = max(memo[-1])
    # TODO avoid O(n**2), ideally avoid hack with ins_n++ etc
    out_s, out_t, out_sub = list(s), list(t), [' '] * len(s)
    ins_n, del_n, sub_n = 0, 0, 0
    for op, i in best:
        if op == SUB:
            out_sub.insert(i + ins_n, '*')
            sub_n += 1
        if op == INS:
            out_s.insert(i + del_n, '-')
            out_sub.append(' ')
            ins_n += 1
        if op == DEL:
            out_t.insert(i + del_n, '-')
            del_n += 1

    print(best_score)
    print(''.join(out_s))
    print(''.join(out_t))
    # print(''.join(out_sub))


sample = """PRTEINS
PRTWPSEIN""".split('\n')

ba5j(*sample)


with open('/Users/oz/Downloads/rosalind_ba5j.txt') as f:
    print(ba5j(*f.read().rstrip().split('\n')))
