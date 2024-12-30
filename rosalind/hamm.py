

def f(s, t):
    return sum(sx != tx for sx, tx in zip(s, t))


assert f("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7
print('ok')


with open('/Users/oz/Downloads/rosalind_hamm.txt') as file:
    lines = file.readlines()
    print(f(lines[0], lines[1]))
