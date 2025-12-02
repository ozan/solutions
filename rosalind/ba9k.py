from collections import defaultdict
import io


def annotate(xs):
    """
    Given a sequence, return a list of pairs annotating each item with its occurence
    """
    counts = defaultdict(lambda: 0)
    out = []
    for x in xs:
        counts[x] += 1
        out.append((x, counts[x]))
    return out


def ba9k(f):
    bwt = f.readline().rstrip()
    i = int(f.readline())

    # annotate bwt with occurence ordering
    last = annotate(bwt)
    first = annotate(sorted(bwt))

    print(first.index(last[i]))  # if we were doing this many times, we would use a dict
    return


sample = """T$GACCA
3"""

# ba9k(io.StringIO(sample))


with open('/Users/oz/Downloads/rosalind_ba9k.txt') as f: ba9k(f)

