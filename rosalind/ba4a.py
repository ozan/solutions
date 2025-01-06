import utils as u


def ba4a(pattern):
    out = []
    for i in range(0, len(pattern), 3):
        aa = u.codon_table[pattern[i:i+3]]
        if aa is None:
            break
        out.append(aa)
    return ''.join(out)


assert ba4a('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA') == 'MAMAPRTEINSTRING'


with open('/Users/oz/Downloads/rosalind_ba4a.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    print(ba4a(f.read().rstrip()))
