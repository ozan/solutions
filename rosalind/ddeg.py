from collections import defaultdict


def ddeg(data):
    nv, ne = map(int, data[0].split())
    g = defaultdict(list)

    for line in data[1:]:
        a, b = map(int, line.split())
        g[a].append(b)
        g[b].append(a)

    deg2 = [sum(len(g[x]) for x in g[i+1]) for i in range(nv)]

    print(' '.join(str(n) for n in deg2))


sample = """5 4
1 2
2 3
4 3
2 4""".split('\n')

ddeg(sample)

with open('/Users/oz/Downloads/rosalind_ddeg.txt') as f:
    ddeg(f.read().rstrip().split('\n'))


