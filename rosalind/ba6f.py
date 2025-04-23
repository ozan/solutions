
def ba6f(data):
    xs = [int(n) for n in data[1:-1].split()]

    out = []
    for x in xs:
        if x > 0:
            out.append(2*x-1)
            out.append(2*x)
        else:
            out.append(-2*x)
            out.append(-2*x-1)
    print('(' + ' '.join(str(x) for x in out) + ')')

sample = '(+1 -2 -3 +4)'
# ba6f(sample)

with open('/Users/oz/Downloads/rosalind_ba6f.txt') as f:
    ba6f(f.read().strip())


