# import utils as u
from collections import Counter


def convolution(spectrum, m):
    """
    Given an experimental spectrum, return top m (with ties) most frequent
    positive differences
    """
    c = Counter()
    for xi, x in enumerate(spectrum):
        for yi in range(xi + 1, len(spectrum)):
            y = spectrum[yi]
            diff = y - x if y >= x else x - y
            if 57 <= diff <= 200:
                c[diff] += 1

    desc = sorted(c.items(), key=lambda x: x[1], reverse=True)
    if len(desc) > m:
        i = m-1
        count = desc[i][1]
        while desc[i][1] == count:
            i += 1
        desc = desc[:i]
    return [x[0] for x in desc]


def count_linear(seq):
    pref = [0]
    for p in seq:
        pref.append(pref[-1] + p)

    spec = [0]
    for i in range(len(seq)):
        for j in range(i+1, len(seq) + 1):
            spec.append(pref[j] - pref[i])

    return Counter(spec)


def count_cyclic(seq):
    len_p = len(seq)
    first, curr = seq, [0] * len_p
    spec = [0, sum(first)]
    for n in range(1, len_p):
        for i in range(0, len_p):
            curr[i] += first[(i+n) % len_p]
        spec.extend(curr)

    return Counter(spec)


def ba4i(m, n, spec):
    m, n = int(n), int(m)
    spec_list = [int(x) for x in spec.split(' ')]
    parent_mass = spec_list[-1]

    parts = convolution(spec_list, m)

    counts = Counter(spec_list)

    leaderboard = [[]]

    best, best_score = None, 0

    while leaderboard:
        candidates = []
        for prior in leaderboard:
            for p in parts:
                seq = prior + [p]
                if sum(seq) > parent_mass:
                    continue
                cyc_score = sum((count_cyclic(seq) & counts).values())
                if cyc_score > best_score and sum(seq) == parent_mass:
                    best, best_score = seq, cyc_score
                linear_score = sum((count_linear(seq) & counts).values())
                candidates.append((linear_score, seq))

        candidates.sort(reverse=True)

        if len(candidates) >= n:
            i = n - 1
            cutoff = candidates[i][0]
            while i < len(candidates) and candidates[i][0] == cutoff:
                i += 1
            candidates = candidates[:i]
        leaderboard = [x[1] for x in candidates]

    print(best_score)

    return best


sample = """20
60
57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493""".split('\n')

# print(ba4i(*sample))


with open('/Users/oz/Downloads/rosalind_ba4i.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    m, n, spec = f.read().rstrip().split('\n')
    res = [str(x) for x in ba4i(m, n, spec)]
    print('-'.join(res))
