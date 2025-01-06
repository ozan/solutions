import utils as u


comp = dict(zip('ACGT', 'TGCA'))


def rc(s):
    return [comp[x] for x in reversed(s)]


trans = dict(zip('ACGT', 'ACGU'))


def tr(s):
    return ''.join(trans[x] for x in s)


def ba4b(pattern, target):
    out = []
    subs_len = len(target) * 3
    s = pattern
    for start in range(len(s)-3):
        for i, x in enumerate(target):
            if x != u.codon_table[tr(s[start+3*i:start+3*(i+1)])]:
                break
        else:
            out.append(s[start:start+subs_len])
        # also check rc
        for i, x in enumerate(target):
            slce = s[start+subs_len-3*(i+1): start+subs_len-3*i]
            if len(slce) != 3 or x != u.codon_table[tr(rc(slce))]:
                break
        else:
            out.append(s[start:start+subs_len])

    return '\n'.join(out)


assert ba4b('ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA', 'MA') == """ATGGCC
GGCCAT
ATGGCC"""


with open('/Users/oz/Downloads/rosalind_ba4b.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    print(ba4b(*f.read().rstrip().split('\n')))
