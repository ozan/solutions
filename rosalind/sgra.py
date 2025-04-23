from collections import defaultdict
from pprint import pprint

masses = [
    ('A', 71.03711),
    ('C', 103.00919),
    ('D', 115.02694),
    ('E', 129.04259),
    ('F', 147.06841),
    ('G', 57.02146),
    ('H', 137.05891),
    ('I', 113.08406),
    ('K', 128.09496),
    ('L', 113.08406),
    ('M', 131.04049),
    ('N', 114.04293),
    ('P', 97.05276),
    ('Q', 128.05858),
    ('R', 156.10111),
    ('S', 87.03203),
    ('T', 101.04768),
    ('V', 99.06841),
    ('W', 186.07931),
    ('Y', 163.06333)]


def find_close(x):
    for aa, mass in masses:
        if abs(x - mass) < 0.001:
            return aa


def sgra(data):
    L = [float(x) for x in data]
    L.sort()
    g = defaultdict(list)
    for i, x in enumerate(L):
        for j in range(i+1, len(L)):
            y = L[j]
            match = find_close(y - x)
            if match:
                g[x].append((y, match))

    start = sorted(list(g.keys()))[0]
    q = [(start, [])]
    best_path = []
    while q:
        v, path = q.pop()
        if len(path) > len(best_path):
            best_path = path
        for v_next, aa in g[v]:
            q.append((v_next, path + [aa]))

    return ''.join(best_path)


sample = """3524.8542
3623.5245
3710.9335
3841.974
3929.00603
3970.0326
4026.05879
4057.0646
4083.08025""".split('\n')


print(sgra(sample))

with open('/Users/oz/Downloads/rosalind_sgra.txt') as f:
    print(sgra(f.read().rstrip().split('\n')))
