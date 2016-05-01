
d_to_r = dict(zip('GCTA', 'CGAU'))


def to_rna(dna):
    return ''.join(d_to_r[d] for d in dna)
