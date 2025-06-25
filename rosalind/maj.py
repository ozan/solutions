import io


sample = io.StringIO("""4 8
5 5 5 5 5 5 5 5
8 7 7 7 1 7 3 7
7 1 6 5 10 100 1000 1
5 1 6 7 1 1 10 1""")


def maj(xs, a, b):
    """
    A divide and conquer algorithm, because I didn't know about (or think of)
    Moore's voting algorithm
    """
    n = b - a
    if n == 0: return None
    if n == 1: return xs[a]

    spl = a + (n // 2)
    cl, cr = maj(xs, a, spl), maj(xs, spl, b)

    if cl is None and cr is None: return None  # neither has majority
    if cl == cr: return cl  # majority is the same

    numl, numr = 0, 0
    for i in range(a, b):
        if xs[i] == cl:
            numl += 1
        elif xs[i] == cr:
            numr += 1
    if numl > n / 2:
        return cl
    if numr > n / 2:
        return cr
    return None


def moore(xs):
    cand, n = xs[0], 0
    for x in xs:
        n += 1 if x == cand else -1
        if n <= 0:
            cand, n = x, 1

    # if there is a majority element, it must be cand. check that it is
    return cand if xs.count(cand) > len(xs) / 2 else -1


def run(data):
    k, n = map(int, data.readline().split())
    out = []
    for line in data.readlines():
        answ = moore([int(x) for x in line.split()])
        out.append(-1 if answ is None else answ)
    print(' '.join(str(x) for x in out))


# run(sample)

with open('/Users/oz/Downloads/rosalind_maj.txt') as f:
    run(f)
