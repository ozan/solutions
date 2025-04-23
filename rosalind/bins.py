
def binsearch(xs, k):
    """
    binary search the sorted array xs for the location of the key k,
    returning -1 if not found

    invariant: if k exists, it must be in the range [a, b)
    """
    a, b = 0, len(xs)
    while a < b:
        mid = (a + b) // 2  # no overflow risk due to PyNumber
        piv = xs[mid]
        if piv == k:
            return mid + 1  # returning 1-indexed due to problem spec
        if piv > k:  # k if exists must be in [a, piv)
            b = mid
        else:  # k if exists must be in [piv + 1, b)
            a = mid + 1
    return -1


def bins(data):
    xs = [int(x) for x in data[2].split()]
    ks = [int(k) for k in data[3].split()]
    out = [binsearch(xs, k) for k in ks]
    print(' '.join(str(o) for o in out))


sample = """5
6
10 20 30 40 50
40 10 35 15 40 20""".split('\n')


with open('/Users/oz/Downloads/rosalind_bins.txt') as f:
    bins(f.read().split('\n'))


