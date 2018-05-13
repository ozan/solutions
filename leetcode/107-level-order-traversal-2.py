
class Solution(object):
    def levelOrderBottom(self, root):
        res, level = [], [root]
        while root and level:
            res.append([n.val for n in level])
            level = [child for n in level for child in (n.left, n.right) if child]
        res.reverse()
        return res