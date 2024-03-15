from collections import defaultdict


def frequent_kmer(text, k):
    d = defaultdict(lambda: 0)

    for i in range(len(text) - k + 1):
        d[text[i:i+k]] += 1

    highest = -1
    res = []
    for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
        if highest == -1:
            highest = v

        if highest != v:
            break
        res.append(k)

    return ' '.join(res)


assert frequent_kmer('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4) == 'GCAT CATG'
