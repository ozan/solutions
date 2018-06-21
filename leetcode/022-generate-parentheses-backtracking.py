"""
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.

Strategy: backtracking search (do not traverse invalid paths)
"""

class Solution(object):

    def generateParenthesis(self, n):
        results, buff, L, R = [], [], '(', ')'

        def dfs(ls=0, rs=0):
            if len(buff) == 2*n:
                results.append(''.join(buff))
                return

            if ls < n:  # capacity to add (
                buff.append(L)
                dfs(ls + 1, rs)
                buff.pop()

            if rs < ls:  # capacity to add )
                buff.append(R)
                dfs(ls, rs + 1)
                buff.pop()

        dfs()
        return results


if __name__ == '__main__':
    sol = Solution().generateParenthesis(2)
    assert sol[0] == '(())'
    assert sol[1] == '()()'
    assert len(sol) == 2

