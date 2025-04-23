
def mer(data):
    xs = [int(x) for x in data[1].split()]
    ys = [int(y) for y in data[3].split()]

    out, xi, yi = [], 0, 0
    while xi < len(xs) or yi < len(ys):
        if yi == len(ys) or xs[xi] < ys[yi]:
            out.append(xs[xi])
            xi += 1
        else:
            out.append(ys[yi])
            yi += 1

    print(' '.join(str(x) for x in out))


sample = """4
2 4 10 18
3
-5 11 12""".split('\n')

# mer(sample)

with open('/Users/oz/Downloads/rosalind_mer.txt') as f:
    mer(f.read().rstrip().split('\n'))


