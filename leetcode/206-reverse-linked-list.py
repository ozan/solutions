class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        prior = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prior
            prior = current
            current = next_node

        return prior
