

def f(text, k, profile):
    lookup = dict(zip('ACGT', profile))
    return max(
        (sum(lookup[text[i+j]][j] for j in range(k)), text[i:i+k])
        for i in range(len(text) - k + 1)
    )


def parse(matrix):
    return [[float(x) for x in row.split(' ')] for row in matrix.strip().split('\n')]


print(f("AGGGGCGTATCACCTGTACAAGTGCTGCCTGTCACTTCATCAGAATTAACTAAAAAAATCGAGCGTAGGGGACAAGGGTAGACAGCCGGGCTAGGAATTGAGCTCACTCTCACACGACCTCCTCATCTTGGACTATCGCTTCTTGTGTACGCAAGAGTGACCGTTATCGCTAGCCACTTTGCTATTACTCAGTAGGCGCT", 8, parse("""
0.28 0.4 0.24 0.36 0.28 0.32 0.48 0.08
0.28 0.12 0.28 0.12 0.32 0.32 0.08 0.36
0.24 0.12 0.28 0.28 0.12 0.24 0.16 0.28
0.2 0.36 0.2 0.24 0.28 0.12 0.28 0.28
""")))
