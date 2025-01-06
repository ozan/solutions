# import utils as u


def ba3b(kmers):
    return ''.join(km[0] for km in kmers[:-1]) + kmers[-1]


sample = """ACCGA
CCGAA
CGAAG
GAAGC
AAGCT""".split('\n')

# print(ba3b(sample))


with open('/Users/oz/Downloads/rosalind_ba3b.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    print(ba3b(f.read().rstrip().split('\n')))
