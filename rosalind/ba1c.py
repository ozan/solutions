

comp = dict(zip('ATCG', 'TAGC'))


def f(pattern):
    return ''.join(comp[p] for p in reversed(pattern))


print(f('AAAACCCGGT'))
