from functools import cmp_to_key


def cmp(text):
    """
    i should come before j iff the cyclic permutation starting at i + 1 mod len(text)
    is less than the cyclic permutation starting at j + 1
    """
    n = len(text)

    def inner(i, j):
        for d in range(len(text)):
            ci, cj = text[(i+d+1) % n], text[(j+d+1) % n]
            if ci < cj: return -1
            if ci > cj: return 1
        return 0
    return inner


def ba9i(text):
    """
    Construct the Burrows-Wheeler transform of given text
    """
    indices = sorted(range(len(text)), key=cmp_to_key(cmp(text)))
    bwt = ''.join(text[i] for i in indices)
    print(bwt)


# ba9i('GCGTGCCTGGTCA$')

with open('/Users/oz/Downloads/rosalind_ba9i.txt') as f: ba9i(f.read().rstrip())
