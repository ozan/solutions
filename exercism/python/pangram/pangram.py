import string

alphabet = set(string.ascii_lowercase)


def is_pangram(word):
    return set(word.lower()).issuperset(alphabet)
