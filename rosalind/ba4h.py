# import utils as u
from collections import Counter


def ba4h(spectrum):
    c = Counter()
    for xi, x in enumerate(spectrum):
        for yi in range(xi + 1, len(spectrum)):
            y = spectrum[yi]
            diff = y - x if y >= x else x - y
            if diff == 0:
                continue
            c[diff] += 1

    desc = sorted(c.items(), key=lambda x: x[1], reverse=True)
    out = []
    for val, count in desc:
        for _ in range(count):
            out.append(val)

    return out



# print(' '.join(str(x) for x in ba4h(sample)))


with open('/Users/oz/Downloads/rosalind_ba4h (1).txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    spectrum = [int(x) for x in f.read().strip().split()]
    print(' '.join(str(x) for x in ba4h(spectrum)))
