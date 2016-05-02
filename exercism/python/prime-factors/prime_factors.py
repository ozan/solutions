from itertools import count


def prime_factors(n, k=2):
    if n <= 1:
        return []

    k = next(filter(lambda x: n % x == 0, count(k)))
    return [k] + prime_factors(n // k, k)
