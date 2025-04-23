from pprint import pprint
from collections import Counter


def conv(data):
    s1, s2 = (list(map(float, row.split())) for row in data)

    mink_diff = [round(abs(x1 - x2), 6) for x1 in s1 for x2 in s2]
    counts = Counter(mink_diff)
    n, x = max((v, k) for k, v in counts.items())
    print(n)
    print(x)


sample = """186.07931 287.12699 548.20532 580.18077 681.22845 706.27446 782.27613 968.35544 968.35544
101.04768 158.06914 202.09536 318.09979 419.14747 463.17369""".split('\n')


# conv(sample)


with open('/Users/oz/Downloads/rosalind_conv.txt') as f:
    print(conv(f.read().rstrip().split('\n')))
