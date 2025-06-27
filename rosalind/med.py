import io


def par3(xs, lo, hi):
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
    return lt, gt


def med(k, xs):
    """
    Repeatedly 3-way partition xs, returning lt, gt boundaries
    Once k is between the two, we know we have found it.
    Otherwise, recursively partition the left or right
    """
    lo, hi = 0, len(xs) - 1

    while lo <= hi:
        lt, gt = par3(xs, lo, hi)

        if lt <= (k - 1) <= gt:
            return xs[k - 1]

        if lt < (k - 1):
            lo = gt + 1

        elif gt > (k - 1):
            hi = lt - 1


def run(f):
    f.readline()  # n
    xs = [int(x) for x in f.readline().split()]
    k = int(f.readline())
    print(med(k, xs))


sample = io.StringIO("""11
2 36 5 21 8 13 11 20 5 4 1
8""")

# run(sample)

with open('/Users/oz/Downloads/rosalind_med.txt') as f: run(f)
