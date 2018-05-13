
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = [root]
        while level:
            left = level[0].val
            level = [child for n in level for child in (n.left, n.right) if child]
        return left
        