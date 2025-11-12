
def afrq(A):
    return [1 + 2*x**0.5 - x for x in A]


sample = "0.1 0.25 0.5"
print(' '.join(f'{p:.03f}' for p in afrq(float(c) for c in sample.split(' '))))
