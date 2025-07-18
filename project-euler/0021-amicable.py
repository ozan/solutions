"""
Evaluate the sum of all the amicable numbers under 10000
"""


def divisor_sum(n):
    ds = 1
    for k in range(2, int(n**0.5)+1):
        div, mod = divmod(n, k)
        if mod == 0:
            ds += (k + div if k != div else k)
    return ds


assert divisor_sum(220) == 284
assert divisor_sum(284) == 220


def amicable_sum(limit):
    total = 0
    for a in range(limit):
        b = divisor_sum(a)
        if b < a and divisor_sum(b) == a:
            total += (a + b)
    return total


print(amicable_sum(10000))
