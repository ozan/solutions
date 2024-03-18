from collections import defaultdict
from itertools import combinations, product


def mutations(s, d):
    seen = set()
    for indices in combinations(range(len(s)), d):
        for replacements in product('ATCG', repeat=d):
            m = dict(zip(indices, replacements))
            mut = ''.join(m[i] if i in m else ch for i, ch in enumerate(s))
            if mut not in seen:
                seen.add(mut)
                yield mut


comp = dict(zip('ATCG', 'TAGC'))


def rev_comp(s):
    return ''.join(comp[c] for c in reversed(s))


def f(text, k, d):
    """
    Assume k <= 12 and d <= 3

    Idea 1:
    for each 4^k possible k-mer, scan text and find number of approximate occurrences.
    This would be O(4^k * len(text) * d)

    Idea 2:
    Iterate over string once, generating all k-mers within d of the substring.
    There will be kCd many patterns, each with 3^d possible k-mers.
    This would then give us O(kCd * len(text) * 3^d)

    Let's say k = 12 and d = 3. Idea 1 is ~ 50M * len(text) whereas Idea 2 is
    ~ 18K * len(text), so much better to use idea 2
    """
    counts = defaultdict(lambda: 0)

    for i in range(len(text) - k + 1):
        substr = text[i:i+k]
        for mut in mutations(substr, d):
            counts[mut] += 1
            counts[rev_comp(mut)] += 1

    mx = -1
    res = []
    for k, v in counts.items():
        if v > mx:
            mx = v
            res = []
        if v == mx:
            res.append(k)
    return res


print(f('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1))
