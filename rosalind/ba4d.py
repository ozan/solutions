# import utils as u

# note: using a set here based on example, but should really be a list, no?
parts = {57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131,
         137, 147, 156, 163, 186}


def ba4d(n):
    memo = [1]
    for i in range(1, n + 1):
        memo.append(sum(memo[i-p] for p in parts if i >= p))
    return memo[-1]


print(ba4d(1265))


# with open('/Users/oz/Downloads/rosalind_ba4b.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    # print(ba4b(*f.read().rstrip().split('\n')))
