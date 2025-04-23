bam50_names = 'A C D E F G H I K L M N P Q R S T V W Y'.split(' ')

bam50_vals = [list(map(int, l.split())) for l in """
 2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
-2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
 0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
 0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
-3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
 1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
-1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
-1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
-1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
-2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
-1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
 0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
 1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
 0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
-2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
 1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
 1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
 0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
-6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
-3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10
""".strip().rstrip().split('\n')]


def bam50(a, b):
    return bam50_vals[bam50_names.index(a)][bam50_names.index(b)]


INDEL = -5


def ba5f(s, t, subf=bam50, debug=False):
    memo = [[(INDEL * i, (0, i)) for i in range(len(t) + 1)]]
    end_score = None
    end_loc = None

    for si, sx in enumerate(s):
        nxt = [(INDEL * (si + 1), (si + 1, 0))]
        memo_row = memo[-1]
        for ti, tx in enumerate(t):
            best = max(
                (0, (-1, -1)),
                (bam50(sx, tx) + memo_row[ti][0], (si, ti)),
                (INDEL + memo_row[ti+1][0], (si, ti+1)),
                (INDEL + nxt[ti][0], (si+1, ti)))
            if end_score is None or best[0] > end_score:
                end_score = best[0]
                end_loc = (si, ti)
            nxt.append(best)
        memo.append(nxt)

    pi, pj = end_loc
    print(end_score)
    # steps = [end_loc]
    steps = [(None, None), end_loc]
    # TODO how to handle very end?
    while pi > 0 and pj > 0:
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


sample = """MEANLY
PENALTY"""

sample = """CAAGGAACTCAATCGTCGAGTCCACGGGGGGCAGAACACGCTATATTTAATCTTGATGAGGAACGCAAATAACCATGGTTGCACGTGAGGATTTTCTTTAGTGAGTTGGGTTGCTTGGTAACTTATCCACTGCTATCTTAAGGGGGTTACTTCGGGATGAACGGCTTATGACAATCACAGTGAGGTCCGTCCCGGCCGATATGAGTTCTATGTTTTAACAGCGTCACCAGTGTCACGTACGGGGCCACCTCAGGCCCTGACCAGGGAATAGAGCGATTTGGGGACTTTCCCGGGTGATGTCTACCAGGAAGTTCGGTACCACTGACTTTGAATAATACTGTCAAAGGGGCTGCACCTTCCCGAGTTCGTCGTCATTACACAGCGCATATATTACACGTTAAGCCGTTTATCCGCATGTTATGCCAATTCGCGTCTTGCCAGGTGCCAACGAGCCTGATAAAGCAGTGGGTAGCGCCGGCACAGTATGTAGCAAGTTCCCCGCCGCGCGTTGAAAGCGTTACGTACAGGCGGCTAAGCGACGTTAAAATTGTCGCTTGCCTAACCCATCTCCCTGACACGGAACATAGCGAATAGTAGTCAACGGAGTTATGGTACAAAGCCTGAAAGCGACCTCAGACGAAGGGTCTGCCCGCAGGACGTGGGCTCTAATCCTCGGGGGCCTCGCCTACGTAGCACATCCCCAATAGCACTAAGAAGATGTGAACGAAACGCCGCTGTCGGATTCCAATTCTGAAATAGATAGTACCGGGTCCGAGGCGATGGAGGGTGGCGAAACCCCCATTTACGCATAGCGGTAACTTGGTCCCGGACTATTTATCAGTTGGTACCCTCGGCCCTGGTGGATGTGTTTTACTGGAATGATGTATAGACATCGCCTAC
CGCCCTACCTTTCGTGCCTATCAAAGTCGGTAGGCGCATTCCGAGCTCCGACTAGCGAGAAAACCAGCACAATGAAGTGCGCCTCCATATGTTAGTATACGGGTTGCCTCAGCTTTGGGCGGGCCTAAGGGCGGGATGAACGGCTTATTCCTGTGCAGTAGGTCGGTCCCGCCGATATGAGTTCTGGAGGTATTTAACAGCAGGGGCACGTGCACTGGGCCGCCTCAGGGGCTCACCATGACCAGGACATCGAGCGGGATCTCAACTTTGGGGACTTTCCCGGGTGATGTCTGCCACTGATGTTCGGTACCAGCGACCATACTGTGAAAAGGGGCTGCAAACATTATCTTCCCGAGTTGTCATTACACAGCATATATTACGCCGAAACTACGTCTCCGCATGTTTAACTCGCGTTTTGCCAGAGCCTAGCTAGGTTATAAAGGCGGCACAGTTTGTTCTAAAACCCGCCCTCGCCGAAGCGTTACGTACAGCGGCAAAGCGACGTTGAAATTGTCGATTGCCTATGGTTGACGCGGAACATAGCGTGACATAGTAGTGATACTCCAAGCGTGAAAGTGACCTAGCGGGTCTGAGCAGGACGTTGGCTCGAGCACGTGCAAGTTAGGGTTGTTCATGCCTGGGGAAAATAGTTTACGATTATTCGGCCATGCGTTAGCGTGCTGCTGTCCAGGCGCAGGGGCTTTCGAAAGTTTACTCCGTGATTGCGATTACCCTGAAGCCAGAGCTACACTTCCACGGACCGAACGCCGAATATCCGGATCCTGCCTGGCTTTCCGGCTTCGGAACTGAGAGAGGATCCGAGAGATAGCTGGTAA"""

# ba5f(*sample.split('\n'))

with open('/Users/oz/Downloads/rosalind_ba5f (1).txt') as f:
    print(ba5f(*f.read().rstrip().split('\n')))
