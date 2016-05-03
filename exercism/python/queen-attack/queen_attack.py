def board(W, B):
    validate(W, B)
    syms = {W: 'W', B: 'B'}
    return [''.join(syms.get((i, j), '_') for j in range(8)) for i in range(8)]


def can_attack(W, B):
    validate(W, B)
    di, dj = abs(W[0] - B[0]), abs(W[1] - B[1])
    return di == 0 or dj == 0 or di == dj


def validate(W, B):
    if any(x not in range(8) for x in W + B):
        raise ValueError('Piece outside board')
    if W == B:
        raise ValueError('Pieces on same square')
