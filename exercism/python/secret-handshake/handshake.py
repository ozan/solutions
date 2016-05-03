
ACTIONS = ('wink', 'double blink', 'close your eyes', 'jump')


def handshake(key):
    try:
        n = key if type(key) == int else int(key, 2)
    except ValueError:
        return []
    if n <= 0:
        return []
    return shake(n)


def shake(n):
    step = 1 - 2 * int(16 & n > 0)
    return [act for i, act in enumerate(ACTIONS) if 1 << i & n][::step]


def code(instructions):
    if not set(instructions).issubset(set(ACTIONS)):
        return '0'
    nums = [1 << ACTIONS.index(act) for act in instructions]
    return strbin(sum(nums) + 16 * int(nums != sorted(nums)))


def strbin(n):
    return str(bin(n))[2:]
