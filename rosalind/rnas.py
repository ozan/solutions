# import utils as u

match = dict(zip('AUCG', ('U', 'AG', 'G', 'UC')))


def rnas(s):
    """
    Memo[i][j] -> Matches in range [j, i)
    """
    memo = [[1 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]

    for end in range(0, len(s) + 1):
        for start in range(end-1, -1, -1):
            exp = match[s[start]]
            tot = memo[end][start+1]
            for i in range(start+4, end):
                if s[i] in exp:
                    tot += memo[i][start+1] * memo[end][i+1]
            memo[end][start] = tot
    return memo[len(s)][0]


sample = 'AUGCUAGUACGGAGCGAGUCUAGCGAGCGAUGUCGUGAGUACUAUAUAUGCGCAUAAGCCACGU'

print(rnas(sample))

print(rnas('CCAUCCGGCAGGCGAUGUCGUGACACUUGGAAAUGCAACUGAGUUAAAUCUCCAUAAUAAUAGUGAGAUUUCCUCCGGAACGCACUAGUUGAGUCGGCCGCGUUAAAAUCGAACGUCUGUGACGAGAAGAUCAGAGAUAACGCGGGUCGCUAUUUACAUCCCCUCAUAUGGCACUUAGUCCUCAAACGGUUC'))

# print(rnas_rec(next(u.scan_fasta(sample))[1]))

# with open('/Users/oz/Downloads/rosalind_rnas_rec (1).txt') as f:
#    print(rnas_rec(next(u.scan_fasta(f))[1]))
