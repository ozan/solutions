

def detect_anagrams(x, phrase):
    return [
        y for y in phrase
        if _key(y) == _key(x) and x.lower() != y.lower()
    ]


def _key(word):
    return ''.join(sorted(word.lower()))
