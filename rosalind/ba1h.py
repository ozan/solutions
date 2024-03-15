

def f(pattern, text, d):
    res = []
    for i in range(len(text) - len(pattern) + 1):
        dist = 0
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                dist += 1
            if dist > d:
                break
        else:
            res.append(i)
    return res


print(f('ATTCTGGA', 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC', 3))
