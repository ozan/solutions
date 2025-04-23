import itertools as it


def ba6b(data):
    sp = [int(x) for x in data[1:-1].split()]
    xs, ys = it.chain([0], sp), it.chain(sp, [len(sp) + 1])
    return sum(x + 1 != y for x, y in zip(xs, ys))


sample = "(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)"
# print(ba6b(sample))

with open('/Users/oz/Downloads/rosalind_ba6b.txt') as f:
    print(ba6b(f.read().rstrip()))
