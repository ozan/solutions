
vals = dict(zip('ACGT', range(4)))


def idx(kmer):
    # A, C, G and T are worth 0, 1, 2 or 3 respectively
    # each additional place increases value by 4x
    # so e.g. AC is 0 * 4 + 1, CA is 1 * 4 + 0, CGT is 1 * 16 + 2 * 4 + 3, etc
    total = 0
    for c in kmer:
        total <<= 2
        total += vals[c]
    return total


def f(text, k):
    """
    Return frequency array where the ith elemnt of the array holds
    the number of times the i-th k-mer (in lexicographic order) appears in text
    """
    freq = [0] * 4 ** k
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        freq[idx(kmer)] += 1
    return freq


print(' '.join(str(d) for d in f('ACGCGGCTCTGAAA', 2)))
