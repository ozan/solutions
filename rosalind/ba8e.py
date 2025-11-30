import io


def d_avg(D, xs, ys):
    return sum(D[x][y] for x in xs for y in ys) / (len(xs) * len(ys))


def ba8e(f):
    n = int(f.readline())
    D = [[float(x) for x in line.split(' ')] for line in f]

    clusters = [{i} for i in range(n)]
    merged = set()

    for _ in range(n-1):
        _, c_i, c_j = min((D[i][j], i, j)
                          for i in range(len(D)) for j in range(i)
                          if i not in merged and j not in merged)
        merged |= {c_i, c_j}
        c_new = clusters[c_i] | clusters[c_j]
        D.append([0.0 if i in merged else d_avg(D, c_new, clusters[i])
                  for i in range(len(clusters))])
        clusters.append(c_new)

    print('\n'.join(' '.join(f'{x+1}' for x in c) for c in clusters if len(c) > 1))


sample = io.StringIO("""7
0.00 0.74 0.85 0.54 0.83 0.92 0.89
0.74 0.00 1.59 1.35 1.20 1.48 1.55
0.85 1.59 0.00 0.63 1.13 0.69 0.73
0.54 1.35 0.63 0.00 0.66 0.43 0.88
0.83 1.20 1.13 0.66 0.00 0.72 0.55
0.92 1.48 0.69 0.43 0.72 0.00 0.80
0.89 1.55 0.73 0.88 0.55 0.80 0.00""")


# ba8e(sample)

with open('/Users/oz/Downloads/rosalind_ba8e.txt') as f: ba8e(f)
