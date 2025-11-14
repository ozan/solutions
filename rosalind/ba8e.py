import io


def ba8e(f):
    n = int(f.readline())
    D = [[float(x) for x in line.split(' ')] for line in f]

    clusters = [{i} for i in range(n)]  # cluster id to contained points... TODO needed?
    T = {i: [] for i in range(n)}  # TODO why not just use list?
    merged = set()

    while len(merged) < len(clusters) - 1:
        _, c_i, c_j = min((D[i][j], i, j) for i in range(len(D)) for j in range(i) if i not in merged and j not in merged)  # TODO better way to avoid?
        # c_new = c_i + c_j
        c_new = len(T)
        T[c_new] = [c_i, c_j]
        merged.add(c_i)
        merged.add(c_j)
        new_points = clusters[c_i] | clusters[c_j]
       
        row = []
        for c_id, points in enumerate(clusters):
            if c_id in merged:
                x = 0.0
            else:
                x = sum(D[i][j] for i in points for j in new_points) / (len(points) * len(new_points))
                # x = min(D[i][j] for i in points for j in new_points)
            row.append(x)
            # print(x)
        row.append(0.0)
        D.append(row)
        clusters.append(new_points)

    # print(clusters)
    for c in clusters:
        if len(c) < 2:
            continue
        print(' '.join(f'{x+1}' for x in c))


sample = io.StringIO("""7
0.00 0.74 0.85 0.54 0.83 0.92 0.89
0.74 0.00 1.59 1.35 1.20 1.48 1.55
0.85 1.59 0.00 0.63 1.13 0.69 0.73
0.54 1.35 0.63 0.00 0.66 0.43 0.88
0.83 1.20 1.13 0.66 0.00 0.72 0.55
0.92 1.48 0.69 0.43 0.72 0.00 0.80
0.89 1.55 0.73 0.88 0.55 0.80 0.00""")


ba8e(sample)

# with open('/Users/oz/Downloads/rosalind_ba8e.txt') as f: ba8e(f)
