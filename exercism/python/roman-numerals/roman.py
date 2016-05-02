from bisect import bisect

PARTS = (
    (1, 'I'),
    (4, 'IV'),
    (5, 'V'),
    (9, 'IX'),
    (10, 'X'),
    (40, 'XL'),
    (49, 'IL'),
    (50, 'L'),
    (90, 'XC'),
    (100, 'C'),
    (400, 'CD'),
    (500, 'D'),
    (900, 'CM'),
    (1000, 'M')
)


def numeral(arabic):
    if arabic == 0:
        return ''

    part, sym = PARTS[bisect(PARTS, (arabic, 'Z')) - 1]
    return '{}{}'.format(sym, numeral(arabic - part))
