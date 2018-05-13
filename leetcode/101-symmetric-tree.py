class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isReflected(root.left, root.right)
    
    def isReflected(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and self.isReflected(left.left, right.right) and self.isReflected(left.right, right.left)
