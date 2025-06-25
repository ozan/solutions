sample = """
ATGCTACC
CGTTTACC
ATTCGACC
AGTCTCCC
CGTCTATC
""".rstrip().split()


def cstr(dna):
    n, out, bits = len(dna), [], [0] * len(dna)

    for i in range(len(dna[0])):
        counts = 0
        for j in range(n):
            bits[j] = int(dna[j][i] == dna[0][i])
            counts += bits[j]
        if 2 <= counts <= n - 2:
            out.append(''.join(str(b) for b in bits))

    return out


assert cstr(sample) == ['10110', '10100']

with open('/Users/oz/Downloads/rosalind_cstr.txt') as f:
    print('\n'.join(cstr(f.read().rstrip().split('\n'))))

