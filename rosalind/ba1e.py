from collections import defaultdict


def f(genome, k, L, t):
    """
    Return a ll distinct k-mers forming (L, t) clumps in genome, ie there are at
    least t occurrences of the k-mer in a region no longer than L

    Plan:

    - In first pass, store all indexes of all k-mers in a dictionary:
      this is O(len(genome) * k) in time, and as much as the smaller
      of O(len(genome) * k) and O(4^k) in space although likely smaller still
    - In second pass, iterate over each k-mer to see if there is a range of t indices
      where i_last + k - i_first <= L

    """
    d = defaultdict(list)
    for i in range(len(genome) - k + 1):
        d[genome[i:i+k]].append(i)

    matches = []
    for kmer, indices in d.items():
        for ii in range(len(indices) - t + 1):
            i_first, i_last = indices[ii], indices[ii + t - 1]
            if i_last + k - i_first <= L:
                matches.append(kmer)
                break

    matches.sort()
    return matches
