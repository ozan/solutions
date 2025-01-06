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


def gcon(s, t, subf=blosum62, debug=False):
    """
    This time, store a tuple in each entry of the memo, (a, b, c)
    where a = best overall for that subproblem, as before
          b = best score where the latest operation was a deletion
          c = best score where the latest operation was an insertion

    As before, a deletion is from s, ie s is longer. An insertion into s would
    form t, ie t is longer.
    """
    if len(s) < len(t):
        s, t = t, s

    memo = [
        (GAP * (i > 0), float('-inf'), GAP * (i > 0))
        for i in range(len(t) + 1)]

    for si, sx in enumerate(s):
        memp, memo[0] = memo[0], (GAP, GAP, float('-inf'))
        for ti, tx in enumerate(t):
            memp, memo[ti+1] = memo[ti+1], (
                max(subf(sx, tx) + x for x in memp),
                max(memo[ti+1][0] + GAP, memo[ti+1][1], memo[ti+1][2] + GAP),
                max(memo[ti][0] + GAP, memo[ti][1] + GAP, memo[ti][2])
            )

    return max(memo[-1])


sample = """>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY"""

assert gcon(*[x for _, x in u.scan_fasta(sample)], debug=True) == 13


with open('/Users/oz/Downloads/rosalind_gcon (2).txt') as f:
    s, t = [x for _, x in u.scan_fasta(f)]
    print(gcon(s, t))
