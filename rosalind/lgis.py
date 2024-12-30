# from io import StringIO
# import utils as u


def lgis(nums):
    best_ending_at = [[nums[0]]]

    for end in range(1, len(nums)):
        opts = [[]]
        for i in range(end):
            if nums[i] < nums[end]:
                opts.append(best_ending_at[i])
        best_ending_at.append(max(opts, key=len) + [nums[end]])

    return max(best_ending_at, key=len)


sample = """5
0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15
"""

# print(revp(next(u.scan_fasta(sample))[1]))

# f = StringIO(sample)

with open('/Users/oz/Downloads/rosalind_lgis (1).txt') as f:
    f.readline()  # skip first
    nums = list(map(int, f.readline().rstrip().split(' ')))
    print(' '.join(map(str, lgis(nums))))
    print(' '.join(map(str, reversed(lgis(list(reversed(nums)))))))
#    print(revp(next(u.scan_fasta(f))[1]))
