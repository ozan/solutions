from collections import defaultdict
from itertools import chain, zip_longest, repeat
from string import digits, ascii_lowercase

rev = ''.join(reversed(ascii_lowercase))
cipher = defaultdict(lambda: None, zip(ascii_lowercase + digits, rev + digits))


def encode(chars):
    return spaced(5, convert(chars))


def decode(chars):
    return ''.join(convert(chars))


def convert(chars):
    return filter(identity, (cipher[ch] for ch in chars.lower()))


def spaced(n, it):
    chunks = map(''.join, zip_longest(*([it] * n), fillvalue=''))
    return ''.join(chain(*zip(chunks, repeat(' ')))).rstrip()


identity = lambda x: x
