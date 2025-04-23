

def pcov(data):
    g = {}
    for l in data:
        pref, suff = l[:-1], l[1:]
        g[pref] = suff

    a = suff
    out = []
    while g:
        out.append(a[0])
        b = g[a]
        del g[a]
        a = b

    return ''.join(out)


sample = """ATTAC
TACAG
GATTA
ACAGA
CAGAT
TTACA
AGATT""".split('\n')

assert pcov(sample) == 'GATTACA'

print(pcov(open('/Users/oz/Downloads/rosalind_pcov.txt').read().rstrip().split('\n')))
