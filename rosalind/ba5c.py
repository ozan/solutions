sample = [
    'AACCTTGG',
    'ACACTGTGA'
]


def subs(xs, ys):
    cache = [''] * (len(ys) + 1)

    for x in xs:
        cache, prior = [''], cache
        for i, y in enumerate(ys):
            cache.append(max(prior[i+1], cache[i], prior[i] + (x if x == y else ''), key=len))

    return prior[-1]


res = subs("ACCGTCTTAGCGATCAACACATTTAACAACGCGCCGCACCCCCCGTCAAACGAGCTTTTGGGCTCTTGTCCTTTTACAAGCTTCACGACGCATACAGCCTTGATCAACGGTTTGATCTGTCTCCCTTCAGCTGGCTTTAAAGGACATACATATGAAGGCCTTAATAAGGTCCGGGAACTCCACATATTCGGTACTGGGCAAACCCCATGAACCACCTCAACATGAAGAGTCCGAGGACTCTCACGATCCACCAATGCAGATCGGAACTGTGCGATCGCGTAATGAGCCGAGTACTTGGTTTGTGTTTAGGTTATGGGGGCCGGGAGCCGGTTCAATATAAGGAAGTAGTTGCAGATTAGTTGTTGCGAACGGTCATAAATTTGATGGGTAAACGTGAACTTAACAAACCGTGATAGCTAATCCTATGCATCCCTTACGTGGATCGACTCGAGTACCCAGGTGAACCGACTACTTGATAACCGGAAATCGCGGTATAAAAGCGCTCACGGTCAGGAGATATACCTCCAAGCAGTAGTCTTTCTGAGCCTAGAGTAGTAAATTACAGGGACGATGTCTTTTACCGAGGCAACATTTTATTGAGAATCACATGAGGCACAGGTAAAGGCGACATCACGATCGAGATCAACCCCTACTTGTTCAAAACATTGAGAACCAGCTCTGTTTTGGAACCTAGAAAGATAACGCATCCGCTTGATATTCCACGGCTTGTCCCTCTTGTGCGGTCCATCTATCGGAGTTTCCTCCGATACGACCCGCAATGTTTCCAGGCGTACGGTACTTTATGAATACACTCGCGCTGTAACCTGTTATGTGAAACACACACGACAGAGCTTCGCGTGGGCCCAGCGACCCGGTAATACTACATCACCGCACACGACCTCGAGCAGTCTTTGCCGGCGTCCGTAAGTAGTCTAAAGTTGTGTTGATGCTTGGGGTTAAAGCTAAATCGTCCGCAGAATACGACTCTCATCCCAATA",
"ACCCGCACGCGCTTTGGTCTAGATTCTAGCTCCAACTTGCCTGCTAGATACTCTGTTAAAAGATGGTTTTACAACCCCCTCCTCTGTCCCTGGGGTATTATATAATACGTCGGATAGTCAGGTACAAATACAAGTGGGTGGGAATACTTTTCCTCGGATCCTAGACCACGGATTACTGCGTGGTTGACAAGAGTCGGCCCGGAGGGAAACGTGAAGGTTAGTGCAATTAAAGTCTCTAATGTGAAGCCTCCGCGAAGCGAGGAGTTTCTGAGATCGAGTACTATTTAGAGTTCGAAATCACGGCTTAACCTCACTGCCACGCATAACTTGCCGGCAATCCAGTTTTGCAACGATACTTAATTTGTGCAGCTCATCTTTGCTGTCCAGAAATAGAGCTAGTCGATCTCATCTTGCGGGTAGCCAGAAGTCCTACCGTCTCCTCCATGTAGCTTAAAAATTTCGGTGAGGATCAAAAATGATAAACGTGACAGGTAAGCTCCTACGTCTATCCTATGACCCCCGCGGCAGAATAGGTTGGTAGTGTTAGTGCGTGAGCTGGTAGAATAGAGCACACTTAGGGAAACGGGAACCGTTATGTAGGGCTGCGACACACAAAAAAGTGTTCGTTGGTAAGCTGCCTCTCCACTAAACAGGATTTCTCTGGATGATCCCATCGAAGCAAGTTACGCACCACGCCGAGGCGGACCCTGGTACTAGCTGCCCCCCCCTTTATGGGGCGCTCGTACATCAAGATGATCGCGGACTCAACCTGATTACGAGTTGTCCAAGTAGTCCAGGGTAAGAGAAACTGGAGAGA")

assert res == "ACCGCAGCGTCAATTTACAACGCCGCACCGTAAAGATGGTTTTACAACCCCCTCCCTGTCCGGTTTATTTCTCTAGTCAGGACAAATAAAGTGGTGGGAATACTTTCTCGGACCAGACCACTACTGGTGGTTGACAAGAGTCGGCCCGGAGGGAACTGGTTGTGTTAGTTATGGGCCCCGGAAGGAGAGTTGAGATCGAGTCTATTTGAGTCGAATCACGGCTAACCTATGCACCTACTTGCCGATCCAGTGAACGATACTTATACCATCGCGTAAAAAGGCTAGTCGATATCCTCCAGAGTAGTCTTCTGAGCTAAAAATTCGGGAGATCAAAAATATAAACTGACAGGTAAGCCTACGTCATCAACCCCCGCAAAATTGGAGTGTTTTGGCTAGAAAGAGCACCTTGAAACGGGCCTTTGTGGGTCCACACAGTTTCTGTAAGCTGTTCCACTACGGTCTTATGATCATCGGCAAGTTAGCACCACGCGAGGCGGACCCGGTACTACTCCCCCACGCTCGACATCTTGCGGCTCCTGATTAAGTTGTGTGTCGGGTAAAGAAACTGAGAGA"

print('ok')
