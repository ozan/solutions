
SCORE = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))

with open('0022_names.txt') as f:
    names = f.read().strip('"').split('","')
    names.sort()
    total = 0
    for i, name in enumerate(names):
        total += (i + 1) * sum(SCORE[letter] for letter in name)
    print(total)
