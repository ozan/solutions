
def iprb(k, m, n):
    t = k + m + n
    aa_aa = n * (n - 1)
    Aa_aa = aa_Aa = n * m
    Aa_Aa = m * (m - 1)
    aa_daughter = aa_aa + 0.5 * Aa_aa + 0.5 * aa_Aa + 0.25 * Aa_Aa
    return 1 - aa_daughter / (t * (t - 1))


print(iprb(2, 2, 2))
print(iprb(22, 24, 28))
