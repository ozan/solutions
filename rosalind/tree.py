
def tree(lines):
    n = int(lines[0])
    components = []
    seen = set()

    for l in lines[1:]:
        if l == '':
            continue
        a, b = l.split(' ')
        seen.add(a)
        seen.add(b)

        cc = {a, b}
        new_components = [cc]
        for c in components:
            if a in c or b in c:
                cc |= c
            else:
                new_components.append(c)
        components = new_components

    print(len(components), n, len(seen))
    return len(components) - 1 + n - len(seen)


sample = """10
1 2
2 8
4 10
5 9
6 10
7 9
""".split('\n')


print(tree(sample))
print(tree(open('/Users/oz/Downloads/rosalind_tree (2).txt').read().split('\n')))

