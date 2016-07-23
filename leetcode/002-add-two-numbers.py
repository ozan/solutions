# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        current = None
        carry = 0
        x, y = l1, l2
        while x or y:
            xv = x and x.val or 0
            yv = y and y.val or 0
            tot = xv + yv + carry
            dig = tot % 10
            carry = tot / 10
            nxt = ListNode(dig)
            if head:
                current.next = nxt
            else:
                head = nxt
            current = nxt
            x = x and x.next
            y = y and y.next
        if carry:
            final = ListNode(carry)
            current.next = final
        return head
