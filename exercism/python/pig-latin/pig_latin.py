from itertools import chain, repeat


CONSONANT = 'c'
VOWEL = 'v'
RULES = tuple(chain(
    zip(('ch', 'qu', 'squ', 'thr', 'th', 'sch'), repeat(CONSONANT)),
    zip(('yt', 'xr'), repeat(VOWEL)),
    zip('bcdfghjklmnpqrstvwxyz', repeat(CONSONANT)),
    zip('aeiou', repeat(VOWEL))
))


def translate(phrase):
    return ' '.join(map(translate_word, phrase.split(' ')))


def translate_word(word):
    head, tail = sound_split(word)
    return '{}{}ay'.format(head, tail)


def sound_split(word):
    for stem, case in RULES:
        head, tail = word[:len(stem)], word[len(stem):]
        if head == stem:
            return (head, tail) if case == VOWEL else (tail, head)
