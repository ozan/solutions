
def fibo(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


print(fibo(24))

# with open('/Users/oz/Downloads/rosalind_kmp.txt') as f:


