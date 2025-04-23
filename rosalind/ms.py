

def mergesort(xs):
    """
    Recursively sort xs in range [start, end)

    TODO avoid slicing
    """
    if len(xs) <= 1:
        return xs

    mid = len(xs) // 2  # no overflow risk due to PyNumber
    left, right = mergesort(xs[:mid]), mergesort(xs[mid:])

    out, li, ri = [], 0, 0
    while li < len(left) or ri < len(right):
        if li == len(left):
            out.append(right[ri])
            ri += 1
        elif ri == len(right) or left[li] < right[ri]:
            out.append(left[li])
            li += 1
        else:
            out.append(right[ri])
            ri += 1
    return out


def ms(data):
    xs = [int(x) for x in data[1].split()]
    out = mergesort(xs)
    print(' '.join(str(x) for x in out))


sample = """10
20 19 35 -18 17 -20 20 1 4 4""".split('\n')

ms(sample)

with open('/Users/oz/Downloads/rosalind_ms.txt') as f:
    ms(f.read().rstrip().split('\n'))


