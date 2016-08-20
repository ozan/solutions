from itertools import cycle


def encode(xs, height):
    positions = pattern(height, len(xs))
    return ''.join(xs[i] for _, i in positions)


def decode(xs, height):
    positions = pattern(height, len(xs))
    rectified = sorted(enumerate(positions), key=lambda t: t[1][1])
    return ''.join(xs[i] for i, _ in rectified)


def pattern(height, width):
    n = 2 * (height - 1)
    positions = (min(x, n - x) for x in cycle(range(n)))
    return sorted(zip(positions, range(width)))
