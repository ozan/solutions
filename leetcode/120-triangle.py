inf = float('infinity')


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        choices = [0]
        for layer in triangle:
            choices = [inf] + choices + [inf]
            best_choices = map(min, zip(choices[:-1], choices[1:]))
            choices = map(sum, zip(layer, best_choices))

        return min(choices)
