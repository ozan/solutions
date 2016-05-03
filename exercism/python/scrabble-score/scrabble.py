

tiles = {
    1: 'AEIOULNRST',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'
}
SCORES = {letter: score for score in tiles for letter in tiles[score]}


def score(word):
    if any(not ch.isalpha() for ch in word):
        return 0
    return sum(SCORES[ch] for ch in word.upper())
