import math


def prob(N, m, i):
    """Chance of exactly i dominant alleles in next gen of population N, given m in current"""
    p = m / (N + N)
    return math.comb(N + N, i) * p**i * (1-p)**(N+N-i)


def wfmd(N, m, g, k):
    xs = [1.0 if i == m else 0.0 for i in range(N+N+1)]

    for _ in range(g):  # loop once for each subsequent generation
        xs = [
            sum(xs[i] * prob(N, i, j) for i in range(N+N+1))
            for j in range(N+N+1)
        ]

    # at least k copies of recessive allele
    return f'{sum(xs[:-k]):.3f}'


assert wfmd(4, 6, 2, 1) == '0.772'
print(wfmd(5, 9, 5, 5))
