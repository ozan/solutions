class Node(object):
    def __init__(self, val):
        self.val = val
        self.left_children = 0
        self.how_many = 1
        self.left = None
        self.right = None


class BTree(object):
    def __init__(self):
        self.head = None

    def add(self, n):
        if self.head is None:
            self.head = Node(n)
            return 0
        parent = None
        node = self.head
        last_step = None  # TODO: fix hack
        cumulative_lt = 0
        while node:
            if n < node.val:
                node.left_children += 1
                node, parent = node.left, node
                last_step = 'left'
            elif n > node.val:
                cumulative_lt += node.left_children + node.how_many
                node, parent = node.right, node
                last_step = 'right'
            else:
                node.how_many += 1
                return cumulative_lt + node.left_children
        setattr(parent, last_step, Node(n))
        return cumulative_lt


def count_smaller(nums):
    tree = BTree()
    for n in reversed(nums):
        yield tree.add(n)


class Solution(object):
    def countSmaller(self, nums):
        return list(reversed(list(count_smaller(nums))))
        