"""
Using two stacks, provide a queue interface.

Plan: maintain two stacks, one for input and one with appropriately
ordered output. To "enqueue", just push to the input stack. To "dequeue",
if the output stack is empty then transfer all members of the input stack
to the output stack, by popping from the former and pushing to the latter.
If it is not empty, simply pop the latter.

"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.out_stack:
            self._transfer()
        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.out_stack:
            self._transfer()
        return self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not (self.in_stack or self.out_stack)

    def _transfer(self):
        """
        Move all members from in_stack to out_stack, in appropriate order.
        """
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())


if __name__ == '__main__':
    q = MyQueue()
    assert q.empty()
    q.push('A')
    assert not q.empty()
    q.push('B')
    assert q.peek() == 'A'
    assert q.pop() == 'A'
    q.push('C')
    assert q.pop() == 'B'
    assert q.pop() == 'C'
    assert q.empty()
    print('ok')
