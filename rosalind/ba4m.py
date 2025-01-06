
def ba4m(deltas):
    """
    Given a list of all pairwise distances between points, return a set of points
    that would generate those distances.

    Idea:

    - Start with 0 and the largest delta, which must be in the result
    - For every other delta, in descending order, consider possible locations
        that construct that difference from an existing point
    - DFS this decision tree, pruning impossible results as we go

    TODO:

    - Do we need to change our logic for these negative deltas?
    - How do we ensure that repeated deltas appear multiple times?
    """
    options = [{0, deltas.pop()}]

    while deltas:
        d = deltas.pop()
        nxt = []
        for op in options:
            for other in op:
                for candidate in (other + d, other - d):
                    if candidate == d or candidate in deltas or candidate in op:
                        nxt.append(op | {candidate})
        options = nxt

    return list(sorted(options))



print(ba4m([0, 0, 0, 2, 2, 3, 3, 4, 5, 6, 7, 8, 10]))

