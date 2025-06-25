
sample = """cat dog elephant ostrich mouse rabbit robot
01xxx00
x00xx11
x11xx00
111x00x""".split('\n')


def qrt(labels, rows):
    results = set()
    for row in rows:
        A = []
        B = []
        for i, x in enumerate(row):
            if x == '0':
                A.append(i)
            elif x == '1':
                B.append(i)

        if len(A) < 2 or len(B) < 2:
            continue

        # produce a quartet for each unique pair in each
        # in practice better to use itertools, but this is more fun:
        for ai in range(0, len(A) - 1):
            for aj in range(ai+1, len(A)):
                for bi in range(0, len(B) - 1):
                    for bj in range(bi+1, len(B)):
                        res = [(A[ai], A[aj]), (B[bi], B[bj])]
                        res.sort()  # avoid duplicates of A, B; B, A with canonical order
                        results.add(tuple(res))

    for aa, bb in results:
        a1, a2 = aa
        b1, b2 = bb
        print(f'{{{labels[a1]}, {labels[a2]}}} {{{labels[b1]}, {labels[b2]}}}')


#qrt(sample[0].split(), sample[1:])
with open('/Users/oz/Downloads/rosalind_qrt (3).txt') as f:
    lines = f.read().rstrip().split('\n')
    qrt(lines[0].split(), lines[1:])
