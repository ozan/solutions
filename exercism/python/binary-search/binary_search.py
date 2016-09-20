
def binary_search(xs, n):
    a, b = 0, len(xs) - 1
    while (a <= b):
        probe = (a + b) / 2
        candidate = xs[probe]
        if candidate == n:
            return probe
        if candidate < n:
            a = probe + 1
        else:
            b = probe - 1
    raise ValueError
