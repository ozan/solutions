
PAIRS = dict(zip('([{', ')]}'))


def check_brackets(xs):
    stack = []
    for x in xs:
        if x in PAIRS:
            stack.append(x)
        else:
            if len(stack) == 0 or not PAIRS[stack.pop()] == x:
                return False  # right skewed or mismatch respectively
    return len(stack) == 0  # ok or left skewed
