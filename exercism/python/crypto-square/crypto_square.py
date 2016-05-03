from itertools import zip_longest
from math import ceil, sqrt


def encode(phrase):
    cleaned = [ch for ch in phrase.lower() if ch.isalnum()]
    width = ceil(sqrt(len(cleaned)))
    rows = chunk(width, cleaned)
    return ' '.join(''.join(col) for col in transpose(rows))


def chunk(n, xs):
    return zip_longest(*[iter(xs)] * n, fillvalue='')


def transpose(matrix):
    return zip(*matrix)
