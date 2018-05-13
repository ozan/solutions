class Solution(object):
    def zigzagLevelOrder(self, root):
        res, level = [], [root]
        while root and level:
            vals = [n.val for n in level]
            if len(res) % 2 == 1:
                vals.reverse()
            res.append(vals)
            level = [child for n in level for child in (n.left, n.right) if child]
        return res