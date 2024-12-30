import functools


prod = functools.partial(functools.reduce, lambda a, b: a * b)


def pmch(s):
    gc = sum(c in 'CG' for c in s)
    au = len(s) - gc
    return prod(range(1, gc//2+1)) * prod(range(1, au//2+1))


print(pmch("AGCUAGUCAU"))
print(pmch('AAUCACUACCGGUAGUACCUUCUAAAGGACAGGACAUUUUUUACCUGCGCCAGAUAUUGCAGUGUGAGGGCC'))
