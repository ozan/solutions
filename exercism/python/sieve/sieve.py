from itertools import islice
import math


def sieve(upto):
    primes = [None, None] + list(range(2, upto + 1))
    p = 2
    while True:
        primes[2*p::p] = [None] * math.floor((upto - p) / p)
        try:
            p = next(filter(identity, islice(primes, p + 1, None)))
        except StopIteration:
            return list(filter(identity, primes))


identity = lambda x: x
