import heapq

sample = """0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3""".split('\n')


def run(case):
    start, end = case[0], case[1]
    weights = {}
    for line in case[2:]:
        a, rest = line.split('->')
        b, c = rest.split(':')
        try:
            weights[a][b] = -int(c)
        except KeyError:
            weights[a] = {b: -int(c)}
    
    q = [(0, start, [start])]
    while q:
        weight, n, path = heapq.heappop(q)
        print(weight, n, path)
        if n == end:
            return -weight, '->'.join(path)
        for k, v in weights[n].items():
            heapq.heappush(q, (weight + v, k, path + [k]))
    return None


        


print(run(sample))


