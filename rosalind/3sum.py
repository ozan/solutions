import io


def three_sum(xs):
    ps = {}

    for q, x in enumerate(xs):
        for r in range(q + 1, len(xs)):
            y = xs[r]
            try:
                p = ps[-(x + y)]
                return f'{p+1} {q+1} {r+1}'  # output expects 1-index
            except KeyError:
                pass
        ps[x] = q

    return -1


def run(f):
    k, n = map(int, f.readline().split())
    for line in f:
        out = three_sum([int(x) for x in line.split(' ')])
        print(out)


sample = io.StringIO("""4 5
2 -3 4 10 5
8 -6 4 -2 -8
-5 2 3 2 -4
2 4 -5 6 8""")

# run(sample)

with open('/Users/oz/Downloads/rosalind_3sum.txt') as f: run(f)
