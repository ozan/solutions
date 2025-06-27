import io


def par(xs):
    """Partition with Lomuto scheme, using first item as pivot (to match test case)"""
    pivot = xs[0]
    i = 1

    for j in range(1, len(xs)):
        if xs[j] < pivot:
            xs[i], xs[j] = xs[j], xs[i]
            i += 1

    xs[i-1], xs[0] = xs[0], xs[i-1]


def run(f):
    f.readline()  # n
    xs = [int(x) for x in f.readline().split()]
    par(xs)
    print(' '.join(map(str, xs)))


sample = io.StringIO("""9
7 2 5 6 1 3 9 4 8""")

# run(sample)

with open('/Users/oz/Downloads/rosalind_par (1).txt') as f: run(f)
