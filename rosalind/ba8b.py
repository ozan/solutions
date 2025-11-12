import io


def dist(x, y):
    return sum((xx-yy)**2 for xx, yy in zip(x, y))


def ba8b(f):
    """Find the mean squared distance from each data point to its nearest center"""
    k, m = map(int, f.readline().split(' '))
    centers = set(tuple(map(float, f.readline().split(' '))) for _ in range(k))
    assert f.readline()[:8] == '--------'
    points = set(tuple(map(float, line.split(' '))) for line in f)

    error = sum(min(dist(p, c) for c in centers) for p in points)
    print(f'{error/len(points):.3f}')


sample = io.StringIO("""2 2
2.31 4.55
5.96 9.08
--------
3.42 6.03
6.23 8.25
4.76 1.64
4.47 4.33
3.95 7.61
8.93 2.97
9.74 4.03
1.73 1.28
9.72 5.01
7.27 3.77""")

# ba8b(sample)

with open('/Users/oz/Downloads/rosalind_ba8b.txt') as f: ba8b(f)
