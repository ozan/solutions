import io


def qs(xs, lo, hi):
    if lo >= hi:
        return

    pivot = xs[lo]

    i, lt, gt = lo, lo, hi
    while i <= gt:
        if xs[i] < pivot:
            xs[lt], xs[i] = xs[i], xs[lt]
            lt += 1
        elif xs[i] > pivot:
            xs[gt], xs[i] = xs[i], xs[gt]
            gt -= 1
        else:
            i += 1

    qs(xs, lo, lt-1)
    qs(xs, gt+1, hi)


def run(f):
    f.readline()  # n
    xs = [int(x) for x in f.readline().split()]
    qs(xs, 0, len(xs) - 1)
    print(' '.join(map(str, xs)))


sample = io.StringIO("""7
5 -2 4 7 8 -10 11""")

# run(sample)

with open('/Users/oz/Downloads/rosalind_qs.txt') as f: run(f)
