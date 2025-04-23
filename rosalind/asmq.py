

def asmq(contigs):
    lens = [len(c) for c in contigs]
    total = sum(lens)

    n75 = 1
    while True:
        s75 = sum(l for l in lens if l >= (n75 + 1))
        if s75 / total < 0.75:
            break
        n75 += 1

    n50 = n75
    while True:
        s50 = sum(l for l in lens if l >= (n50 + 1))
        if s50 / total < 0.5:
            break
        n50 += 1
    return n50, n75


sample = """GATTACA
TACTACTAC
ATTGAT
GAAGA""".split('\n')

print(asmq(sample))


with open('/Users/oz/Downloads/rosalind_asmq.txt') as f:
    print(asmq(f.read().rstrip().split('\n')))
