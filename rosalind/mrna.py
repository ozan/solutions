opts = {'F': 2, 'L': 6, 'I': 3, 'V': 4, 'M': 1, 'S': 6, 'P': 4, 'T': 4, 'A': 4, 'Y': 2, 'H': 2, 'N': 2, 'D': 2, 'Q': 2, 'K': 2, 'E': 2, 'C': 2, 'R': 6, 'G': 4, 'W': 1}


sample = 'MA'


def mrna(s):
    out = 3  # different ways to stop
    for aa in s:
        out = (out * opts[aa]) % 1000000
    return out


print(mrna(sample))

print(mrna(open('/Users/oz/Downloads/rosalind_mrna.txt').read().rstrip()))
