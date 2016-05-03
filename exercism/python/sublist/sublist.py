from collections import deque


SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 0


def check_lists(xs, ys):
    if len(xs) == len(ys):
        return EQUAL * int(xs == ys)

    smaller, larger = (xs, ys) if len(xs) < len(ys) else (ys, xs)
    q = deque([], len(smaller))

    for x in larger:
        q.append(x)
        if list(q) == smaller:
            return SUBLIST if smaller == xs else SUPERLIST

    return UNEQUAL
