import urllib.request


def get_locations(lines):
    chars = ''.join(lines[1:])
    locations = []
    for i, c in enumerate(chars[:-3]):
        d, e, f = chars[i+1:i+4]
        if c == 'N' and d != 'P' and e in 'ST' and f != 'P':
            locations.append(i + 1)
    return locations

sample = """A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST"""


def mprt(id_source):
    for uniprot_id in id_source.split('\n'):
        uniprot_id_short = uniprot_id.split('_')[0]
        url = f'https://rest.uniprot.org/uniprotkb/{uniprot_id_short}.fasta'
        with urllib.request.urlopen(url) as f:
            fasta = f.read().decode('utf-8')
        locs = get_locations(fasta.split('\n'))
        if len(locs) > 0:
            print(uniprot_id)
            print(' '.join(map(str, locs)))


# mprt(sample)

with open('/Users/oz/Downloads/rosalind_mprt (1).txt') as f:
    mprt(f.read().rstrip())
