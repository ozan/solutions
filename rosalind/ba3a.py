# import utils as u


def ba3a(data):
    k = int(data[0])
    text = data[1]

    print('\n'.join(sorted(text[i:i+k] for i in range(len(text)-k+1))))


sample = """5
CAATCCAAC""".split('\n')

# print(ba3a(sample))


with open('/Users/oz/Downloads/rosalind_ba3a.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    ba3a(f.read().rstrip().split('\n'))
