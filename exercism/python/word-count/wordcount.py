from collections import Counter
from functools import reduce


valid_ranges = (
    (0x0030, 0x003a),  # digits
    (0x0061, 0x007b),  # lowercase Latin
    (0x0400, 0x0500)  # Cyrillic
)


def word_count(phrase):
    return Counter(tokenize(phrase.lower()))


def in_range(memo, char):
    if any(ord(char) in range(*rng) for rng in valid_ranges):
        memo['current'].append(char)
    elif memo['current']:
        memo['tokens'].append(''.join(memo['current']))
        memo['current'] = []
    return memo


def tokenize(phrase):
    memo = {'current': [], 'tokens': []}
    return reduce(in_range, phrase + ' ', memo)['tokens']
