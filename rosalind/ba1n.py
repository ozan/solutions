from itertools import combinations, product


def f(s, d):
    seen = set()
    for indices in combinations(range(len(s)), d):
        for replacements in product('ATCG', repeat=d):
            m = dict(zip(indices, replacements))
            mut = ''.join(m[i] if i in m else ch for i, ch in enumerate(s))
            if mut not in seen:
                seen.add(mut)
                yield mut


print('\n'.join(f('TCACCACTTG', 3)))
