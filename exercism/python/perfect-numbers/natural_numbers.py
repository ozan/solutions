
def is_perfect(n):
    return n == sum(factors(n))


def factors(n):
    primes = set(prime_factors(n))
    return combine(n, primes)


def combine(n, xs):
    for x, y in [(x, y) for x in xs for y in xs]:
        m = x * y
        if (m < n and m not in xs and n % m == 0):
            xs.add(m)
            xs.add(n // m)
            return combine(n, xs)
    return xs


def prime_factors(n):
    if n == 1:
        yield 1
        return
    for k in range(2, n + 1):
        if n % k == 0:
            yield k
            yield from prime_factors(n // k)
            return
