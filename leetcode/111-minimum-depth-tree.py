class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        level, depth = [root], 1
        while True:
            next_level = []
            for node in level:
                if node.left is None and node.right is None:
                    return depth
                next_level.extend([ch for ch in (node.left, node.right) if ch])
            level = next_level
            depth += 1