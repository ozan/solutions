
def ba6j(data):
    edges = [tuple(map(int, part.split(', ')))
             for part in data[0][1:-1].split('), (')]
    a, b, c, d = [int(n) for n in data[1].split(', ')]

    out = []
    for x, y in edges:
        if (x == a and y == b) or (x == b and y == a):
            out.append((a, c))
        elif (x == c and y == d) or (x == d and y == c):
            out.append((b, d))
        else:
            out.append((x, y))

    print(', '.join(str(t) for t in out))


sample = """(2, 4), (3, 8), (7, 5), (6, 1)
1, 6, 3, 8""".split('\n')
# expected: (2, 4), (3, 1), (7, 5), (6, 8)
# ba6j(sample)

with open('/Users/oz/Downloads/rosalind_ba6j.txt') as f:
    ba6j(f.read().strip().split('\n'))

