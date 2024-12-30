from io import StringIO


def scan_fasta(source):
    source = StringIO(source) if isinstance(source, str) else source

    desc, seq = None, []
    while True:
        line = source.readline().rstrip()
        if line == '' or line[0] == '>':
            if desc:
                yield (desc, ''.join(seq))
            if not line:
                return
            desc, seq = line[1:], []
        else:
            seq.append(line)


comp = dict(zip('ACGT', 'TGCA'))


def reverse_comp(s):
    for x in reversed(s):
        yield comp[x]


trans = dict(zip('ACGT', 'UGCA'))


def transcribe(x):
    return trans[x]


codon_table = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': None, 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': None, 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': None, 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def translate(codon):
    return codon_table[codon]
