from collections import deque
from functools import reduce
from itertools import islice


def largest_product(xs, n):
    if n == 0:
        return 1
    if not 0 < n <= len(xs):
        raise ValueError

    q = deque([], n)
    subs = ((q.append(int(x)) or q) for x in xs)
    return max(map(product, islice(subs, n - 1, None)), default=0)


def product(xs):
    return reduce(lambda x, y: x * y, list(xs), 1)
