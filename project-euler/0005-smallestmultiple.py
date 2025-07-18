"""
What is the smallest positive number that is evenly divisible by all numbers from 1 to 20?

Note this can be done with pen and paper: find prime factors of first 20 numbers, and include
in the product only the highest power of each factor.

More interesting to find a programatic approach for higher N
"""

import math


def smallest_multiple(n):
    """
    Consider all primes p <= n. Find the highest power k of p such that p^k <= n. The product
    of all these p^ks will be our answer. Note that k will be 1 for all p < sqrt(n).
    """

    ks = [0] + [1] * (n)

    for p in range(2, int(math.sqrt(n)) + 1):
        if ks[p] == 0: continue  # skip non-primes... we'll find these as we go
        ks[p] = math.floor(math.log(n) / math.log(p))
        for i in range(p+p, n + 1, p): ks[i] = 0  # skip multiples of p
    return math.prod(p ** k for p, k in enumerate(ks))


assert smallest_multiple(10) == 2520
assert smallest_multiple(20) == 232792560

# starting to create very large products, enough to exceed python limit
print(smallest_multiple(5000))
