
from itertools import islice


def primes():
    known = set()
    candidate = 2
    while True:
        for p in known:
            if candidate % p == 0:
                break
        else:
            yield candidate
            known.add(candidate)
        candidate += 1


def nth_prime(n):
    return next(islice(primes(), n - 1, None))


identity = lambda x: x
