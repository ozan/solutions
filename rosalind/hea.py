import io


def hea(xs):
    for i, x in enumerate(xs):
        while i > 0:
            ii = (i-1) // 2
            if x > xs[ii]:
                xs[ii], xs[i] = x, xs[ii]
                i = ii
            else:
                break
    return xs


def run(f):
    _ = int(f.readline())
    xs = [int(x) for x in f.readline().split()]
    out = hea(xs)
    print(' '.join(str(x) for x in out))


sample = io.StringIO("""5
1 3 5 7 2""")

# run(sample)

with open('/Users/oz/Downloads/rosalind_hea.txt') as f: run(f)
