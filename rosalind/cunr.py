"""

Consider an unrooted binary tree with n leaves. It must have n - 2 internal nodes, connected
by n - 3 internal edges. The n leaves are each connected by one external edge. So there are a
total of (n - 3) + n edges. An unrooted binary tree of n + 1 leaves can then be made by splitting
one of these trees on any of its 2n - 3 edges, in other words b(n + 1) = b(n) * (2n - 3).

Rewriting with k = n + 1, our recurrence relation is:

b(k) = b(k - 1) * (2k - 5)

We only need one base case for this, so can use b(3) = 1
"""


def cunr(n):
    b = 1

    for k in range(4, n + 1):
        b = (b * (k + k - 5)) % 1000000

    return b


assert cunr(5) == 15
print(cunr(843))
