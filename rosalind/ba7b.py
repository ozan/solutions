

def ba7b(data):
    n, j = int(data[0]), int(data[1])
    D = [[int(x) for x in row.split()] for row in data[2:]]

    return min(D[j][i] + D[j][k] - D[i][k]
               for i in range(n) for k in range(i+1, n)
               if i != j and k != j) // 2


sample = """4
1
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0""".split('\n')

print(ba7b(sample))

with open('/Users/oz/Downloads/rosalind_ba7b.txt') as f:
    print(ba7b(f.read().rstrip().split('\n')))
