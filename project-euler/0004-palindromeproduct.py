"""
Find the largest palindrome product of two 3-digit numbers.

"""

import heapq


def is_palindrome(n):
    ns = str(n)
    return ns == ns[::-1]


def largest_palindrome_brute(dig):
    """
    Absolute brute force: iterate (n, m) from (100, 100) to (999, 999) testing each
    to be palindrome... this is around 400K tests, so runs in 10s of ms already.
    """
    a, b = 10**(dig-1), 10**dig
    best = (-1, None, None)

    for n in range(a, b):
        for m in range(n, b):
            prod = n * m
            if is_palindrome(prod):
                best = max(best, (prod, n, m))

    return best


def largest_palindrome(dig):
    """
    Start with (N, N), then for each (n, m) that comes off the pqueue, test
    it before adding (n-1,m) and (n, m-1) to the queue. We can also enforce n >= m to reduce
    the search further. This gets the 4 digit search back to 10s of ms, as it can for
    5 or 6 digit search. It can do up to 9 digit search in less than a minute.

    Results:

    2   99          91          9009
    3   993         913         906609
    4   9999        9901        99000099
    5   99999       99901       990090099
    6   999999      999001      999000000999
    7   9998017     9997647     99956644665999
    8   99999999    99990001    9999000000009999
    9   999980347   999920317   999900665566009999

    Further work would likely use some analysis to filter candidates
    """
    b = 10**dig - 1

    q = []
    heapq.heappush(q, (-b*b, b, b))

    last = -1
    while q:
        neg_prod, n, m = heapq.heappop(q)
        prod = -neg_prod
        if prod == last:
            continue
        last = prod
        if is_palindrome(prod):
            return prod, n, m

        heapq.heappush(q, (-(prod - n), n, m - 1))
        if n - 1 >= m:
            heapq.heappush(q, (-(prod - m), n - 1, m))

    return None


print(largest_palindrome(9))
