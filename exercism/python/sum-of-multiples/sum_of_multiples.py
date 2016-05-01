
def sum_of_multiples(n, factors):
    positive_factors = set(factors) - set([0])
    has_divisor = lambda m: any(m % d == 0 for d in positive_factors)
    return sum(filter(has_divisor, range(n)))
