from functools import cmp_to_key


def cmp(text):
    def inner(i, j):
        while i < len(text) and j < len(text):
            ci, cj = text[i], text[j]
            if ci < cj: return -1
            if ci > cj: return 1
            i += 1
            j += 1
        if i == j:
            return 0
        if i < j:
            return 1
        return -1

    return inner


def ba9g(text):
    """
    Constructs the suffix array without explicitly creating the substrings in memory
    """
    suffixes = sorted(range(len(text)), key=cmp_to_key(cmp(text)))
    print(', '.join(str(i) for i in suffixes))


ba9g('AACGATAGCGGTAGA$')

with open('/Users/oz/Downloads/rosalind_ba9g.txt') as f: ba9g(f.read().rstrip())
