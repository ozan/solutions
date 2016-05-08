# strategy:
# generate palindromes between min_factor ^2 and max_factor^2 in the
# appropriate direction, then try to factor each one


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def smallest_palindrome(max_factor, min_factor=0):
    for a in range(min_factor, max_factor + 1):
        for b in range(a, )

def largest_palindrome(max_factor, min_factor=0):
    pass
