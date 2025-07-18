"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def divisor_sum(n):
    total = 1
    for k in range(2, int(n**0.5)+1):
        div, mod = divmod(n, k)
        if mod == 0:
            total += (k if div == k else div + k)
    return total


assert divisor_sum(4) == 3
assert divisor_sum(28) == 28
assert divisor_sum(12) == 16


def find_abundants(a, b):
    return set(n for n in range(a, b+1) if divisor_sum(n) > n)


assert find_abundants(2, 50) == {12, 18, 20, 24, 30, 36, 40, 42, 48}


def abundant_sum(abundants, n):
    return any(n - k in abundants for k in abundants)


def nonabundant_sums(limit):
    abundants = find_abundants(12, limit)
    return sum(n for n in range(1, limit) if not abundant_sum(abundants, n))


print(nonabundant_sums(28213))
