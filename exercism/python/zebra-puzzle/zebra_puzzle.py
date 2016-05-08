from collections import namedtuple, deque
from itertools import permutations

# consider each house to be a 5-tuple of one of each of if we were to generate
# all possibilities and check against constraints we would have pow(5!, 5) =
# 24,883,200,000 so too many to brute force. instead do a depth first search..
# depth first since we need to get to a root anyway so want to prune subtrees
# ASAP

House = namedtuple('House', ['nationality', 'color', 'drink', 'pet', 'smokes'])

options = (
    ('Norwegian', 'Englishman', 'Spaniard', 'Ukranian', 'Japanese'),
    ('green', 'red', 'yellow', 'orange', 'ivory'),
    ('tea', 'coffee', 'orange juice', 'water', 'milk'),
    ('horse', 'fox', 'dog', 'snails', 'zebra'),
    ('Old Gold', 'Kools', 'Lucky Strike', 'Chesterfields', 'Parliaments')
)


def solution():
    initial_iters = [permutations(opts, 5) for opts in options]
    initial_conf = [House(*attrs) for attrs in zip(*(next(it) for it in iters))]

    # TODO use stack instead of queue; requires tee
    queue = deque([(initial_iters, initial_conf)])

    while queue:
        for constraint in constraints:
            # if any constraint violated, return



solution()
