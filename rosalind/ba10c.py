
def ba10c(data):
    alpha = data[2].split()
    x = [alpha.index(c) for c in data[0]]

    states = data[6].split()

    trans = [[float(p) for p in row.split()[1:]] for row in data[7:7+len(states)]]
    emission = [[float(p) for p in row.split()[1:]] for row in data[9+len(states):]]
    
    memo = [[(1.0, None) for _ in states]]

    for xi, xx in enumerate(x):
        nxt = []
        prior = memo[xi]
        for si in range(len(states)):
            em = emission[si][xx]
            max_w = max((em * pr[0] * trans[pi][si], pi) for pi, pr in enumerate(prior))
            nxt.append(max_w)
        memo.append(nxt)

    sink = max((pr, pi) for pi, pr in enumerate(memo[-1]))
    _, si = sink

    mi = len(memo) - 1
    hidden = []
    while mi > 0:
        hidden.append(states[si])
        si = memo[mi][si][1]
        mi -= 1

    print(''.join(reversed(hidden)))


sample = """xyxzzxyxyy
--------
x   y   z
--------
A   B
--------
    A   B
A   0.641   0.359
B   0.729   0.271
--------
    x   y   z
A   0.117   0.691   0.192
B   0.097   0.42    0.483""".split('\n')


# ba10c(sample)

with open('/Users/oz/Downloads/rosalind_ba10c.txt') as f:
    ba10c(f.read().rstrip().split('\n'))
