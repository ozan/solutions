# import utils as u

masses = dict(zip(
    'GASPVTCILNDKQEMHFRYW',
    [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]))


def ba4c(peptide):
    len_p = len(peptide)
    first, curr = [masses[p] for p in peptide], [0] * len_p
    out = [0, sum(first)]
    for n in range(1, len_p):
        for i in range(0, len_p):
            curr[i] += first[(i+n) % len_p]
        out.extend(curr)
    out.sort()
    return out


# print(' '.join(str(x) for x in ba4c('FWSIICLIRWFPAA')))


# with open('/Users/oz/Downloads/rosalind_ba4b.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    # print(ba4b(*f.read().rstrip().split('\n')))
