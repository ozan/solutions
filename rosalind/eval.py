from functools import reduce, partial

prod = partial(reduce, lambda a, b: a * b)


def eval(data):
    n = int(data[0])
    dna = data[1]
    A = [float(x) for x in data[2].split()]

    B = []
    for a in A:
        p1 = prod((a if d in 'GC' else 1-a) / 2 for d in dna)
        B.append(p1 * (n - 1))

    print(' '.join(f'{b:.4f}' for b in B))
    return B


sample = """10
AG
0.25 0.5 0.75""".split('\n')

eval(sample)


with open('/Users/oz/Downloads/rosalind_eval.txt') as f:
    eval(f.read().rstrip().split('\n'))
