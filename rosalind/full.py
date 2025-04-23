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


def full(data):
    mass = float(data[0])
    L = [float(x) for x in data[1:]]
    L.sort()
    prior = None
    half = L[:len(L) // 2]
    half.sort(reverse=True)
    out = []
    while half:
        x = half.pop()
        if prior is None:
            prior = x
            continue
        diff = abs(x - prior)
        match = find_close(diff)
        if match:
            out.append(match)
            prior = x
        else:
            half.append(mass - x)
            half.sort(reverse=True)

    return ''.join(out)


sample = """1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091""".split('\n')


print(full(sample))


with open('/Users/oz/Downloads/rosalind_full.txt') as f:
    print(full(f.read().rstrip().split('\n')))
