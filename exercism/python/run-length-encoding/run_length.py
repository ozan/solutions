from functools import reduce


def encode(given):
    def reducer(memo, ch):
        encoding, count, prior = memo
        if prior is None or ch == prior:
            return encoding, count + 1, ch
        next_enc = '{}{}'.format(count if count > 1 else '', prior)
        return encoding + next_enc, 1, ch

    return reduce(reducer, list(given) + [{}], ('', 0, None))[0]


def decode(given):
    def reducer(memo, ch):
        decoding, n = memo
        if ch.isdigit():
            return decoding, n * 10 + int(ch)
        return decoding + (n or 1) * ch, 0

    return reduce(reducer, given, ('', 0))[0]
