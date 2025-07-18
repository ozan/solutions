"""
Find the sum of all the primes below two million

Since we know the bounds, we can use Eratosthenes' sieve
"""


def sieve(limit):
    candidates = list(range(limit))
    candidates[1] = 0
    for p in range(2, limit):
        if candidates[p] == 0:  # already zeroed => not prime
            continue
        for i in range(2*p, limit, p):
            candidates[i] = 0  # zero out all multiples of the prime
    return sum(candidates)


assert sieve(10) == 17
print(sieve(2000000))
