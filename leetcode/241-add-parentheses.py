from collections import deque

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}


def tokenize(expr):
    num = ''
    for char in expr:
        if char in operations:
            if num:
                yield int(num)
                num = ''
            yield operations[char]
        else:
            num += char
    yield int(num)


def product(xs, ys):
    for x in xs:
        for y in ys:
            yield x, y


def possible_values(items):
    if len(items) == 1:
        return [items[0]]

    left = []
    right = deque(items)
    values = []
    while len(right) >= 2:
        left.append(right.popleft())
        op = right.popleft()
        left_vals = possible_values(left)
        right_vals = possible_values(right)
        values += [op(x, y) for x, y in product(left_vals, right_vals)]
        left.append(op)
    return values


class Solution(object):
    def diffWaysToCompute(self, input):
        items = list(tokenize(input))
        return possible_values(items)
