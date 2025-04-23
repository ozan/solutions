def ba10b(data):
    alpha = data[2].split()
    x = [alpha.index(c) for c in data[0]]

    states = data[6].split()
    path = [states.index(s) for s in data[4]]

    emission = [[float(p) for p in row.split()[1:]] for row in data[9:]]

    p = 1.0    
    for s, xx in zip(path, x):
        p *= emission[s][xx]

    print(p)


sample = """xxyzyxzzxzxyxyyzxxzzxxyyxxyxyzzxxyzyzxzxxyxyyzxxzx
--------
x   y   z
--------
BBBAAABABABBBBBBAAAAAABAAAABABABBBBBABAABABABABBBB
--------
A   B
--------
    x   y   z
A   0.612   0.314   0.074 
B   0.346   0.317   0.336""".split('\n')


# ba10b(sample)

with open('/Users/oz/Downloads/rosalind_ba10b.txt') as f:
    ba10b(f.read().rstrip().split('\n'))
