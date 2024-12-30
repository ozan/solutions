
import utils as u


def revp(s):
    for n in range(4, 13):
        for i in range(len(s) - n + 1):
            ss = s[i:i+n]
            if ss == ''.join(u.reverse_comp(ss)):
                print(i + 1, n)


sample = """>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT"""

# print(revp(next(u.scan_fasta(sample))[1]))

with open('/Users/oz/Downloads/rosalind_revp.txt') as f:
    print(revp(next(u.scan_fasta(f))[1]))
