"""
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math


def lexperm(n, digits):
    out = []
    prms = math.factorial(len(digits))
    while digits:
        prms /= len(digits)
        div = math.ceil(n / prms) - 1
        out.append(digits.pop(div))
        n -= div * prms
    return ''.join(out)


assert lexperm(4, list('012')) == '120'
print(lexperm(1000000, list('0123456789')))
