from io import StringIO

from Bio.Seq import Seq

from utils import scan_fasta


def rvco(f):
    count = 0
    for _, seq in scan_fasta(f):
        rc = Seq(seq).reverse_complement()
        if rc == seq:
            count += 1
    return count


sample = """>Rosalind_64
ATAT
>Rosalind_48
GCATA"""

# print(rvco(StringIO(sample)))

with open('/Users/oz/Downloads/rosalind_rvco.txt') as f:
    print(rvco(f))

