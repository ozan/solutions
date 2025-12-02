from collections import defaultdict


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


def ba9j(bwt):
    """Given the BWT of text, find text"""

    # annotate bwt with occurence ordering
    last = annotate(bwt)
    first = annotate(sorted(bwt))

    lookup = dict(zip(last, first))

    text = []
    nxt = ('$', 1)
    while len(text) < len(bwt):
        nxt = lookup[nxt]
        text.append(nxt[0])

    print(''.join(text))


# ba9j('TTCCTAACG$A')

with open('/Users/oz/Downloads/rosalind_ba9j.txt') as f: ba9j(f.read().rstrip())

