
vals = {'C': -1, 'G': 1, 'A': 0, 'T': 0}


def f(dna):
    indices = [0]
    skew = 0
    best = 0
    for i, d in enumerate(dna):
        skew += vals[d]
        if skew < best:
            best = skew
            indices = []
        if skew == best:
            indices.append(i + 1)
    return indices
