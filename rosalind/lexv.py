

def lexv(chars, n):
    if n == 1:
        return chars

    return [
        c + rest
        for c in chars for rest in lexv(chars, n - 1)
        if not (rest and not c)
    ]


# print('\n'.join(lexv(['', 'D', 'N', 'A'], 3)))
print('\n'.join(lexv(['', 'T', 'H', 'N', 'V', 'J', 'G', 'U', 'K', 'Y', 'P', 'O'], 4)))
