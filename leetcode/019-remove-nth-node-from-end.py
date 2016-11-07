# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        current = head
        stack = []
        while current is not None:
            stack.append(current)
            current = current.next
        for _ in range(n):
            current = stack.pop()
        try:
            prior = stack.pop()
        except IndexError:
            return current.next
    
        prior.next = current.next
        return head
