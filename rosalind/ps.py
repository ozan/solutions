import heapq
import io


def ps(k, xs):
    maxq = []

    for x in xs:
        if len(maxq) < k:
            heapq.heappush(maxq, -x)
        else:
            heapq.heappushpop(maxq, -x)

    out = []
    while maxq:
        out.append(str(-heapq.heappop(maxq)))

    print(' '.join(reversed(out)))


def run(f):
    f.readline()  # n
    xs = [int(x) for x in f.readline().split()]
    k = int(f.readline())
    ps(k, xs)


sample = io.StringIO("""10
4 -6 7 8 -9 100 12 13 56 17
3""")

# run(sample)

with open('/Users/oz/Downloads/rosalind_ps (1).txt') as f: run(f)
