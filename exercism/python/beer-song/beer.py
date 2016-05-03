

template = """{n_cap} bottle{pl_n} of beer on the wall, {n} bottle{pl_n} of beer.
{bridge}, {m} bottle{pl_m} of beer on the wall.
"""

bridge = (
    'Go to the store and buy some more',
    'Take it down and pass it around',
    'Take one down and pass it around'
)


def song(high, low=0):
    return '\n'.join(verse(n) for n in range(high, low-1, -1)) + '\n'


def verse(n):
    cap = lambda xs: xs[min(n, len(xs) - 1)]
    rules = {
        'n': ('no more', n),
        'n_cap': ('No more', n),
        'm': (99, 'no more', n - 1),
        'pl_n': ('s', '', 's'),
        'pl_m': ('s', 's', '', 's'),
        'bridge': bridge
    }
    return template.format(**{k: cap(rules[k]) for k in rules})
