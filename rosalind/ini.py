from Bio.Seq import Seq


def ini(s):
    seq = Seq(s)
    return ' '.join(str(seq.count(b)) for b in 'ACGT')


sample = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

print(ini(sample))


with open('/Users/oz/Downloads/rosalind_ini.txt') as f:
    print(ini(f.read()))
