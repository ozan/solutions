sample = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""


def cons(lines):
    # first, parse
    ss = []
    current = None
    for l in lines:
        if l == '' or l[0] == '>':
            if current:
                ss.append(current)
            current = ''
        else:
            current += l

    P = []
    for c in 'ACGT':
        r = []
        for i in range(len(ss[0])):
            r.append(sum(c == s[i] for s in ss))
        P.append(r)

    consensus = ''.join(max(zip(col, 'ACGT'))[1] for col in zip(*P))

    print(consensus)
    for c, row in zip('ACGT', P):
        print(f'{c}: {" ".join(str(n) for n in row)}')


cons(sample.split('\n'))
print(cons(open('/Users/oz/Downloads/rosalind_cons.txt').read().split('\n')))

