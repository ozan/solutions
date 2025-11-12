import io


def dist(x, y):
    return sum((xx-yy)**2 for xx, yy in zip(x, y))


def ba8c(f):
    """Lloyd algorithm: centers to clusters then clusters to centers"""
    k, m = map(int, f.readline().split(' '))
    points = [tuple(map(float, line.split(' '))) for line in f]
    centers = set(points[:k])

    while True:
        clusters = {c: [] for c in centers}
        for p in points:
            clusters[min((dist(c, p), c) for c in centers)[1]].append(p)

        next_centers = set()
        for v in clusters.values():
            c = [0.0] * m
            for point in v:
                for i, x in enumerate(point):
                    c[i] += x
            for i in range(m):
                c[i] /= len(v)
            next_centers.add(tuple(c))

        if next_centers == centers:
            break

        centers = next_centers

    for c in centers:
        print(' '.join(f'{x:.3f}' for x in c))


sample = io.StringIO("""2 2
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

# ba8c(sample)

with open('/Users/oz/Downloads/rosalind_ba8c.txt') as f: ba8c(f)
