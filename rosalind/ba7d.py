
def dist(D, c1, c2):
    """
    Distance between two clusters is sum of pairwise distances, divided by
    product of cardinalities
    """
    return sum(D[x1][x2] for x1 in c1 for x2 in c2) / (len(c1) * len(c2))


def ba7d(data):
    n = int(data[0])
    D = [[int(x) for x in row.split()] for row in data[1:]]

    clusters = {i: [i] for i in range(n)}
    T = {i: [] for i in range(n)}
    ages = {i: 0 for i in range(n)}

    while len(clusters) > 1:
        # find the two closest clusters
        closest, cl_i, cl_j = float('inf'), None, None
        keys = list(clusters.keys())
        for i in range(len(keys)):
            for j in range(i+1, len(keys)):
                d = dist(D, clusters[keys[i]], clusters[keys[j]])
                if d < closest:
                    closest, cl_i, cl_j = d, keys[i], keys[j]
        
        # merge Ci and Cj into a new cluster Cnew with |Ci| + |Cj| elements
        c_new = len(T)
        clusters[c_new] = clusters[cl_i] + clusters[cl_j]
        
        # remove Ci and Cj from Clusters 
        del clusters[cl_i]
        del clusters[cl_j]

        # add a new node labeled by cluster Cnew to T
        # connect node Cnew to Ci and Cj by directed edges 
        T[c_new] = [cl_i, cl_j]
        ages[c_new] = closest / 2
    
    for x, ys in T.items():
        for y in ys:
            age = ages[x] - ages[y]
            print(f'{x}->{y}:{age:.3f}')
            print(f'{y}->{x}:{age:.3f}')
    return


sample = """4
0   20  17  11
20  0   20  13
17  20  0   10
11  13  10  0""".split('\n')

print(ba7d(sample))

with open('/Users/oz/Downloads/rosalind_ba7d (1).txt') as f:
    ba7d(f.read().rstrip().split('\n'))
