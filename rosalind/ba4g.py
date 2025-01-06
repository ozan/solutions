# import utils as u

from collections import Counter


parts = {57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186}


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


def ba4g(n, spec):
    n = int(n)
    spec_list = [int(x) for x in spec.split(' ')]
    parent_mass = spec_list[-1]
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


sample = """10
0 71 113 129 147 200 218 260 313 331 347 389 460""".split('\n')

# print(ba4g(*sample))


# with open('/Users/oz/Downloads/ba4g_extra.txt') as f:
with open('/Users/oz/Downloads/rosalind_ba4g (7).txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    n, spec = f.read().rstrip().split('\n')
    res = [str(x) for x in ba4g(n, spec)]
    print('-'.join(res))
    counts = Counter(int(x) for x in spec.split())
