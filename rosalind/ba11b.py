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


mass_for_aa = dict(masses)


def find_close(x):
    for aa, mass in masses:
        if abs(x - mass) < 0.001:
            return aa


def ideal_spectrum(prot):
    out = []
    w_pref, w_suff = 0, 0
    for i in range(len(prot)):
        w_pref += mass_for_aa[prot[i]]
        w_suff += mass_for_aa[prot[-(i+1)]]
        out.append(w_pref)
        out.append(w_suff)
    out.pop()  # don't double count full peptide
    out.sort()
    return out


def ba11b(spectrum):
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

    q = [(0, [])]

    pprint(g)

    while q:
        v, path = q.pop()
        
        if v == spectrum[-1]:
            if ideal_spectrum(path) == spectrum[1:]:
                return ''.join(path)

        for vv, letter in g[v]:
            q.append((vv, path + [letter]))


sample = list(map(int, '57 71 154 185 301 332 415 429 486'.split()))

print(ba11b(sample))

with open('/Users/oz/Downloads/rosalind_ba11b.txt') as f:
    print(ba11b(list(map(int, f.read().split()))))
