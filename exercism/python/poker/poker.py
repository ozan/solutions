from collections import Counter
from functools import reduce

RANK_VAL = dict(zip('23456789TJQKA', range(2, 15)))
VAL_RANK = {v: k for k, v in RANK_VAL.items()}


first = lambda t: t[0]
second = lambda t: t[1]


def of_kind(n):
    def inner(h):
        counts = {v: k for k, v in Counter(rank for rank, _ in h).items()}
        return counts.get(n, 0)
    return inner

highest = lambda h: sorted(rank for rank, _ in h)[-1]
pair = of_kind(2)


def two_pair(h):
    pairs = sorted(
        rank for rank, count in Counter(rank for rank, _ in h).items()
        if count == 2
    )
    return len(pairs) == 2 and pairs[1] * 14 + pairs[0]


def straight(h):
    ranks = list(sorted(rank for rank, _ in h))
    return len(set(ranks)) == 5 and ranks[-1] - ranks[0] == 4 and ranks[-1]

triple = of_kind(3)
flush = lambda h: len(set(suit for _, suit in h)) == 1 and highest(h)
full = lambda h: triple(h) and pair(h) and 13 * triple(h) + pair(h)
square = of_kind(4)
straight_flush = lambda h: straight(h) and flush(h) and highest(h)

CASES = (
    highest,
    pair,
    two_pair,
    triple,
    straight,
    flush,
    full,
    square,
    straight_flush
)


def poker(hands):
    memo = {'winners': [], 'max_score': 0}
    return reduce(maximize, hands, memo)['winners']


def score(hand):
    hand_scores = (f(hand) for f in CASES)
    overall_scores = (i * 1e3 + hs for i, hs in enumerate(hand_scores) if hs)
    return int(max(overall_scores))


def maximize(memo, hand):
    the_score = score(parse(hand))
    if the_score == memo['max_score']:
        memo['winners'].append(hand)
    if the_score > memo['max_score']:
        memo = {'winners': [hand], 'max_score': the_score}
    return memo


def parse(hand):
    return [(RANK_VAL[c[0]], c[1]) for c in hand]
