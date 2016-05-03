SPACE, MINE, NS_EDGE, EW_EDGE, CORNER = ' *|-+'

product = lambda xs, ys: [(x, y) for x in xs for y in ys]
OFFSETS = product((-1, 0, 1), (-1, 0, 1))

chunk = lambda n, xs: [xs[i*n:(i+1)*n] for i in range(len(xs) // n)]


def board(M):
    validate(M)
    width, height = (len(M[0]), len(M))
    syms = [counts(M, i, j) for i, j in product(range(height), range(width))]
    return [''.join(row) for row in chunk(width, syms)]


def counts(M, i, j):
    if M[i][j] != SPACE: return M[i][j]
    return str(sum(M[i + di][j + dj] == MINE for di, dj in OFFSETS) or ' ')


def validate(M):
    MT = list(zip(*M))
    edges = M[0] + M[-1] + ''.join(MT[0] + MT[-1])
    pieces = ''.join(row[1:-1] for row in M[1:-1])

    errors = [msg for msg, predicate in (
        ('Irregular board shape', len(set(map(len, M))) > 2),
        ('Weird edge', set(edges) - set(NS_EDGE + EW_EDGE + CORNER)),
        ('Weird piece', set(pieces) - set(SPACE + MINE))
    ) if predicate]
    if errors: raise ValueError(errors[0])
