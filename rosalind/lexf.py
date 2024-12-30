
def lexf(chars, n):
    if n == 1:
        return list(chars)

    return [c + rest for c in chars for rest in lexf(chars, n - 1)]


# print('\n'.join(lexf('ACGT', 2)))
print('\n'.join(lexf('ABCDEFGH', 3)))
