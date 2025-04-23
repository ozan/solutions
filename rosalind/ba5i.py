

INDEL = -2
MISMATCH = -2
MATCH = 1


def ba5i(s, t):
    memo = [[(INDEL * i, (0, i)) for i in range(len(t) + 1)]]
    end_score = None
    end_loc = None

    for si, sx in enumerate(s):
        nxt = [(0, (-1, -1))]  # any number of initial dels is free
        memo_row = memo[-1]
        for ti, tx in enumerate(t):
            best = max(
                ((MATCH if sx == tx else MISMATCH) + memo_row[ti][0], (si, ti)),
                (INDEL + memo_row[ti+1][0], (si, ti+1)),
                (INDEL + nxt[ti][0], (si+1, ti)))
            # can terminate whenever s is finished, but no sooner
            if si == len(s) - 1 and (end_score is None or best[0] >= end_score):
                end_score = best[0]
                end_loc = (si, ti)
            nxt.append(best)
        memo.append(nxt)

    pi, pj = end_loc
    print(end_score)
    # steps = [end_loc]
    steps = [(None, None), end_loc]
    while pi >= 0 and pj >= 0:
        nxt = memo[pi][pj]
        _, (pi, pj) = nxt
        steps.append((pi, pj))

    pi, pj, si, ti = 0, 0, 0, 0
    if steps[-1] == (-1, -1):
        steps.pop()
        pi, pj = steps[-1]
        si, ti = steps[-1]

    sa, ta = [], []
    while steps:
        ni, nj = steps.pop()
        if ni is None and nj is None:
            sa.append(s[si])
            ta.append(t[ti])
            break
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
            pass
        pi, pj = ni, nj

    print(''.join(sa))
    print(''.join(ta))


sample = """PAWHEAECHEAGAWGHEEC
HEAGAWGHEE"""

# ba5i(*sample.split('\n'))

with open('/Users/oz/Downloads/rosalind_ba5i.txt') as f:
    print(ba5i(*f.read().rstrip().split('\n')))
