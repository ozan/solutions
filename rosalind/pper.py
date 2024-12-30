def pper(n, k):
    tot = 1
    for _ in range(k):
        tot = (tot * n) % 1000000
        n -= 1
    return tot


print(pper(97, 9))
