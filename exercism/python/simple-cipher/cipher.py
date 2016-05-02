from functools import partial
from itertools import cycle, starmap
from random import randint

orda = ord('a')
ordz = ord('z')


def shift(x, y):
    return chr(orda + (ord(x) + ord(y) - 2 * orda) % 26)


def unshift(x, y):
    return chr(orda + (ord(x) - ord(y)) % 26)


def random_key(length):
    return ''.join(chr(randint(orda, ordz)) for _ in range(100))


class Cipher(object):
    def __init__(self, key=None):
        if key and any(not ch.isalpha() or not ch.islower() for ch in key):
            raise ValueError

        self.key = key or random_key(length=100)
        self.encode = partial(self._translate, shift)
        self.decode = partial(self._translate, unshift)

    def _translate(self, f, given):
        chars = (ch.lower() for ch in given if ch.isalpha())
        return ''.join(starmap(f, zip(chars, cycle(self.key))))


class Caesar(Cipher):
    def __init__(self):
        super(Caesar, self).__init__('d')
