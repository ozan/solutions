
vals = dict(zip('ACGT', range(4)))


def f(text):
    total = 0
    for c in text:
        total <<= 2
        total += vals[c]
    return total


print(f('GTTACTTTCACCAACCCGCCAACATCTACT'))
