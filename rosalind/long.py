# from io import StringIO
import utils as u


def long(dataset):
    """
    Assumes we can greedily match as we go, and that bruteforce is fine

    TODO must be a better way!
    """
    dataset = list(dataset)

    _, out = dataset.pop()

    seen = set()
    while len(dataset) > len(seen):
        # try matching to each
        best_i = 0
        for name, t in dataset:
            if name in seen:
                continue
            for i in range(best_i, len(t)):
                if i > best_i and t[:i] == out[-i:]:
                    best_out = out + t[i:]
                    best_i = i
                    best_name = name
                if i > best_i and out[:i] == t[-i:]:
                    best_out = t[:-i] + out
                    best_i = i
                    best_name = name
        out = best_out
        seen.add(best_name)

    return out


sample = """>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
"""

# print(lgis(u.scan_fasta(sample)))

with open('/Users/oz/Downloads/rosalind_long.txt') as f:
    print(long(u.scan_fasta(f)))
