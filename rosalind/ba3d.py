# import utils as u
import itertools as it


def ba3d(data):
    n = int(data[0]) - 1  # n = k - 1, since prob defines k as kmer length
    text = data[1]
    
    # Plan:
    # Construct adjacency list as tuples
    # Sort lexicographically to bring like source vertices together
    # Group by source vertex
    # Output is source -> neighbor1,neighor2 etc
    pairs = sorted((text[i:i+n], text[i+1:i+n+1]) for i in range(len(text) - n))
    for source, neighbors in it.groupby(pairs, lambda x: x[0]):
        print(f'{source} -> {",".join(n[1] for n in neighbors)}')



sample = """4
AAGATTCTCTAC""".split('\n')

# ba3d(sample)


with open('/Users/oz/Downloads/rosalind_ba3d.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    print(ba3d(f.read().rstrip().split('\n')))
