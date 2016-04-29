#!/usr/bin/env python

"""
Combinatorial solution: O(width + height) time, O(1) space.

Note:

*   Runs much faster in Python3.X than Python2.X because the former uses
    a divide and conquer factorial implementation whereas the latter
    uses the naive iterative implementation.
*   There are much faster implementations of `choose`, or we could trade
    off some space for time by pre-computing factorials.

"""

from math import factorial


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def unique_paths(width, height):
    return choose(width + height, width)


assert unique_paths(3, 4) == 35


"""
Dynamic programming solution: O(width * height) time, O(width) space.
"""


def ones(n):
    return [1 for _ in range(n)]


def next_row(prior, _):
    return reduce(lambda xs, y: xs + [xs[-1] + y], prior, [0])[1:]


def unique_paths_dp(width, height):
    return reduce(next_row, ones(height), ones(width + 1))[-1]


assert unique_paths_dp(3, 4) == 35
