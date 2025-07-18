"""
Find the 10001st prime.

Since we don't really know how big it'll be, we can't use Eratosthenes' Sieve. Instead
test divisibility against known primes as we iterate up
"""


def nth_prime(n):
    primes = [3, 5, 7, 11, 13]  # don't test against 2: skip even candidates instead

    c = primes[-1] + 2  # next candidate
    while len(primes) <= n:
        for p in primes:
            if c % p == 0:
                break
        else:
            primes.append(c)
        c += 2

    return primes[n-2]


assert nth_prime(6) == 13
print(nth_prime(10001))
