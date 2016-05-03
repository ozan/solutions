from operator import add, sub, mul, floordiv
from functools import reduce

OPS = {'plus': add, 'minus': sub, 'divided': floordiv, 'multiplied': mul}


def calculate(question):
    initial, ops = tokenize(question)
    return reduce(lambda a, x: x[0](a, x[1]), ops, initial)


def tokenize(question):
    words = [w for w in question[8:-1].split(' ') if w != 'by']
    try:
        rest = [(OPS[op], int(n)) for op, n in zip(words[1::2], words[2::2])]
    except KeyError:
        raise ValueError
    return int(words[0]), rest
