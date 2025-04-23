
def ins(data):
    xs = [int(x) for x in data[1].split()]
    swaps = 0
    for i in range(1, len(xs)):
        k = i
        while k > 0 and xs[k] < xs[k-1]:
            swaps += 1
            xs[k], xs[k-1] = xs[k-1], xs[k]
            k -= 1
    print(swaps)
    # print(xs)


sample = """6
6 10 4 5 1 2""".split('\n')

# ins(sample)

with open('/Users/oz/Downloads/rosalind_ins.txt') as f:
    ins(f.read().rstrip().split('\n'))


