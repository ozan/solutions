
def ba6g(data):
    xs = [int(n) for n in data[1:-1].split()]

    out = []
    for i in range(0, len(xs), 2):
        a, b = xs[i], xs[i+1]
        out.append((1 if b > a else -1) * max(a, b) // 2)
    print('(' + ' '.join(f'{x:+}' for x in out) + ')')

sample = '(1 2 4 3 6 5 7 8)'
# ba6g(sample)

with open('/Users/oz/Downloads/rosalind_ba6g.txt') as f:
    ba6g(f.read().strip())


