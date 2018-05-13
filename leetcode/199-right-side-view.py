
class Solution(object):
    def rightSideView(self, root):
        res, level = [], [root]
        while root and level:
            res.append(level[-1].val)
            level = [child for n in level for child in (n.left, n.right) if child]
        return res
        