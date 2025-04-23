masses = [
    ('A', 71.03711),
    ('C', 103.00919),
    ('D', 115.02694),
    ('E', 129.04259),
    ('F', 147.06841),
    ('G', 57.02146),
    ('H', 137.05891),
    ('I', 113.08406),
    ('K', 128.09496),
    ('L', 113.08406),
    ('M', 131.04049),
    ('N', 114.04293),
    ('P', 97.05276),
    ('Q', 128.05858),
    ('R', 156.10111),
    ('S', 87.03203),
    ('T', 101.04768),
    ('V', 99.06841),
    ('W', 186.07931),
    ('Y', 163.06333)]


def find_close(x):
    for aa, mass in masses:
        if abs(x - mass) < 0.001:
            return aa


def spec(data):
    pref = [float(x) for x in data]
    out = []
    for i in range(1, len(pref)):
        diff = pref[i] - pref[i-1]
        aa = find_close(diff)
        if aa:
            out.append(aa)
    return ''.join(out)


sample = """3524.8542
3710.9335
3841.974
3970.0326
4057.0646""".split('\n')


print(spec(sample))


with open('/Users/oz/Downloads/rosalind_spec.txt') as f:
    print(spec(f.read().rstrip().split('\n')))
