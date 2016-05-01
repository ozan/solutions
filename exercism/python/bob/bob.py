import re

R_YELL = 'Whoa, chill out!'
R_QUESTION = 'Sure.'
R_SILENCE = 'Fine. Be that way!'
R_DEFAULT = 'Whatever.'


def has_alpha(what):
    return len(re.findall('[a-zA-Z]', what)) > 0


def yelling(what):
    return what == what.upper() and has_alpha(what)


def question(what):
    trimmed = what.strip()
    return trimmed and trimmed[-1] == '?'


def silence(what):
    return what.strip() == ''


def hey(what):
    return (
        silence(what) and R_SILENCE or
        yelling(what) and R_YELL or
        question(what) and R_QUESTION or
        R_DEFAULT
    )
