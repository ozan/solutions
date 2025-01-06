from collections import defaultdict
# import utils as u


def ba3l(data):
    k, d = (int(x) for x in data[0].split())

    kdmers = [line.split('|') for line in data[1:]]

    out = [kdmers[0][0]]
    out.extend(x[0][-1] for x in kdmers[1:])
    out.extend(x[1][0] for x in kdmers[-(d+1):-1])
    out.append(kdmers[-1][1])

    return ''.join(out)


sample = """4 2
GACC|GCGC
ACCG|CGCC
CCGA|GCCG
CGAG|CCGG
GAGC|CGGA""".split('\n')

assert ba3l(sample) == 'GACCGAGCGCCGGA'


with open('/Users/oz/Downloads/rosalind_ba3l.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    print(ba3l(f.read().rstrip().split('\n')))
