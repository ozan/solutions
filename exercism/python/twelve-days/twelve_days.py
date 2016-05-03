ORDINALS = 'first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth'.split(' ')
GIFTS = (
    'a Partridge in a Pear Tree.',
    'two Turtle Doves',
    'three French Hens',
    'four Calling Birds',
    'five Gold Rings',
    'six Geese-a-Laying',
    'seven Swans-a-Swimming',
    'eight Maids-a-Milking',
    'nine Ladies Dancing',
    'ten Lords-a-Leaping',
    'eleven Pipers Piping',
    'twelve Drummers Drumming',
)
PRELUDE = 'On the {} day of Christmas my true love gave to me, '


def sing():
    return verses(1, 12)


def verse(n):
    return PRELUDE.format(ORDINALS[n-1]) + human_join(GIFTS[n-1::-1]) + '\n'


def verses(m, n):
    return '\n'.join(verse(x) for x in range(m, n + 1)) + '\n'


def human_join(xs):
    if len(xs) == 1: return xs[0]
    if len(xs) == 2: return ', and '.join(xs)
    return human_join([', '.join(xs[:-1]), xs[-1]])
