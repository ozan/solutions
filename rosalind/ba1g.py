
def f(xs, ys):
    return sum(1 for x, y in zip(xs, ys) if x != y)


print(f('GGGCCGTTGGT', 'GGACCGTTGAC'))
