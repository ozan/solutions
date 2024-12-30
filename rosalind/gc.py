
def gc(lines):
    tots = {}

    curr_id, curr_gc, curr_at = None, 0, 0

    for line in lines:
        if line and line[0] == '>':
            if curr_id:
                tots[curr_id] = curr_gc / (curr_gc + curr_at)
            curr_id, curr_gc, curr_at = line[1:], 0, 0
            continue
        for c in line:
            if c == 'G' or c == 'C':
                curr_gc += 1
            elif c == 'A' or c == 'T':
                curr_at += 1

    tots[curr_id] = curr_gc / (curr_gc + curr_at)

    max_id, max_gc = max(tots.items(), key=lambda x: x[1])

    print(max_id)
    print(max_gc * 100)

    return max_id, max_gc


sample = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
""".split('\n')


# print(gc(sample))

print(gc(open('/Users/oz/Downloads/rosalind_gc (2).txt').read().split('\n')))
