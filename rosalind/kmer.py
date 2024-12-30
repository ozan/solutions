from collections import defaultdict

def lexf(chars, n):
    if n == 1:
        return list(chars)

    return [c + rest for c in chars for rest in lexf(chars, n - 1)]


sample = """CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG"""


def kmer(s):
    counts = defaultdict(lambda: 0)
    for i in range(len(s) - 3):
        counts[s[i:i+4]] += 1

    return [counts[k] for k in lexf('ACGT', 4)]


print(' '.join(map(str, kmer(sample))))

with open('/Users/oz/Downloads/rosalind_kmer.txt') as f:
    lines = f.read().split('\n')
    print(' '.join(map(str, kmer(''.join(lines[1:])))))

# print('\n'.join(lexf('ACGT', 4)))
