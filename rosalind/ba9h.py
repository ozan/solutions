from functools import cmp_to_key
import io


def cmp(text):
    def inner(i, j):
        while i < len(text) and j < len(text):
            ci, cj = text[i], text[j]
            if ci < cj: return -1
            if ci > cj: return 1
            i += 1
            j += 1
        if i == j:
            return 0
        if i < j:
            return 1
        return -1

    return inner


def ba9h(f):
    text = f.readline().rstrip()
    patterns = [line.rstrip() for line in f]

    cmp_func = cmp(text)
    suffixes = sorted(range(len(text)), key=cmp_to_key(cmp_func))

    out = []
# binary search for any occurrences of patterns in suffixes
    # first just find one occurence of one pattern
    for p in patterns:
        lo, hi = 0, len(suffixes)  # target, if it exists, is in range [lo, hi)

        # first our target is the first occurence, if any, of a match
        while lo < hi:
            mid = (lo + hi) // 2
            probe = suffixes[mid]
            test = text[probe:probe+len(p)]
            if p > test:
                lo = mid + 1
            else:
                hi = mid

        first = lo
        # now try to find the last occurence of a match

        hi = len(suffixes)
        while lo < hi:
            mid = (lo + hi) // 2
            probe = suffixes[mid]
            test = text[probe:probe+len(p)]
            if p < test:
                hi = mid
            else:
                lo = mid + 1

        last = hi
        out.extend(suffixes[i] for i in range(first, last))

    out.sort()
    print(' '.join(str(x) for x in out))


sample = io.StringIO("""AATCGGGTTCAATCGGGGT
ATCG
GGGT""")


# ba9h(sample)

with open('/Users/oz/Downloads/rosalind_ba9h.txt') as f: ba9h(f)
