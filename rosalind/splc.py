"""
The easy, ineffecient way to do this would be to repeatedly construct new
strings by finding and splicing each intron one after another.

Let's instead do it the hard, efficent way: one single scan to greedily
identify the start and end points of each intron, then another scan to
translate AAs from the _original_ string, skipping the indexes of introns
"""

import itertools as it

aas = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': None, 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': None, 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': None, 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def splice(s, intron_ranges):
    ir = iter(intron_ranges)

    try:
        start, end = next(ir)
    except StopIteration:
        start, end = None, None

    for i, c in enumerate(s):

        if end and i == end:
            try:
                start, end = next(ir)
            except StopIteration:
                start, end = None, None

        if start and start <= i < end:
            continue

        yield c


def splc(lines):
    # parse input
    parts = []
    s = None
    introns = []
    for line in lines:
        if line == '' or line[0] == '>':
            if len(parts) == 0:
                continue
            if s is None:
                s = ''.join(parts)
            else:
                introns.append(''.join(parts))
            parts = []
        else:
            parts.append(line)

    # scan ONCE to find ranges of each intron
    intron_ranges = []  # [start, end)   ... ie inclusive/exclusive!

    candidates = []
    for i, c in enumerate(s):
        next_candidates = []
        just_added = False
        for intrn, start in candidates:
            di = i - start
            if intrn[di] != c:
                continue
            if di == len(intrn) - 1:
                intron_ranges.append((start, start + di + 1))
                next_candidates = []
                just_added = True
                break
            else:
                next_candidates.append((intrn, start))
        if not just_added:
            for intrn in introns:
                if intrn[0] == c:
                    next_candidates.append((intrn, i))
        candidates = next_candidates

    # scan ONCE more to to split and translate
    out = []
    for codon in it.batched(splice(s, intron_ranges), n=3):
        aa = aas[''.join(codon)]
        if aa is None:
            break
        out.append(aa)
    return ''.join(out)


sample = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
""".split('\n')

# assert splc(sample) == 'MVYIADKQHVASREAYGHMFKVCA'

print(splc(open('/Users/oz/Downloads/rosalind_splc (1).txt').read().split('\n')))
