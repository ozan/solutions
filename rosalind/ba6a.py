

def find(xs, x, i):
    """Find first instance of either x or -x starting from i"""
    while i < len(xs):
        if xs[i] == x or xs[i] == -x:
            return i
        i += 1
    return -1


def reverse(xs, i, j):
    """In place reversal of range (i, j) with sign flip"""
    while i <= j:
        xs[i], xs[j] = -xs[j], -xs[i]
        i, j = i + 1, j - 1


def ba6a(data):
    sp = [int(x) for x in data[1:-1].split()]

    i = 0
    while i < len(sp):
        x = sp[i]
        if x == i + 1:
            i += 1
            continue
        elif -x == i + 1:
            sp[i] = -x
            i += 1
        else:
            j = find(sp, i+1, i+1)
            reverse(sp, i, j)
        print('(' + ' '.join(f'{x:+}' for x in sp) + ')')


sample = "(-3 +4 +1 +5 -2)"
# ba6a(sample)

with open('/Users/oz/Downloads/rosalind_ba6a.txt') as f:
    ba6a(f.read().rstrip())
