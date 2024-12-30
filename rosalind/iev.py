
probs = (1, 1, 1, 0.75, 0.5, 0)


def iev(*args):
    return 2 * sum(a * p for a, p in zip(args, probs))


print(iev(*map(int, "1 0 0 1 0 1".split(" "))))
print(iev(*map(int, "19010 17195 16363 17880 19958 16466".split(" "))))
