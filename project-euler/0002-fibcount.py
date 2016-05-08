#!/usr/bin/env python

from itertools import ifilter, takewhile


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def even(n):
    return n % 2 == 0


def less_than(n):
    return lambda a: a < n


print sum(takewhile(less_than(4e6), ifilter(even, fib())))
