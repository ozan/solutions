"""
What is the value of the first triangle number to have over five hundred divisors?

This could just be brute forced, but we can also use an existing table of primes as well
as the property that the number of dividisors of n can be determined by the exponents of its
prime factors, ie if n = p1^k1 * p2^k2 * p3^k3 ... then the number of divisors is
(k1 + 1) * (k2 + 1) * (k3 + 1) ...
"""


def sieve(limit):
    candidates = list(range(limit))
    candidates[1] = 0
    for p in range(2, limit):
        if candidates[p] == 0:  # already zeroed => not prime
            continue
        for i in range(2*p, limit, p):
            candidates[i] = 0  # zero out all multiples of the prime
    return [c for c in candidates if c]


PRIMES = sieve(100000)


def divisors(n):
    total = 1
    pi = 0

    while n > 1:
        p = PRIMES[pi]
        k = 0
        while n > 1:
            div, mod = divmod(n, p)
            if mod == 0:
                k += 1
                n = div
            else:
                break
        if k > 0:
            total *= (k + 1)
        pi += 1

    return total


def triangular_divisors(goal):
    n, candidate = 1, 1

    while divisors(candidate) <= goal:
        n += 1
        candidate += n

    return candidate


assert triangular_divisors(5) == 28
print(triangular_divisors(500))
