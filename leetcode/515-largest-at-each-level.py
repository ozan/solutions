
class Solution(object):
    def largestValues(self, root):
        res, level = [], [root]
        while root and level:
            res.append(max(n.val for n in level))
            level = [child for n in level for child in (n.left, n.right) if child]
        return res
        