
def perm(n):

    def f(choices):
        if len(choices) <= 1:
            return [choices]

        out = []
        for i, x in enumerate(choices):
            out.extend([x] + etc for etc in f(choices[:i] + choices[i+1:]))
        return out

    res = f(list(range(1, n + 1)))
    print(len(res))
    for r in res:
        print(' '.join(map(str, r)))


print(perm(5))
