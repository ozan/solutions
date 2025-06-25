import io


def hs(xs):
    # first, max heapify xs
    for i, x in enumerate(xs):
        while i > 0:
            ii = (i-1) // 2
            if xs[i] > xs[ii]:
                xs[ii], xs[i] = xs[i], xs[ii]
                i = ii
            else:
                break

    # xs[:si] is heap, xs[si:] is sorted
    si = len(xs) - 1
    while si > 0:
        xs[0], xs[si] = xs[si], xs[0]
        si -= 1
        i = 0
        while i < si:
            y = xs[i*2+1] if i*2+1 < si else None
            z = xs[i*2+2] if i*2+2 < si else None

            if y is None: break
            if (z is None or y > z) and xs[i] < y:  # TODO cleanup
                xs[i], xs[i*2+1] = xs[i*2+1], xs[i]
                i = i * 2 + 1
            elif z is not None and xs[i] < z:
                xs[i], xs[i*2+2] = xs[i*2+2], xs[i]
                i = i * 2 + 2
            else:
                break

    # repeatedly place top of max heap at the
    # then, repeatedly take the top of the heap to the beginning of the sorted part
    return xs


def run(f):
    _ = int(f.readline())
    xs = [int(x) for x in f.readline().split()]
    out = hs(xs)
    print(' '.join(str(x) for x in out))


sample = io.StringIO("""9
2 6 7 1 3 5 4 8 9""")

# run(sample)

with open('/Users/oz/Downloads/rosalind_hs.txt') as f: run(f)
