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


def ba9l(f):
    bwt = f.readline().rstrip()
    patterns = f.readline().rstrip().split(' ')

    # annotate bwt with occurence ordering
    last = annotate(bwt)
    first = annotate(sorted(bwt))

    last_to_first = dict((x, i) for i, x in enumerate(first))

    out = []
    for p in patterns:
        pattern = [c for c in p]

        top = 0
        bottom = len(last) - 1
        while top <= bottom:
            if not pattern:
                out.append(bottom - top + 1)
                break

            symbol = pattern.pop()

            ti, bi = None, None
            i = top
            while i <= bottom:
                if bwt[i] == symbol:
                    bi = i
                    if ti is None:
                        ti = i
                i += 1
            if ti is None:
                out.append(0)
                break

            top = last_to_first[last[ti]]
            bottom = last_to_first[last[bi]]

    print(' '.join(str(n) for n in out))


sample = """TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
CCT CAC GAG CAG ATC"""


# ba9l(io.StringIO(sample))


with open('/Users/oz/Downloads/rosalind_ba9l.txt') as f: ba9l(f)
