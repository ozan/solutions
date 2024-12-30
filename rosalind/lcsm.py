sample = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

def lcsm(lines):
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

    # sort by shortest
    ss.sort(key=len)

    n = len(ss[0])
    while True:
        common = None
        for s in ss:
            subs = set()
            for i in range(len(s) - n + 1):
                subs.add(s[i:i+n])
            if common is None:
                common = subs
            else:
                common = common.intersection(subs)
            if not common:
                break
        if common:
            return common
        n -= 1
    pass


print(lcsm(sample.split('\n')))
print(lcsm(open('/Users/oz/Downloads/rosalind_lcsm.txt').read().split('\n')))

