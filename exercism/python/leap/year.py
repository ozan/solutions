
def divides(n):
    return lambda d: n % d == 0


def is_leap_year(year):
    div = divides(year)
    return div(400) or div(4) and not div(100)
