
def is_palindrome(n):
    return str(n) == str(n)[::-1]


def palindromes_in_range(max_factor, min_factor):
    return [
        [a * b, [a, b]]
        for a in range(min_factor, max_factor + 1)
        for b in range(a, max_factor + 1)
        if is_palindrome(a * b)
    ]


def smallest_palindrome(max_factor, min_factor=1):
    return min(palindromes_in_range(max_factor, min_factor))


def largest_palindrome(max_factor, min_factor=0):
    return max(palindromes_in_range(max_factor, min_factor))
