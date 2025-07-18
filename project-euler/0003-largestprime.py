"""

Finding the largest prime factor of a large number

Idea: consider a candidate factor k, starting at 2. If it is not a factor, iterate.
If it does factor n, it *must* be a prime factor, otherwise we would have already
identified a factor of k. Continue with n / k.
"""


def factors(n):
    k = 2
    while k < n:
        q, r = divmod(n, k)
        if r == 0:
            yield k
            n = q
        else:
            k += 1
    yield k


for k in factors(600851475143):
    print(k)
