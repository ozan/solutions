
def abbreviate(phrase):
    return ''.join(caps(phrase))


def caps(phrase):
    yield phrase[0]
    for a, b in adjactent_pairs(phrase):
        if case_change(a, b) or alpha_change(a, b):
            yield b.upper()


def adjactent_pairs(xs):
    ys = iter(xs)
    next(ys, None)
    return zip(xs, ys)


def case_change(a, b):
    return a.islower() and b.isupper()


def alpha_change(a, b):
    return b.isalpha() and not a.isalpha()
