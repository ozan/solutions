import io


def dist(x, y):
    return sum((xx-yy)**2 for xx, yy in zip(x, y))


def ba8a(f):
    """Find k centers in m dimensional space from the given points"""
    k, m = map(int, f.readline().split(' '))

    centers = [tuple(map(float, f.readline().split(' ')))]
    points = set(tuple(map(float, line.split(' '))) for line in f)

    while len(centers) < k:
        # Add to centers the point that is futhest away from any existing center
        _, nxt = max(min((dist(c, p), p) for c in centers) for p in points)
        centers.append(nxt)
        points.remove(nxt)

    for c in centers:
        print(' '.join(str(x) for x in c))


sample = io.StringIO("""3 2
0.0 0.0
5.0 5.0
0.0 5.0
1.0 1.0
2.0 2.0
3.0 3.0
1.0 2.0""")

# ba8a(sample)

with open('/Users/oz/Downloads/rosalind_ba8a.txt') as f:
    ba8a(f)
