def sign(n):

    def inner(choices):
        if len(choices) == 0:
            return [[]]

        return [[s * x] + rest
                for s in (-1, 1)
                for i, x in enumerate(choices)
                for rest in inner(choices[:i] + choices[i+1:])]

    perms = inner(list(range(1, n + 1)))
    print(len(perms))
    for p in perms:
        print(' '.join(map(str, p)))


print(sign(6))
