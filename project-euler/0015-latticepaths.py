import math


def paths(n):
    return math.comb(n + n, n)


assert paths(2) == 6
print(paths(20))
