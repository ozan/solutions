masses = dict(zip(
    'GASPVTCILNDKQEMHFRYW',
    [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]))


def ba4j(peptide):
    pref = [0]
    for p in peptide:
        pref.append(pref[-1] + masses[p])
    spec = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide) + 1):
            spec.append(pref[j] - pref[i])
    print(' '.join(str(x) for x in sorted(spec)))


ba4j('LHRAFFFLCKTCKRNTTEIVRMHAEKAIKWWTEWCRGYYL')

# with open('/Users/oz/Downloads/rosalind_ba4j.txt') as f:
    # dbru(f.read().rstrip().split('\n'))
