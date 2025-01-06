comp = dict(zip('ACGT', 'TGCA'))


def dbru(kmers):
    out = set()
    for k in kmers:
        rc = ''.join(comp[x] for x in reversed(k))
        out.add((k[:-1], k[1:]))
        out.add((rc[:-1], rc[1:]))
    print('\n'.join(f'({a}, {b})' for a, b in out))


sample = """TGAT
CATG
TCAT
ATGC
CATC
CATC""".split('\n')

# dbru(sample)

with open('/Users/oz/Downloads/rosalind_dbru.txt') as f:
    dbru(f.read().rstrip().split('\n'))
