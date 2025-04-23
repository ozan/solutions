"""
NOTE not really sure what's going on here. It really seems like this is the
right algorithm... initializing with 1.0 / |States|, return the sum etc.
Parsing seems to be correct. Hmm
"""

def ba10d(data):
    alpha = data[2].split()
    x = [alpha.index(c) for c in data[0]]

    states = data[6].split()

    trans = [[float(p) for p in row.split()[1:]] for row in data[7:7+len(states)]]
    emission = [[float(p) for p in row.split()[1:]] for row in data[9+len(states):]]

    memo = [[1.0 / len(states) for s in states]]
  
    for xi, xx in enumerate(x):
        nxt = []
        prior = memo[-1]
        for si in range(len(states)):
            exp = emission[si][xx] * sum(pr * trans[pi][si] for pi, pr in enumerate(prior))
            nxt.append(exp)
        memo.append(nxt)
    
    # pprint(memo)
    print(sum(memo[-1]))


sample = """xzyyzzyzyy
--------
x   y   z
--------
A   B
--------
    A   B
A   0.303   0.697 
B   0.831   0.169 
--------
    x   y   z
A   0.533   0.065   0.402 
B   0.342   0.334   0.324""".split('\n')


ba10d(sample)

with open('/Users/oz/Downloads/rosalind_ba10d (3).txt') as f:
    ba10d(f.read().rstrip().split('\n'))
