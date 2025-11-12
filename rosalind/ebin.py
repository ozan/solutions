import io
import math
import sys


MIN_PROB = sys.float_info.min


def log_prob(n, p, i):
    """
    Chance of exactly i dominant alleles in next gen of population n, given p prevalence.

    Computed in log space to avoid extremely large value of n!
    """
    coef = math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
    return coef + i * math.log(max(p, MIN_PROB)) + (n - i) * math.log(max(1 - p, MIN_PROB))


def ebin(s):
    n = int(s.readline())
    P = [float(x) for x in s.readline().split(' ')]

    out = []
    for p in P:
        expected = sum(i * math.exp(log_prob(n, p, i)) for i in range(n + 1))
        assert abs(expected - n * p) < 0.001
        out.append(expected)

    print(' '.join(f'{o:.3f}' for o in out))
    return out


sample = io.StringIO("""17
0.1 0.2 0.3""")

ebin(sample)


with open('/Users/oz/Downloads/rosalind_ebin (1).txt') as f:
    ebin(f)
