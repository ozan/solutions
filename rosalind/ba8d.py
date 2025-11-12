import io
import math


def dist(x, y):
    return sum((xx-yy)**2 for xx, yy in zip(x, y))**0.5


def ba8d(f):
    """Soft k-means clustering"""
    k, m = map(int, f.readline().split(' '))
    beta = float(f.readline())
    data = [[float(x) for x in line.split(' ')] for line in f]
    n = len(data)

    # start by copying first k points as centers, per problem spec
    centers = [data[i][:] for i in range(k)]
    hidden_matrix = [[0.0] * n for _ in range(k)]

    for _ in range(100):
        # Step 1: each (point, center) should be assigned a "responsibility", ie
        # to what degree that point's membership should be attributed to that center
        # we construct a k x n matrix, ie one row for each center; one column per point

        # populate in two steps: first calculate absolute pull, then normalize
        for i in range(k):
            for j in range(n):
                hidden_matrix[i][j] = math.exp(-beta * dist(data[j], centers[i]))

        for j in range(n):
            tot = sum(hidden_matrix[i][j] for i in range(k))
            for i in range(k):
                hidden_matrix[i][j] /= tot

        # Step 2: Use these soft clusters to compute new clusters
        for i in range(k):
            norm = sum(hidden_matrix[i])
            for j in range(m):  # the jth dimension, out of m
                x = sum(hidden_matrix[i][di] * datum[j] for di, datum in enumerate(data))
                centers[i][j] = x / norm

    for c in centers:
        print(' '.join(f'{x:.3f}' for x in c))


sample = io.StringIO("""2 2
2.7
1.3 1.1
1.3 0.2
0.6 2.8
3.0 3.2
1.2 0.7
1.4 1.6
1.2 1.0
1.2 1.1
0.6 1.5
1.8 2.6
1.2 1.3
1.2 1.0
0.0 1.9""")

# ba8d(sample)

with open('/Users/oz/Downloads/rosalind_ba8d.txt') as f: ba8d(f)
