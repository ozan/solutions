sample = """4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2""".split('\n')

[0, 3, 5, 9, 9]
[1, 4, 7, 13, 15]


def longest(case):
    n, m = map(int, case[0].split(' '))
    down = [[int(c) for c in line.split(' ')] for line in case[1:n+1]]
    right = [[int(c) for c in line.split(' ')] for line in case[n+2:]]

    best = [0] * (m + 1)

    for i in range(0, n):
        for j in range(m + 1):
            best[j] = max(
                best[j] + down[i][j],
                0 if j == 0 else best[j - 1] + right[i + 1][j - 1])

    return best[-1]



print(longest((sample)))

print(longest(("""17 12
0 1 3 2 0 0 4 3 4 4 2 1 4
4 2 0 3 0 2 3 3 2 0 3 4 2
0 3 1 1 4 4 1 3 3 4 0 2 2
4 2 2 4 0 2 4 1 2 0 3 2 3
4 4 1 1 1 4 3 4 0 1 1 4 0
3 2 3 0 4 3 4 4 1 0 0 4 2
3 1 0 4 2 1 0 0 4 4 3 3 3
2 1 3 4 3 3 2 2 4 4 0 3 4
1 1 0 0 0 4 2 1 1 4 1 4 3
4 4 3 0 1 1 2 2 1 4 1 0 3
0 0 3 1 4 3 3 0 0 4 1 2 4
1 3 3 1 3 4 1 4 0 1 2 1 3
2 4 2 3 1 3 4 0 1 3 1 1 0
1 2 2 2 0 0 2 1 3 2 1 2 3
4 0 1 3 0 4 0 2 2 0 3 2 4
0 1 1 1 4 0 3 0 2 3 0 2 2
4 4 1 1 3 0 1 1 0 2 1 3 3
-
2 0 2 1 2 3 1 4 0 0 0 3
2 2 1 1 3 0 1 2 3 1 0 3
4 3 0 4 1 0 2 4 0 0 2 0
0 0 3 0 2 1 0 0 3 3 2 3
3 1 3 3 2 3 1 3 0 0 0 3
0 0 1 1 1 4 1 0 2 0 3 3
0 3 3 1 4 2 3 1 3 0 2 3
2 4 2 2 0 2 1 3 4 0 0 4
1 3 0 1 4 1 2 1 4 2 1 3
4 3 3 4 3 0 3 4 3 2 1 1
4 2 1 1 1 3 0 0 4 4 3 3
3 2 4 0 0 0 2 1 0 4 3 0
3 4 3 4 1 0 1 1 3 3 2 1
1 2 1 3 4 2 1 1 4 4 2 0
2 1 3 2 0 4 2 4 4 0 1 3
3 4 0 3 2 0 0 1 0 0 2 0
0 4 3 3 3 1 0 1 3 1 3 0
1 1 4 2 2 0 0 4 0 3 3 2""".split('\n'))))

