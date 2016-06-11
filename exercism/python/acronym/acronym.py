

def abbreviate(phrase):
    return ''.join(caps(phrase))


def caps(phrase):
    a = ' '
    for b in phrase:
        if case_change(a, b) or alpha_change(a, b):
            yield b.upper()
        a = b


def case_change(a, b):
    return a.islower() and b.isupper()


def alpha_change(a, b):
    return b.isalpha() and not a.isalpha()
