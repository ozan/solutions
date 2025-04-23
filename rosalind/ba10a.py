import itertools as it


def ba10a(data):
    states = data[2].split()
    path = [states.index(s) for s in data[0]]
    trans = [[float(p) for p in row.split()[1:]] for row in data[5:]]

    print(states, path, trans)
    
    p = 0.5
    for s, t in zip(path, it.islice(path, 1, None)):
        p *= trans[s][t]

    print(p)


sample = """AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB
--------
A   B
--------
    A   B
A   0.194   0.806
B   0.273   0.727""".split('\n')


# ba10a(sample)

with open('/Users/oz/Downloads/rosalind_ba10a (3).txt') as f:
     ba10a(f.read().rstrip().split('\n'))
