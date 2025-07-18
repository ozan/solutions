"""
If all the numbers from 1 to 1000 inclusive were written out in words,
how many letters would be used?

Written inefficiently (constructing names, then counting) to aid in debugging
"""


numerals = ' one two three four five six seven eight nine'.split(' ')
teens = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ')
tys = '? ? twenty thirty forty fifty sixty seventy eighty ninety'.split(' ')


def letter_count(limit):
    counts = 0

    def name(n):
        if n < 10:
            return numerals[n]
        if n < 20:
            return teens[n-10]
        if n < 100:
            return f'{tys[n // 10]}{numerals[n % 10]}'
        if n < 1000:
            if n % 100 == 0:
                return f'{numerals[n // 100]}hundred'
            return f'{numerals[n // 100]}hundredand{name(n % 100)}'
        if n == 1000:
            return 'onethousand'

    for n in range(1, limit+1):
        counts += len(name(n))

    return counts


assert letter_count(5) == 19
print(letter_count(1000))
