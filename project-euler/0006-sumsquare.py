
def sum_square_diffence(n):
    return n * (n + 1) * (3 * n + 2) * (n - 1) // 12


assert sum_square_diffence(10) == 2640
print(sum_square_diffence(100))
