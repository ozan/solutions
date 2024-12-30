import utils as u


def hamm(s, t):
    return sum(sx != tx for sx, tx in zip(s, t))


def pdst(dataset):
    ss = [s for _, s in dataset]

    for s in ss:
        len_s = len(s)
        print(' '.join(f'{(hamm(s, t)/len_s):.5f}' for t in ss))



sample = """>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA"""

# print(pdst(u.scan_fasta(sample)))

with open('/Users/oz/Downloads/rosalind_pdst.txt') as f:
    print(pdst(u.scan_fasta(f)))
