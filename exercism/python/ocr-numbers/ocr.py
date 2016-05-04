# from itertools import chain
import string

chunk = lambda n, xs: [xs[i*n:(i+1)*n] for i in range(len(xs) // n)]
transpose = lambda xs: list(zip(*xs))


def split_digits(pic):
    individual_digits = [transpose(xs) for xs in chunk(3, transpose(pic))]
    return [tuple(''.join(x) for x in xs) for xs in individual_digits]


def compose_pic(digs):
    return [''.join(line) for line in transpose(digs)]


signatures = split_digits((
    ' _     _  _     _  _  _  _  _ ',
    '| |  | _| _||_||_ |_   ||_||_|',
    '|_|  ||_  _|  | _||_|  ||_| _|',
    '                              '
))

NUMS = dict(zip(signatures, string.digits))
PICS = dict(zip(string.digits, signatures))


def number(pic):
    if not (len(pic) == 4 and all(len(row) % 3 == 0 for row in pic)):
        raise ValueError
    return ''.join(NUMS.get(tuple(d), '?') for d in split_digits(pic))


def grid(digits):
    if not all(d.isdigit() for d in digits):
        raise ValueError
    return compose_pic(PICS[d] for d in digits)
