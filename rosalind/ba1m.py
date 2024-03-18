
nucs = dict(zip(range(4), 'ACGT'))


def f(index, k):
    return ''.join(nucs[(index >> i) % 4] for i in reversed(range(0, k*2, 2)))


print(f(5541, 11))
