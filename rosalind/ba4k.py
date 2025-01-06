from collections import Counter

masses = dict(zip(
    'GASPVTCILNDKQEMHFRYW',
    [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]))


def ba4k(peptide, observed):
    pref = [0]
    for p in peptide:
        pref.append(pref[-1] + masses[p])

    spec = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide) + 1):
            spec.append(pref[j] - pref[i])

    expected_counts = Counter(spec)
    observed_counts = Counter(int(x) for x in observed.split(' '))

    return sum((expected_counts & observed_counts).values())


print(ba4k('NQEL', '0 99 113 114 128 227 257 299 355 356 370 371 484'))

with open('/Users/oz/Downloads/rosalind_ba4k.txt') as f:
    print(ba4k(*f.read().rstrip().split('\n')))
