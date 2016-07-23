"""

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher
or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x.
You win the game when you guess the number I picked.


Given a particular n >= 1, find out how much money you need to have to
guarantee a win.


---

at any point, i have lower and upper bounds for my guess
the cost of any given guess n is n + max(f(a, n-1), f(b, n+1))
want to chose the min of cost(n) in possible ns

let's say n = 3
could guess 1, 2 or 3

cost of guessing 1 is 1 + C(2, 3)
cost of guessing 2 is 2 + max(C(1,1), C(3, 3))
cost of guessing 3 is 3 + C(1, 2)

so could do it recursively with a memo or bottom up DP

"""


class Solution(object):

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def cost(a, b):
            if a >= b:
                return 0

            if (a, b) in memo:
                return memo[(a, b)]

            res = min(
                k + max(cost(a, k - 1), cost(k + 1, b))
                for k in range(a, b + 1)
            )
            memo[(a, b)] = res
            return res

        return cost(1, n)
