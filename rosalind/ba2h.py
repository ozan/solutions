# import utils as u


def ba2h(data):
    pattern = data[0]
    dna = data[1].split()
    k = len(pattern)

    return sum(
        min(sum(x != y for x, y in zip(pattern, s[i:i+k]))
            for i in range(len(s) - k + 1))
        for s in dna)


sample = """AAA
TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT""".split('\n')

print(ba2h(sample))


with open('/Users/oz/Downloads/rosalind_ba2h.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    print(ba2h(f.read().rstrip().split('\n')))
