
def saddle_points(M):
    if len(set(map(len, M))) > 1:
        raise ValueError

    MT = list(zip(*M))
    points = set()
    for i, row in enumerate(M):
        for j, x in enumerate(row):
            if x == max(row) and x == min(MT[j]):
                points.add((i, j))
    return points
