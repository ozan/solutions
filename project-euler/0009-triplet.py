"""
Find a Pythagorean triplet for which a + b + c = 1000

This is easy enough to brute force with the constraint a <= b <= c, so consider:

    a in the range 1 to 1000 / 3
    b in the range a to (1000 - a) / 2
    c then determined as 1000 - a - b, and we can just check if a * a + b * b == c * c

This is O(n**2) and in fact only 83,333 inner loops

"""


def triples(n):
    inner = 0
    for a in range(1, n//3 + 1):
        count = 0
        for b in range(a, (n-a)//2 + 1):
            count += 1
            inner += 1
            c = n - a - b
            if a * a + b * b == c * c:
                print(f'{a}^2 + {b}^2 = {c}^2, abc = {a * b * c}')
                return


print(triples(1000))
