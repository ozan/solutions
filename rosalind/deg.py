
def deg(data):
    nv, ne = map(int, data[0].split())
    deg = [0] * (nv+1)
    for line in data[1:]:
        a, b = map(int, line.split())
        deg[a] += 1
        deg[b] += 1
    print(' '.join(str(n) for n in deg[1:]))


sample = """6 7
1 2
2 3
6 3
5 6
2 5
2 4
4 1""".split('\n')

# deg(sample)

with open('/Users/oz/Downloads/rosalind_deg.txt') as f:
    deg(f.read().rstrip().split('\n'))


