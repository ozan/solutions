# import utils as u


def ba3c(kmers):
    for s in kmers:
        for t in kmers:
            if s[1:] == t[:-1]:
                print(f'{s} -> {t}')


sample = """ATGCG
GCATG
CATGC
AGGCA
GGCAT""".split('\n')

# print(ba3c(sample))


with open('/Users/oz/Downloads/rosalind_ba3c (1).txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    print(ba3c(f.read().rstrip().split('\n')))
