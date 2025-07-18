

def collatz_lengths(limit):
    """
    For now, return a dict mapping range(n) to lengths from each
    """
    lengths = {1: 1}

    best = (1, 1)  # length, start

    def inner(n):
        try:
            return lengths[n]
        except KeyError:
            pass

        if n % 2 == 0:
            nn = n // 2
        else:
            nn = 3 * n + 1

        lengths[n] = inner(nn) + 1
        return lengths[n]

    for n in range(2, limit):
        best = max(best, (inner(n), n))

    return best


print(collatz_lengths(1000000))
