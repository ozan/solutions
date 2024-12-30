from Bio import Entrez


handle = Entrez.efetch(db='nucleotide', id='JX462670 JQ796071 FJ817486 NM_001079732 NM_001159758 NM_131329 NM_001003102 JX308803 NM_001025158'.split(' '), rettype='fasta')

res = handle.read()

print(min([x for x in res.split('\n\n') if x], key=len))


