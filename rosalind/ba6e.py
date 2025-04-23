from collections import defaultdict

comp = dict(zip('ACGT', 'TGCA'))


def ba6e(data):
    k = int(data[0])
    s, t = data[1], data[2]

    xs = defaultdict(list)
    ys = defaultdict(list)

    for i in range(len(s) - k + 1):
        sub = s[i:i+k]
        rc = ''.join(comp[x] for x in reversed(sub))
        xs[sub].append(i)
        xs[rc].append(i)

    for i in range(len(t) - k + 1):
        sub = t[i:i+k]
        ys[sub].append(i)

    out = []
    for k, xx in xs.items():
        if k not in ys:
            continue
        yy = ys[k]
        for x in xx:
            for y in yy:
                out.append((x, y))

    for p in out:
        print(p)
    return out



sample = """3
AAACTCATC
TTTCAAATC""".split('\n')

# ba6e(sample)

with open('/Users/oz/Downloads/rosalind_ba6e (1).txt') as f:
    ba6e(f.read().split('\n'))


