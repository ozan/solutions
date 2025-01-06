from collections import Counter

masses = dict(zip(
    'GASPVTCILNDKQEMHFRYW',
    [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]))


def count_exp(peptide):
    pref = [0]
    for p in peptide:
        pref.append(pref[-1] + masses[p])

    spec = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide) + 1):
            spec.append(pref[j] - pref[i])

    return Counter(spec)


def ba4l(peptides, observed, n):
    c = Counter(int(x) for x in observed.split(' '))
    n = int(n)

    scores = [(sum((count_exp(p) & c).values()), p) for p in peptides.split(' ')]

    scores.sort(reverse=True)

    nval = scores[n-1][0]
    i = n - 1
    while scores[i][0] == nval:
        i += 1
    out = [p for _, p in scores[:i]]
    print(' '.join(out))
    return out


sample = """LAST ALST TLLT TQAS
0 71 87 101 113 158 184 188 259 271 372
2""".split('\n')

ba4l(*sample)

with open('/Users/oz/Downloads/rosalind_ba4l.txt') as f:
    ba4l(*f.read().rstrip().split('\n'))
