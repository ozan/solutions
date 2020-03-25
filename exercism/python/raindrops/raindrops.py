divisors = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))


def convert(n):
    return ''.join(word for d, word in divisors if n % d == 0) or str(n)
