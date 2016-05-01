from itertools import groupby, starmap


DIGIT = {}  # sentinal value indicating something is a digit


def encode(str):
    return ''.join(starmap(_encoding, groupby(str, _identity)))


def decode(str):
    return ''.join(_gen_decoding(groupby(str, _num_or_char)))


def _identity(x):
    return x


def _num_or_char(ch):
    return DIGIT if ord(ch) in range(0x30, 0x3a) else ch


def _encoding(sym, repeats):
    n_repeats = len(list(repeats))
    return sym if n_repeats == 1 else '{}{}'.format(n_repeats, sym)


def _gen_decoding(token_groups):
    while True:
        try:
            key, group = next(token_groups)
            if key is DIGIT:
                n_repeats = int(''.join(group))
                sym, _ = next(token_groups)
            else:
                sym = key
                n_repeats = 1
            yield sym * n_repeats
        except StopIteration:
            return
