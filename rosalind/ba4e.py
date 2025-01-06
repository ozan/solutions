# import utils as u

# note: using a set here based on example, but should really be a list, no?
parts = {57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131,
         137, 147, 156, 163, 186}


def cyclo(nums):
    len_p = len(nums)
    first, curr = nums[:], [0] * len_p
    out = [0, sum(first)]
    for n in range(1, len_p):
        for i in range(0, len_p):
            curr[i] += first[(i+n) % len_p]
        out.extend(curr)
    out.sort()
    return out


def ba4e(spec):
    spec_list = [int(x) for x in spec.split(' ')]
    spec = set(spec_list)
    opts = [[]]  # to stash sum to avoid re-adding
    out = []
    while opts:
        nxt = []
        for op in opts:
            if cyclo(op) == spec_list:
                out.append('-'.join(str(x) for x in op))
                continue
            for p in parts:
                if p + sum(op) in spec:
                    nxt.append(op + [p])
        opts = nxt
    print(' '.join(out))
    return out


# ba4e("0 113 128 186 241 299 314 427")


with open('/Users/oz/Downloads/rosalind_ba4e.txt') as f:
    # s, t = [x for _, x in u.scan_fasta(f)]
    # pass
    ba4e(f.read().rstrip())
