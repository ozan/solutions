sample = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""


def grph(lines):
    strings = []
    name, s = None, ''
    for line in lines:
        if line == '':
            strings.append((name, s))
            break
        if line[0] == '>':
            if s:
                strings.append((name, s))
            name = line[1:]
            s = ''
        else:
            s += line

    # find adjacencies by just testing all of them
    for sname, s in strings:
        for tname, t in strings:
            if s != t and s[-3:] == t[:3]:
                print(sname, tname)


grph(sample.split('\n'))
print()
grph(open('/Users/oz/Downloads/rosalind_grph.txt').read().split('\n'))

