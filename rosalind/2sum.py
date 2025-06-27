import io


def two_sum(xs):
    idxs = {}
    for i, x in enumerate(xs):
        try:
            return f'{idxs[-x] + 1} {i + 1}'
        except KeyError:
            idxs[x] = i
    return -1


def run(f):
    k, n = map(int, f.readline().split())
    for line in f:
        out = two_sum(map(int, line.split(' ')))
        print(out)


sample = io.StringIO("""4 5
2 -3 4 10 5
8 2 4 -2 -8
-5 2 3 2 -4
5 4 -5 6 8""")

# run(sample)

with open('/Users/oz/Downloads/rosalind_2sum.txt') as f: run(f)
