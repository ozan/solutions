import utils as u


def kmp(word):
    table = [0] * len(word)
    for i in range(1, len(word)):
        j = table[i-1]
        while j > 0 and word[i] != word[j]:
            j = table[j-1]
        if word[i] == word[j]:
            j += 1
        table[i] = j
    print(' '.join(str(s) for s in table))
    return table


sample = """>Rosalind_87
CAGCATGGTATCACAGCAGAG"""

with open('/Users/oz/Downloads/rosalind_kmp.txt') as f:
    for _, s in u.scan_fasta(f):
        kmp(s)


