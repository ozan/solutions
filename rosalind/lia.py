import math


def lia(k, n):
    m = 1 << k
    p = 0.25

    return 1 - sum(math.comb(m, i) * (p ** i) * (1 - p) ** (m - i) for i in range(n))


print(lia(6, 19))
