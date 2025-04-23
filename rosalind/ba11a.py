from collections import defaultdict
from pprint import pprint

masses = [
    ('A', 71),
    ('C', 103),
    ('D', 115),
    ('E', 129),
    ('F', 147),
    ('G', 57),
    ('H', 137),
    ('I', 113),
    ('K', 128),
    ('L', 113),
    ('M', 131),
    ('N', 114),
    ('P', 97),
    ('Q', 128),
    ('R', 156),
    ('S', 87),
    ('T', 101),
    ('V', 99),
    ('W', 186),
    ('Y', 163)]


def find_close(x):
    for aa, mass in masses:
        if abs(x - mass) < 0.001:
            return aa


def ba11a(spectrum):
    spectrum.append(0)
    spectrum.sort()
    g = defaultdict(list)
    for i, x in enumerate(spectrum):
        for j in range(i+1, len(spectrum)):
            y = spectrum[j]
            if y == x:
                continue
            match = find_close(y - x)  # TODO can do exact match for int
            if match:
                g[x].append((y, match))

    pprint(g)
    for source, dests in g.items():
        for dest, aa in dests:
            print(f'{source}->{dest}:{aa}')

    return


sample = list(map(int, '57 71 154 185 301 332 415 429 486'.split()))

# ba11a(sample)

with open('/Users/oz/Downloads/rosalind_ba11a (1).txt') as f:
    print(ba11a(list(map(int, f.read().split()))))
