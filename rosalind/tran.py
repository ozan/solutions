from utils import scan_fasta

transit = dict(zip('AGCT', 'GATC'))


def tran(dataset):
    _, s = next(dataset)
    _, t = next(dataset)
    c = sum(1j if transit[sx] == tx else 1 for sx, tx in zip(s, t) if sx != tx)
    return c.imag / c.real


sample = """>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT"""


print(tran(scan_fasta(sample)))

with open('/Users/oz/Downloads/rosalind_tran.txt') as f:
    print(tran(scan_fasta(f)))
