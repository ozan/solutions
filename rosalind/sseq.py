import utils as u


def sseq(dataset):
    _, s = next(dataset)
    _, t = next(dataset)

    ti = 0
    out = []
    for si, sx in enumerate(s):
        if sx == t[ti]:
            out.append(si + 1)
            ti += 1
            if ti == len(t):
                return out

    return None


sample = """>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA"""

# print(sseq(u.scan_fasta(sample)))

with open('/Users/oz/Downloads/rosalind_sseq.txt') as f:
    print(' '.join(map(str, sseq(u.scan_fasta(f)))))
