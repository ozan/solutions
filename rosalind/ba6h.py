

def parse(data):
    i = 0
    out = []
    while i < len(data):
        j = data.find(')', i)
        out.append([int(x) for x in data[i+1:j].split()])
        i = j+1
    return out


def ba6h(data):
    parts = parse(data)

    edges = []
    for part in parts:
        for i, x in enumerate(part):
            y = part[(i+1) % len(part)]
            frm = x*2 if x > 0 else -x*2-1
            to = y*2-1 if y > 0 else -y*2
            edges.append((frm, to))

    print(', '.join(str(edge) for edge in edges))


sample = '(+1 -2 -3)(+4 +5 -6)'
#ba6h(sample)

with open('/Users/oz/Downloads/rosalind_ba6h.txt') as f:
    ba6h(f.read().strip())

