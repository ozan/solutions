from collections import defaultdict


def ba9m(f):
    bwt = f.readline().rstrip()
    patterns = f.readline().rstrip().split(' ')

    # count[sym][i] = number of occurences of sym in first i positions
    count = {}
    for i, c in enumerate(bwt):
        if c not in count:
            count[c] = [0] * (i + 1)
        for cc in count:
            count[cc].append(count[cc][-1] + (c == cc))

    # first_occ[sym] = index of first occurence of sym in first column
    first_occ = {}
    for i, c in enumerate(sorted(bwt)):
        if c in first_occ:
            continue
        first_occ[c] = i
    print(first_occ)

    out = []
    for p in patterns:
        pattern = [c for c in p]

        top = 0
        bottom = len(bwt) - 1
        matched = False
        while top <= bottom:
            if not pattern:
                out.append(bottom - top + 1)
                matched = True
                break

            symbol = pattern.pop()
            top = first_occ[symbol] + count[symbol][top]
            bottom = first_occ[symbol] + count[symbol][bottom+1] - 1

        if not matched:
            out.append(0)

    print(' '.join(str(n) for n in out))


sample = """GGCGCCGC$TAGTCACACACGCCGTA
ACC CCG CAG"""

# ba9m(io.StringIO(sample))


with open('/Users/oz/Downloads/rosalind_ba9m (1).txt') as f: ba9m(f)
