from collections import deque


def slices(xs, n):
    if n == 0 or n > len(xs):
        raise ValueError

    q = deque(xs, n)
    return [
        list(q) for i, x in enumerate(xs)
        if q.append(int(x)) or i >= n - 1
    ]
