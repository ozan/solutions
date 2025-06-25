"""

Consider a rooted binary tree with n leaves. It must have n - 1 internal nodes, n external
edges, and n - 2 internal edges, for a total of 2n - 2 edges. Given any rooted binary tree with
n leaves, we could construct an n + 1 leaved tree by splitting on any existing edge to add
the leaf, OR by constructing a new root with the added leaf as a child. Hence,

b(n + 1) = b(n) * (2n - 1)

Rewriting as k = n + 1, we have:

b(k) = b(k - 1) * (2k - 3)

We only need one base case, so can use b(2) = 1
"""


def root(n):
    b = 1

    for k in range(3, n + 1):
        b = (b * (k + k - 3)) % 1000000

    return b


assert root(4) == 15

print(root(939))
