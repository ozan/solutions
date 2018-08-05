def spiral(size):
    x, d, vals = 0, 1j, {}
    for n in range(size * size):
        vals[x] = n + 1
        if {(x+d).real, (x+d).imag} & {-1, size} or x+d in vals:
            d *= -1j
        x += d
    return [[vals[i + 1j*j] for j in range(size)] for i in range(size)]
