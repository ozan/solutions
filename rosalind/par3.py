import io


def par3(xs):
    pivot = xs[0]

    i, lt, gt = 0, 0, len(xs) - 1
    while i <= gt:
        if xs[i] < pivot:
            xs[lt], xs[i] = xs[i], xs[lt]
            lt += 1
        elif xs[i] > pivot:
            xs[gt], xs[i] = xs[i], xs[gt]
            gt -= 1
        else:
            i += 1


def run(f):
    f.readline()  # n
    xs = [int(x) for x in f.readline().split()]
    par3(xs)
    print(' '.join(map(str, xs)))


sample = io.StringIO("""9
4 5 6 4 1 2 5 7 4""")

# run(sample)

with open('/Users/oz/Downloads/rosalind_par3 (1).txt') as f: run(f)
