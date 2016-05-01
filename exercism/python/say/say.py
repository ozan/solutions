

def say(n):
    if n >= 1e12:
        raise AttributeError

    if n < 0:
        raise AttributeError

    return _say(n, '')


def _say(n, prefix):
    for part, name in PARTS:
        high, low = n // part, n % part
        if high == 0:
            continue

        tail_prefix = '-' if part < 100 else ' and '
        tail = low and _say(low, tail_prefix) or ''

        if part < 100:
            return '{}{}{}'.format(prefix, name, tail)

        head = _say(high, prefix and ' ' or '')
        return '{} {}{}'.format(head, name, tail)

    return 'zero'


PARTS = (
    (1e9, 'billion'),
    (1e6, 'million'),
    (1e3, 'thousand'),
    (100, 'hundred'),
    (90, 'ninety'),
    (80, 'eighty'),
    (70, 'seventy'),
    (60, 'sixty'),
    (50, 'fifty'),
    (40, 'forty'),
    (30, 'thirty'),
    (20, 'twenty'),
    (19, 'nineteen'),
    (18, 'eighteen'),
    (17, 'seventeen'),
    (16, 'sixteen'),
    (15, 'fifteen'),
    (14, 'fourteen'),
    (13, 'thirteen'),
    (12, 'twelve'),
    (11, 'eleven'),
    (10, 'ten'),
    (9, 'nine'),
    (8, 'eight'),
    (7, 'seven'),
    (6, 'six'),
    (5, 'five'),
    (4, 'four'),
    (3, 'three'),
    (2, 'two'),
    (1, 'one')
)
