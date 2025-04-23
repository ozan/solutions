from collections import Counter

masses = dict([
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
    ('Y', 163.06333)])


def spec(prot):
    """
    Return the complete spectrum, ie the weights of every prefix and suffix
    """
    out = []
    w_pref, w_suff = 0, 0
    for i in range(len(prot)):
        w_pref += masses[prot[i]]
        w_suff += masses[prot[-(i+1)]]
        out.append(w_pref)
        out.append(w_suff)
    out.pop()  # avoid double-counting the full pref == the full suff
    return out


def prsm(data):
    n = int(data[0])
    proteins = data[1:n+1]
    R = [float(x) for x in data[n+1:]]

    best = []
    for prot in proteins:
        S = spec(prot)
        mink_diff = [round(abs(x1 - x2), 6) for x1 in R for x2 in S]
        counts = Counter(mink_diff)
        n, x = max((v, k) for k, v in counts.items())
        best.append((n, prot))

    n, prot = max(best)
    print(n)
    print(prot)


sample = """4
GSDMQS
VWICN
IASWMQS
PVSMGAD
445.17838
115.02694
186.07931
314.13789
317.1198
215.09061""".split('\n')

# prsm(sample)

with open('/Users/oz/Downloads/rosalind_prsm.txt') as f:
    print(prsm(f.read().rstrip().split('\n')))
