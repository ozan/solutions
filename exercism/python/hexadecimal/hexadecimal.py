
DIGITS = '0123456789abcdef'


def hexa(hx):
    hx = hx.lower()
    if any(d not in set(DIGITS) for d in hx):
        raise ValueError

    return sum(DIGITS.index(d) << (4 * i) for i, d in enumerate(reversed(hx)))
