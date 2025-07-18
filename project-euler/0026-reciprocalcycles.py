"""
Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""


def cycle_length(d):
    r = 10
    seen = {}
    i = 0
    while True:
        if r == 0:
            return -1
        if r in seen:
            return i - seen[r]
        seen[r] = i
        i += 1
        r = 10 * (r % d)


assert cycle_length(2) == -1
assert cycle_length(3) == 1
assert cycle_length(7) == 6


print(max((cycle_length(d), d) for d in range(2, 1000)))
