from functools import cache
import math


@cache
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


def choose(n, k):
    return fact(n) / (fact(k) * fact(n-k))


def indc(n):
    two_n = n << 1
    total = math.log10(1 << (two_n))

    out = []
    running = 0
    for k in range(two_n):
        running += choose(two_n, k)
        out.append(math.log10(running) - total)

    print(' '.join(f'{x:.4f}' for x in reversed(out)))


indc(45)


