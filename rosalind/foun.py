"""
TODO got stuck on the logprob stuff... probably best to carefully start again when
feeling better
"""

import io
import math
import sys


MIN_FLOAT = sys.float_info.min


def logsumexp(log_probs):
    """
    Compute log(sum(exp(log_probs))) in a numerically stable way
    """
    mx = max(log_probs)
    return mx + math.log(sum(math.exp(x - mx) for x in log_probs))


def prob(N, m, k):
    """
    Chance of exactly k copies of an allele in next generation of population N given m in current
    """
    p = m / (N + N)
    coef = math.lgamma(N+N+1) - math.lgamma(k+1) - math.lgamma(N+N-k+1)
    return coef + k * math.log(max(p, MIN_FLOAT)) + (N+N-k) * math.log(max(1-p, MIN_FLOAT))


def foun(f):
    N, m = map(int, f.readline().split(' '))
    A = list(map(int, f.readline().split(' ')))

    # transition matrix in natural log space
    M = [[prob(N, i, j) for i in range(N+N+1)] for j in range(N+N+1)]

    out = [[0] * len(A) for _ in range(m)]
    for j, a in enumerate(A):
        # initialize probability vector based on given a
        xs = [0.0 if i == a else float('-inf') for i in range(N+N+1)]

        for g in range(m):  # for each generation
            xs = [
                logsumexp([x + M[k][i] for i, x in enumerate(xs)])
                for k in range(N+N+1)
            ]
            out[g][j] = xs[0]

    for row in out:
        print(' '.join(f'{x / math.log(10):.10f}' for x in row))



sample = io.StringIO("""4 3
0 1 2""")

foun(sample)

with open('/Users/oz/Downloads/rosalind_foun.txt') as f:
    foun(f)
