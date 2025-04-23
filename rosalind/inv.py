

def inv(data):
    xs = [int(x) for x in data[1].split()]
    cnt = 0
    for i, x in enumerate(xs):
        for j in range(i+1, len(xs)):
            y = xs[j]
            if x > y:
                cnt += 1
    print(cnt)
    return cnt


sample = """5
-6 1 15 8 10""".split('\n')

inv(sample)

with open('/Users/oz/Downloads/rosalind_inv.txt') as f:
    inv(f.read().rstrip().split('\n'))


