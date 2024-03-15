def f(genome, pattern):
    ii = []
    for i in range(len(genome)):
        for j in range(len(pattern)):
            if i + j >= len(genome) or genome[i+j] != pattern[j]:
                break
        else:
            ii.append(i)
    return ii


print(' '.join(str(i) for i in f('GATATATGCATATACTT', 'ATAT')))
