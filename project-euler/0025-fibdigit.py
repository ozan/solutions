"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Python's big number representation is hugely helpful for us here
"""


def fibdigit(digits):
    target = 10 ** (digits - 1)
    a, b, i = 0, 1, 1
    while b < target:
        a, b, i = b, a + b, i + 1
    return i


print(fibdigit(1000))
