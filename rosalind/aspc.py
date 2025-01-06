

def aspc(n, m):
    fact = [1]
    for i in range(1, n+1):
        fact.append(fact[-1] * i)

    tot = 0
    for k in range(m, n + 1):
        tot += fact[n] // (fact[k] * fact[n-k])
    return tot % 1000000



print(aspc(1753, 1279))

# with open('/Users/oz/Downloads/rosalind_dbru.txt') as f:
    # dbru(f.read().rstrip().split('\n'))
