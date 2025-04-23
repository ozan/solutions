

def ba5g(xs, ys):
    memo = list(range(len(ys) + 1))

    for xi, x in enumerate(xs):
        mp, memo[0] = memo[0], xi + 1
        for yi, y in enumerate(ys):
            mp, memo[yi+1] = memo[yi+1], min((x != y) + mp, 1 + memo[yi+1], 1 + memo[yi])

    return memo[-1]


sample = """PLEASANTLY
MEANLY""".split('\n')

print(ba5g(*sample))

with open('/Users/oz/Downloads/rosalind_ba5g.txt') as f:
    print(ba5g(*f.read().rstrip().split('\n')))
