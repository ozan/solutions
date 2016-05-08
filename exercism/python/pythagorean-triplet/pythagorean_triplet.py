# WIP: one test failing

from math import ceil


def triplets_in_range(mn, mx):
    results = set()
    for b in range(4 * int(ceil(mn / 4)), mx, 4):
        prims = primitive_triplets(b)
        for k in range(1, mx + 1):
            for a, b, c in prims:
                if k*a >= mn and k*c <= mx:
                    results.add((k*a, k*b, k*c))
    return results


def primitive_triplets(b):
    if b % 2 == 1:
        raise ValueError
    results = set()
    for m in range(2, b // 2 + 1):
        n = b / (2 * m)
        if m > n and (m - n) % 2 == 1 and gcd(m, n) == 1:
            a, c = int(m*m - n*n), int(m*m + n*n)
            results.add(tuple(sorted([a, b, c])))
    return results


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)


def is_triplet(sides):
    a, b, c = sorted(sides)
    return a*a + b*b == c*c
