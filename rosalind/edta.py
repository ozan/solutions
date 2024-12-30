import utils as u

DEL, INS, SUB = 'DIS'


def edta(s, t):
    memo, memp = [[(INS, j) for j in range(i)] for i in range(len(t) + 1)], []

    for si, sx in enumerate(s):
        # memp, memo[0] = memo[0], si + 1
        memp, memo[0] = memo[0], [(DEL, i) for i in range(si + 1)]
        for ti, tx in enumerate(t):
            # TODO avoid pre-emptive construction
            memp, memo[ti + 1] = memo[ti + 1], min(
                memp + ([] if tx == sx else [(SUB, si)]),
                memo[ti+1] + [(DEL, ti+1)],
                memo[ti] + [(INS, ti)],
                key=len
            )

    best = memo[-1]

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

    print(len(best))
    print(''.join(out_s))
    print(''.join(out_t))
    print(''.join(out_sub))
    return len(best)


sample = """>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN"""


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


with open('/Users/oz/Downloads/rosalind_edta (2).txt') as f:
    n = 1000
    s, t = [x[:n] for _, x in u.scan_fasta(f)]
    assert edta(s, t) == edit(s, t)
