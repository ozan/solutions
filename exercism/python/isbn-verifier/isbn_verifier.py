
def digits(isbn):
    try:
        *xs, checksum = isbn
    except ValueError:
        return
    # non-checksum digits
    for x in xs:
        if x.isdigit():
            yield int(x)
    # checksum digit
    if checksum == 'X':
        yield 10
    if checksum.isdigit():
        yield int(checksum)


def is_valid(isbn):
    summands = [(10-i) * n for i, n in enumerate(digits(isbn))]
    return len(summands) == 10 and sum(summands) % 11 == 0
