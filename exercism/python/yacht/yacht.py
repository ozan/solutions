from collections import Counter


YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    counts = Counter(dice)

    if category == YACHT:
        return 50 if len(counts) == 1 else 0

    if category == FULL_HOUSE:
        return sum(dice) if set(counts.values()) == {2, 3} else 0

    if category == FOUR_OF_A_KIND:
        if len(counts) == 1:
            return 4 * dice[0]
        inverse = {counts[x]: x for x in counts}
        return 4 * inverse[4] if set(counts.values()) == {4, 1} else 0

    if category == LITTLE_STRAIGHT:
        return 30 if set(dice) == {1, 2, 3, 4, 5} else 0

    if category == BIG_STRAIGHT:
        return 30 if set(dice) == {2, 3, 4, 5, 6} else 0

    if category == CHOICE:
        return sum(dice)

    return category * (counts.get(category) or 0)
