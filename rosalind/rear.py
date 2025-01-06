from collections import deque


def inversions(xs, ys):

    q = deque([(ys, 0)])

    while q:
        seq, n = q.popleft()
        if seq == xs:
            return n

        start, end = 0, len(xs)
        while xs[start] == seq[start]:
            start += 1
        while xs[end-1] == seq[end-1]:
            end -= 1

        i = seq.index(xs[start])
        j = seq.index(xs[end-1])

        q.append((seq[:start] + list(reversed(seq[start:i+1])) + seq[i+1:], n + 1))
        q.append((seq[:j] + list(reversed(seq[j:end])) + seq[end:], n + 1))


def rear(data):
    cases = [
        [[int(x) for x in line.split(' ')] for line in pair.split('\n')]
        for pair in data.split('\n\n')]

    out = [inversions(xs, ys) for xs, ys in cases]
    print(' '.join(str(x) for x in out))
    return out


sample = """1 2 3 4 5 6 7 8 9 10
3 1 5 2 7 4 9 6 10 8

3 10 8 2 5 4 7 1 6 9
5 2 3 1 7 4 10 8 6 9

8 6 7 9 4 1 3 10 2 5
8 2 7 6 9 1 5 3 10 4

3 9 10 4 1 8 6 7 5 2
2 9 8 5 1 7 3 4 6 10

1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10"""

# rear(sample)

with open('/Users/oz/Downloads/rosalind_rear (1).txt') as f:
    rear(f.read().rstrip())
